from multiprocessing import Pool, cpu_count
from pdf_doc import PdfDoc
from difflib import SequenceMatcher
import argparse

class MatchBlocks:
    def __init__(self, pdf_docs: list, threshold: float):
        self.pdf_docs = pdf_docs
        self.used_blocks_B = set()  
        self.threshold = threshold
        
    @staticmethod
    def compare_block_with_others(args):
        block_A, flat_blocks_B, used_blocks_B, threshold = args
        match_val = 0
        best_block_num = None
        best_page = None
        switched_block = False

        for (page_num_B, block_num_B, text_B) in flat_blocks_B:
            # Skip this block if it has already been used
            if (page_num_B, block_num_B) in used_blocks_B:
                continue

            similarity = SequenceMatcher(None, block_A[-1].strip(), text_B.strip()).ratio()
            
            # Obvious matches
            if similarity > 0.995: 
                used_blocks_B.add((page_num_B, block_num_B))  # Add this block to the set of used blocks
                return (block_A[0], block_A[1]), (page_num_B, block_num_B), switched_block
                
            # Matching by maximum string similarity
            if similarity > match_val :
                match_val = similarity
                best_block_num = block_num_B
                best_page = page_num_B
        
        switched_block = True if (block_A[0], block_A[1]) != (best_page, best_block_num) else False
        
        if match_val > threshold and best_block_num is not None and best_page is not None:
            used_blocks_B.add((best_page, best_block_num))  # Add this block to the set of used blocks
            return (block_A[0], block_A[1]), (best_page, best_block_num), switched_block
        else:
            return (block_A[0], block_A[1]), None, switched_block

    def match_blocks(self, parallel=False, threshold=None):
        if threshold is None:
            threshold = self.threshold
        #sorted_docs = sorted(self.pdf_docs, key=lambda doc: len(doc.pages))
        #docA = sorted_docs[0]
        #docBs = sorted_docs[1:]

        docA = self.pdf_docs[0]
        docB = self.pdf_docs[1]
        
        #for docB in docBs:
        match = {}
        flat_blocks_A = [(page_num, block[5], block[4]) for page_num in range(len(docA.pages)) for block in docA.get_blocks_in_page(page_num)]
        flat_blocks_B = [(page_num, block[5], block[4]) for page_num in range(len(docB.pages)) for block in docB.get_blocks_in_page(page_num)]
        
        if parallel:
            with Pool(cpu_count()) as p:
                results = p.map(self.compare_block_with_others, [(block_A, flat_blocks_B, self.used_blocks_B, self.threshold) for block_A in flat_blocks_A])
        else:
            results = [self.compare_block_with_others((block_A, flat_blocks_B, self.used_blocks_B, self.threshold)) for block_A in flat_blocks_A]

        # Total matches
        match = {k:v for k,v,s in results}
        
        # Blocks that were switched
        switch_match = {k:v for k,v,s in results if s}
        
        # Blocks that were matched
        matched_A_set = set(k for k, v in match.items() if v is not None)
        matched_B_set = set(v for k, v in match.items() if v is not None)

        # Blocks that were not matched
        # blocks removed from docB or inserted in docA - assuming docs are temporal versions removed from A
        unmatched_B = {(page_num, i) for page_num in range(len(docB.pages)) for i in range(docB.get_num_blocks_page(page_num))} - matched_B_set
        # blocks removed from docA or inserted in docB - assuming docs are temporal versions inserted in B
        unmatched_A = {(page_num, i) for page_num in range(len(docA.pages)) for i in range(docA.get_num_blocks_page(page_num))} - matched_A_set

        return  match, switch_match, unmatched_A, unmatched_B

    def print_detected_blocks(self, match, switch_match):
        print(("-")*10)
        for block_A, block_B in match.items():
            if block_A in switch_match.keys(): print("switched")
            print(pdf_list[0].get_blocks_in_page(*block_A)[4])
            if block_B is None: print('No block_B match - probably removed')
            else: print(pdf_list[1].get_blocks_in_page(*block_B)[4])
            print(("-")*10)
            print('\n')
            
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare blocks in PDFs")
    parser.add_argument('-m', '--menu', action='store_true', help='Stop for console acess')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print the match result')
    parser.add_argument('-p', '--parallel', action='store_true', help='Execute the code with parallel processing')
    parser.add_argument('files', metavar='file', type=str, nargs='+', help='the PDF files to compare')
    parser.add_argument('-t', '--threshold', type=float, default=0.6, help='Set the threshold for block comparison')
    args = parser.parse_args()

    print('Selected files:', args.files)
    
    pdf_list = [PdfDoc(file_name) for file_name in args.files]
    
    match_blocks = MatchBlocks(pdf_list, args.threshold)
    match, switch_match, unmatched_A, unmatched_B = match_blocks.match_blocks(parallel=args.parallel)
    
    if args.verbose: 
        match_blocks.print_detected_blocks(match, switch_match)
    
    if args.menu:
        breakpoint()

