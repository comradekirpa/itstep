sentence = input("Введите нужный текст")
print(". ".join(i.capitalize() for i in sentence.split(". ")))
