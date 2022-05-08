from translate import Translator

user_input = input("Enter a word/sentence to translate: ")
user_lang = input("Enter a language (tr, ar, ect.): ")

translator = Translator(to_lang=user_lang)
translation = translator.translate(user_input)
print(translation)
