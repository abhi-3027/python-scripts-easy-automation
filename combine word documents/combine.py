from docx import Document

files = ['LL.docx', 'doc2.docx']  #put the name of all the files that you want to merge 

def combine_word_documents(files):
    merged_document = Document()

    for index, file in enumerate(files):
        sub_doc = Document(file)

        # Don't add a page break if you've reached the last file.
        if index < len(files)-1:
           sub_doc.add_page_break()

        for element in sub_doc.element.body:
            merged_document.element.body.append(element)

    merged_document.save('merged.docx')

combine_word_documents(files)