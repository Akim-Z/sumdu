# Створення текстового файлу та запис даних
filename = "questions_and_answers.txt"

try:
    # Відкриття файлу у режимі запису
    with open(filename, 'w', encoding='utf-8') as file:
        # Запис прізвища та питання
        file.write("Прізвище: Здоровоцов Акім\n")
        file.write("Питання: Як реалізувати функцію, яка обчислює інтеграл в Python (з використанням бібліотеки scipy)?\n")
    print(f"Дані успішно записані у файл {filename}")
except IOError as e:
    print(f"Помилка роботи з файлом: {e}")
