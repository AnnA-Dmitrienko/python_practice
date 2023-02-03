from translate import Translator
translator = Translator(to_lang="ru")

try:
    with open('sad.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
    with open('test-ru.txt', mode='w') as my_file2:
        my_file2.write(translation)
except FileNotFoundError as err:
    print("check your file path!")
