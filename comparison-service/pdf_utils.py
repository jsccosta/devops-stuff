import fitz
import hashlib
import difflib
import os

# This function will highlight the blocks and underline the words summarized in the dictionary results
def comparison_writer(pdf_index: str, file_path, results, upload_folder=str):  
    
    filename = os.path.splitext(os.path.basename(file_path))[0]
    
    if pdf_index == '1': 
        result_str = '-'
        output_path = upload_folder+'/'+filename+'_previous.pdf'
    elif pdf_index == '2': 
        result_str = '+'
        output_path = upload_folder+'/'+filename+'_current.pdf'

    doc = fitz.open(file_path)
    n_pages = len(doc)

    total_blocks = 0  # keep track of total blocks processed so far

    for page_number in range(n_pages):
        page = doc[page_number]
        blocks = page.get_text("blocks")
        word_dict = page.get_text("words")

        n_words = 0  # reset the word count for each new page

        for block_id, block in enumerate(blocks):
            global_block_id = total_blocks + block_id  # calculate the global block id

            if global_block_id in results.keys():
                # Highlighting paragraphs where are changes
                block_coordinates = block[:4]
                block_rectangle = fitz.Rect(block_coordinates)
                highlight = page.add_highlight_annot(block_rectangle)
                highlight.set_colors(stroke=(0,0,1))
                highlight.update(opacity=0.1)

                for word in results[global_block_id][result_str]:
                    # in case only word changes
                    if type(word[1]) == int: 
                        add_underline_annotation(page, word_dict, [word[1]], n_words)
                    # in case several words in a row change    
                    else: 
                        add_underline_annotation(page, word_dict, word[1], n_words)


            n_words += len(block[4].split())
        total_blocks += len(blocks)  # update the total blocks processed so far

        # # Save the modified PDF
        doc.save(output_path, garbage=4, deflate=True, clean=True)

    return output_path


def text_extraction(file_paths):
    results = {}
    for file_path in file_paths:
        pdf_document = fitz.open(file_path)
        extracted_text = ""
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            text = page.get_text()
            extracted_text += text
        
        pdf_document.close()
        results[file_path] = extracted_text
    return results

# this functions takes only the text (no information about it) from the dictionary resulting from the previous
# function
def get_block_texts(text_dict):
    block_texts = []
    for page_number in text_dict:
        for block in text_dict[page_number]['blocks']:
            block_text = ''
            if block['lines']:
                for line in block['lines']:
                    for span in line['spans']:
                        block_text += span['text'] + ' '
            block_texts.append(block_text.strip())
    return block_texts


def get_text_dict(file_path:str):
    doc = fitz.open(file_path)
    text_dict = {}

    for i in range(len(doc)):
        page = doc[i]
        text_dict[i] = page.get_text('dict', sort=False)

    return text_dict

def string_to_md5(input_string):
    hasher = hashlib.md5()
    hasher.update(input_string.encode('utf-8'))
    return hasher.hexdigest()

def compare_paragraphs(s1, s2):
    words_s1 = s1.split()
    words_s2 = s2.split()

    d = difflib.Differ()
    diff = [word.strip() for word in list(d.compare(words_s1, words_s2))]

    result = {'-':[], '+':[]}

    result_1 = [element for element in diff if not element.startswith('+')]
    result_2 = [element for element in diff if not element.startswith('-')]

    changes_1 = []
    i = 0
    while i < len(result_1):
        if result_1[i].startswith('-'):
            words = [result_1[i].lstrip('- ')]
            indices = [i]
            i += 1
            while i < len(result_1) and result_1[i].startswith('-'):
                words.append(result_1[i].lstrip('- '))
                indices.append(i)
                i += 1
            indices = indices[0] if len(indices) == 1 else tuple(indices)
            changes_1.append((' '.join(words), indices))
        else:
            i += 1

    changes_2 = []
    i = 0
    while i < len(result_2):
        if result_2[i].startswith('+'):
            words = [result_2[i].lstrip('+ ')]
            indices = [i]
            i += 1
            while i < len(result_2) and result_2[i].startswith('+'):
                words.append(result_2[i].lstrip('+ '))
                indices.append(i)
                i += 1
            indices = indices[0] if len(indices) == 1 else tuple(indices)
            changes_2.append((' '.join(words), indices))
        else:
            i += 1

    result['-'] = changes_1
    result['+'] = changes_2
    
    return result

# This function is but a auxiliary function for readability 
def add_underline_annotation(page, word_dict, word_indices, n_words):
    first_word_index = word_indices[0] + n_words
    last_word_index = word_indices[-1] + n_words 
    word_rectangle = fitz.Rect(word_dict[first_word_index][:2]+
                                word_dict[last_word_index][2:4])

    underline = page.add_underline_annot(word_rectangle)
    underline.update()

def extract_differences(previous_doc, current_doc):
    results = {}
    # paragraph index
    block_idx = 0

    blocks_pdf1 = get_block_texts(get_text_dict(previous_doc))
    blocks_pdf2 = get_block_texts(get_text_dict(current_doc))

    for paragraph_1, paragraph_2 in zip(blocks_pdf1, blocks_pdf2):
    # similar paragraphs don't get compared
        if string_to_md5(paragraph_1) != string_to_md5(paragraph_2): 
            # creating a dictionary with all changes in the text
            results[block_idx] = compare_paragraphs(paragraph_1, paragraph_2)

    # incrementing paragraph index
    block_idx += 1

    return results