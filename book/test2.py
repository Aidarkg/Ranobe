from ebooklib import epub
import ebooklib
import os

def save_all_chapters(epub_file_path, output_folder):
    book = epub.read_epub(epub_file_path)
    
    # Создаем папку для сохранения файлов, если она не существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Поиск и сохранение содержимого всех глав
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT and item.get_name().startswith("Chapter"):
            chapter_name = item.get_name()
            print("Saving content of {}...".format(chapter_name))
            content = item.get_content()
            output_file_path = os.path.join(output_folder, chapter_name)
            
            # Декодируем содержимое в UTF-8 и сохраняем в файл
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(content.decode('utf-8'))
            print("Content of {} saved to: {}".format(chapter_name, output_file_path))

# Укажите путь к файлу EPUB
epub_file_path = "ranobe/chernoknijnik_v_mire_magov.epub"

# Укажите папку для сохранения содержимого глав
output_folder = "D:/PycharmProjects/WEB дизайн/Чернокнижник/chapter1_content.html"

# Вызываем функцию сохранения содержимого всех глав в файлы
save_all_chapters(epub_file_path, output_folder)




# Укажите путь для сохранения содержимого главы в файл
# output_file_path = "D:/PycharmProjects/WEB дизайн/Чернокнижник/chapter1_content.html"

