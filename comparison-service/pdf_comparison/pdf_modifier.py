from pdf_doc import PdfDoc

class PdfModifier:
    def __init__(self, pdf_docs: list, changes):
        self.pdf_docs = pdf_docs
        self.changes = changes
        self.edit_sets = {
            "color_dic": {
                "light_blue" : (0, 1, 1),
                "ambar" : (1, 0.749, 0),
                "red" : (1,0,0),
                "green" : (0,1,0)
            },
            "color_func": {
                "switched" : "green",
                "delete" : "red",
                "insert" : "green",
                "replace" : "ambar"
            }
        }

    def highlight(self, change_type, change):
        tag = change_type
        color = self.edit_sets['color_dic'][self.edit_sets['color_func'][tag]]

        if tag == 'replace':
            coordinates_A = change['coordinates_A']
            coordinates_B = change['coordinates_B']

            page_num_A, block_num_A = change['match_tuple'][:2]
            self.highlight_text(self.pdf_docs[0], page_num_A, block_num_A, coordinates_A, color)

            page_num_B, block_num_B = change['match_tuple'][2:]
            self.highlight_text(self.pdf_docs[1], page_num_B, block_num_B, coordinates_B, color)
        else:
            doc_num = 0 if tag != 'insert' else 1
            page_num = change['match_tuple'][doc_num * 2]  # 0 or 2 depending on doc_A or doc_B
            block_num = change['match_tuple'][doc_num * 2 + 1]  # 1 or 3 depending on doc_A or doc_B
            word_bbox = change['coordinates_A'] if tag != 'insert' else change['coordinates_B']

            self.highlight_text(self.pdf_docs[doc_num], page_num, block_num, word_bbox, color)

    def highlight_text(self, pdf_doc, page_num, block_num, word_bbox, color):
        page = pdf_doc.pages[page_num]
        
        # Highlight the entire block with a light blue color
        block_bbox = pdf_doc.get_blocks_in_page(page_num)[block_num][:4]
        annot = page.add_highlight_annot(block_bbox)
        annot.set_colors(stroke=self.edit_sets['color_dic']['light_blue'])
        annot.set_opacity(0.15)
        annot.update()

        # Highlight the specific words based on the change type
        annot = page.add_rect_annot(word_bbox)
        annot.set_colors(stroke=color)
        annot.update()

    def apply_changes(self):
        # Triggers the changes in the PDFs
        for change_type, changes in self.changes.items():
            for change in changes:
                self.highlight(change_type, change)

    def save_altered_files(self, output_path_A, output_path_B):
        # Saves the altered pdfs to the specified file paths
        self.pdf_docs[0].save(output_path_A, garbage=4, deflate=True, clean=True)
        self.pdf_docs[1].save(output_path_B, garbage=4, deflate=True, clean=True)
