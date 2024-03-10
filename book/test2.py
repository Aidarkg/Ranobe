import os
import ebooklib
from ebooklib import epub

def extract_epub_content(epub_file_path):
    book = epub.read_epub(epub_file_path)
    content = ''
    a = 0
    for item in book.get_items():
        a += 1
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = item.get_body_content().decode('utf-8')  # Преобразование содержимого в строку
        title = item.get_name()
        print(title)
        if a == 50:
            break
    return title

epub_file_path = 'ranobe/dobro_pojalovat_v_klass_prevoshodstva.epub'
content = extract_epub_content(epub_file_path)
# print(content)
# ranobe/dobro_pojalovat_v_klass_prevoshodstva.epub