#Задано речення. Скласти програму, яка визначає і виводить на екран всі його слова, відмінні від слова «привіт».
greeting = "Привіт , Василю , можеш привітатися зі мною"

# Розділення рядка на список слів
my_list = greeting.split(" ")
# Заміна ком у кожному слові на порожній рядок
my_list = [word.replace(',', '') for word in my_list]

# Виведення кожного слова списку, крім "Привіт"
for word in my_list:
    if word != "Привіт" and word != "":
        print(word, end= " ")
