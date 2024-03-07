from ebooklib import epub
import ebooklib


book = epub.read_epub('ranobe/chernoknijnik_v_mire_magov.epub')


def read_epub(epub_file_path):
    book = epub.read_epub(epub_file_path)
    
    # Получаем метаданные книги
    # print("Title:", book.get_metadata("DC", "title"))
    # print("Author:", book.get_metadata("DC", "creator"))
    
    a = 0
    for item in book.get_items():
        a += 1
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            print("Content of:", item.get_name())
            # content = item.get_content()
        # if a == 50:
        #     break
            # print(content.decode('utf-8'))  # Декодируем содержимое в UTF-8

    # for item in book.get_items():
    #     if item.get_type() == ebooklib.ITEM_DOCUMENT and item.get_name() == "Chapter1.html":
    #         print("Content of Chapter1.html:")
    #         content = item.get_content()

    #         print(content.decode('utf-8'))  # Декодируем содержимое в UTF-8
    #         break

# Укажите путь к файлу EPUB
epub_file_path = 'D:/PycharmProjects/WEB дизайн/ranobe/avidreaders.ru__mat-uchenya.epub'

# Вызываем функцию чтения
read_epub(epub_file_path)
