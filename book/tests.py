from ebooklib import epub
import ebooklib


book = epub.read_epub('ranobe/chernoknijnik_v_mire_magov.epub')


def read_epub(epub_file_path):
    book = epub.read_epub(epub_file_path)
    
    # Получаем метаданные книги
    # title = book.get_metadata('DC', 'title')[0][0]
    # genre = book.get_metadata('DC', 'genre')
    # print(title)
    # print(genre)
    # print("Author:", book.get_metadata("DC", "creator"))
    # description = book.get_metadata("DC", "description")
    # description = description[0][0]
    # print(description)
    # print(type(description))
    # print("Publisher:", book.get_metadata("DC", "publisher"))
    # metadata_keys = book.metadata.keys()
    # print("Available metadata keys:", metadata_keys)

    # a = 0
    # for item in book.get_items():
    #     a += 1
    #     if item.get_type() == ebooklib.ITEM_DOCUMENT:
    #         print("Content of:", item.get_name())
    #         content = item.get_content()
    #     if a == 50:
    #         break
    #         print(content.decode('utf-8'))  # Декодируем содержимое в UTF-8
    images = book.get_items_of_type(ebooklib.ITEM_IMAGE)
    print(images)
    # for item in book.get_items():
    #     if item.get_type() == ebooklib.ITEM_DOCUMENT and item.get_name() == "CoverPage.html":
    #         print("Content of CoverPage.html:")
    #         content = item.get_content()

    #         print(content.decode('utf-8'))  # Декодируем содержимое в UTF-8
    #         break

# Content of: CoverPage.html
# Content of: Header.html

# Укажите путь к файлу EPUB
epub_file_path = 'ranobe/chernoknijnik_v_mire_magov.epub'

# Вызываем функцию чтения
read_epub(epub_file_path)
