import csv
import json
import os

# Дані для запису в .csv файл
data = [
    ["name", "age", "city"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

# Назва .csv файлу
csv_filename = "students.csv"
json_filename = "students.json"

# Створення .csv файлу
def create_csv_file(filename, data):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Дані успішно записані у файл {filename}")
    except IOError as e:
        print(f"Помилка роботи з файлом: {e}")

# Конвертація .csv у .json
def convert_csv_to_json(csv_filename, json_filename):
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data_list = list(csv_reader)

        with open(json_filename, mode='w', encoding='utf-8') as file:
            json.dump(data_list, file, indent=4)
        print(f"Дані успішно конвертовані у файл {json_filename}")
    except IOError as e:
        print(f"Помилка роботи з файлом: {e}")
    except Exception as e:
        print(f"Інша помилка: {e}")

# Виконання функцій
create_csv_file(csv_filename, data)
convert_csv_to_json(csv_filename, json_filename)
