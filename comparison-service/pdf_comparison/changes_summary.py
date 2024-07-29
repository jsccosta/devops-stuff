from pdf_doc import PdfDoc


class ChangesSummary:
    def __init__(self, pdf_docs: list, changes):
        self.pdf_docs = pdf_docs
        self.changes = changes


    def write_changes(self):
        # Iterates through each change and writes the corresponding description into a text file.
        for change_type, changes in self.changes.items():
            for change in changes:
                if change_type == 'insert':
                    change_dets = f'The following text has been inserted on page {change["match_tuple"][2]}: {change["text_B"]}.'
                    self.write_details(change_dets= change_dets)

                elif change_type == 'delete':
                    change_dets = f'The following text has been deleted on page {change["match_tuple"][0]}: {change["text_A"]}.'
                    self.write_details(change_dets= change_dets)

                elif change_type == 'replace':
                    change_dets = f'The text on page {change["match_tuple"][0]}: {change["text_A"]}, has been replaced with the following text: {change["text_B"]}.'
                    self.write_details(change_dets= change_dets)

    def write_details(self, change_dets):
        # Opens a new text file and writes the details of the change.
        with open("changes_summary.txt", "a") as f:
            f.write(change_dets)
            f.write('\n')
            print(f'Written: {change_dets}')
            f.close()
