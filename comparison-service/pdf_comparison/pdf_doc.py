import pymupdf

class PdfDoc(pymupdf.Document):
    def __init__(self, pdf_path):
        super().__init__(pdf_path)
        self.pages = [page for page in self]
        
    def get_text_in_page(self, page_num):
        return self.pages[page_num].get_textpage()
    
    def get_blocks_in_page(self, page_num, block_num = None):
        if block_num is None:
            return self.pages[page_num].get_text("blocks", sort=True)

        else:
            return self.pages[page_num].get_text("blocks", sort=True)[block_num]

    def get_num_blocks_page(self, page_num):
        return len(self.pages[page_num].get_text("blocks", sort=True))
    
    def get_page(self, page_num):
        return self.text_pages[page_num]
    
    def get_words_in_page(self, page_num):
        words = self.pages[page_num].get_text("words", sort=True)
        return self.correct_line_numbers(words)
        
    def correct_line_numbers(self, words):
        previous_block_no = -1
        previous_y0 = -1
        previous_y1 = -1
        word_no = 0
        for index, word in enumerate(words):
            current_block_no, current_y0, current_y1 = word[5], word[1], word[3]
            if current_block_no == previous_block_no and current_y0 == previous_y0 and current_y1 == previous_y1:
                line_no = 0
                word_no += 1
            else:
                line_no = word[6]
                word_no = word[7]
            previous_block_no, previous_y0, previous_y1 = current_block_no, current_y0, current_y1
            words[index] = (*word[:6], line_no, word_no)
        return words
