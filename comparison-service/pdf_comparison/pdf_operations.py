# file imports
from match_blocks import MatchBlocks
from pdf_modifier import PdfModifier
from changes_summary import ChangesSummary
from pdf_doc import PdfDoc

# python imports
from difflib import SequenceMatcher
import argparse
import json


class PdfOperations:
    def __init__(self, file_names):
        # Input: file_names, a list of strings representing file paths
        # Initializes the PdfOperations object with a list of PdfDoc objects
        if not isinstance(file_names, list):
            raise ValueError("file_names must be a list of strings representing file paths")

        self.pdf_docs = [PdfDoc(file_name) for file_name in file_names]
        self.result = MatchBlocks(self.pdf_docs, threshold=0.4).match_blocks(parallel=True)
        self.replacements = self.compare_files()
        self.replacements_json = self.export_replacements_json()

    @staticmethod
    def combine_coordinates(coords_list):
        # Input: coords_list, a list of coordinates
        # Returns: A tuple representing the combined coordinates
        # If the list is empty, returns None
        if not coords_list:
            return None
        x0 = min(coord[0] for coord in coords_list)
        y0 = min(coord[1] for coord in coords_list)
        x1 = max(coord[2] for coord in coords_list)
        y1 = max(coord[3] for coord in coords_list)
        return (x0, y0, x1, y1)

    @staticmethod
    def get_coordinates(words_info, block_num, start_index, end_index):
        # Input: words_info, a list of word information
        #        block_num, the block number
        #        start_index and end_index, the start and end indices for the words
        # Returns: A list of coordinates for the words in the specified block and index range
        return [word[:4] for word in words_info if word[5] == block_num and start_index <= word[7] < end_index]

    def find_replacements(self, info_A, info_B):
        page_num_A = info_A[0]
        page_num_B = info_B[0]
        block_num_A = info_A[1]
        block_num_B = info_B[1]

        switched = True if (page_num_A, block_num_A) != (page_num_B, block_num_B) else False

        text_A = self.pdf_docs[0].get_blocks_in_page(*info_A)[4].strip()
        text_B = self.pdf_docs[1].get_blocks_in_page(*info_B)[4].strip()

        words_info_A = self.pdf_docs[0].get_words_in_page(page_num_A)
        words_info_B = self.pdf_docs[1].get_words_in_page(page_num_B)

        s = SequenceMatcher(None, text_A.split(), text_B.split())
        grouped_opcodes = s.get_grouped_opcodes(n=3)

        replacements_in_block = []

        for group in grouped_opcodes:
            for tag, i1, i2, j1, j2 in group:
                if tag == 'equal':
                    continue

                coordinates_A = self.get_coordinates(words_info_A, block_num_A, i1, i2) if tag != 'insert' else None
                coordinates_B = self.get_coordinates(words_info_B, block_num_B, j1, j2) if tag != 'delete' else None

                replacement = {
                    'tag': tag,
                    'match_tuple' : (page_num_A, block_num_A, page_num_B, block_num_B),
                    'text_A': ' '.join(text_A.split()[i1:i2]) if tag != 'insert' else '',
                    'text_B': ' '.join(text_B.split()[j1:j2]) if tag != 'delete' else '',
                    'coordinates_A': self.combine_coordinates(coordinates_A) if coordinates_A else '',
                    'coordinates_B': self.combine_coordinates(coordinates_B) if coordinates_B else '',
                    'switched' : switched
                }

                replacement = {k: v for k, v in replacement.items() if v != ''}

                replacements_in_block.append(replacement)

        return replacements_in_block

    def compare_files(self):
        replacements = {'insert': [], 'delete': [], 'replace': []}

        for info_A, info_B in self.result[0].items():
            if info_B != None:
                replacements_in_block = self.find_replacements(info_A, info_B)
                if replacements_in_block:
                    for replacement in replacements_in_block:
                        replacements[replacement['tag']].append(replacement)
        return replacements

    def export_replacements_json(self):
        return json.dumps(self.replacements, indent=4)

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Compare blocks in PDFs")

    # Add the arguments
    parser.add_argument('-c', '--changes', action='store_true', help='Print the match result')
    parser.add_argument('files', metavar='file', type=str, nargs='+', help='the PDF files to compare')

    # Parse the arguments
    args = parser.parse_args()

    # Ensure there are at least two files to compare
    if len(args.files) < 2:
        parser.error("You must provide at least two PDF files to compare.")

    print('Selected files:', args.files)

    # Initialize PdfOperations with file names
    operations = PdfOperations(args.files)

    # Perform comparison and get changes
    changes = operations.compare_files()

    # Create PdfDoc objects for each file
    pdf_docs = [PdfDoc(file) for file in args.files]

    # Initialize PdfModifier with PdfDoc objects and changes
    modifier = PdfModifier(pdf_docs, changes)

    # Apply changes to highlight differences
    modifier.apply_changes()

    # Save altered files with a new name indicating they have been modified
    output_files = [item.replace(".pdf", "_altered.pdf") for item in args.files]

    modifier.save_altered_files(output_files[0], output_files[1])

    print(f"Modified files have been saved as: {output_files}")

    # Write up summary of changes
    summary = ChangesSummary(pdf_docs, changes)
    summary.write_changes()
