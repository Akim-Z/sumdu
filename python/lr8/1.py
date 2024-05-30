# Імпорт необхідних бібліотек
import json

# Створення словника для зберігання інформації про успішність студентів
students_data = {
    "group_number": "КНд-21с",
    "students": []
}

# Функція для додавання студента до словника
def add_student(group_number, last_name, first_name, patronymic, age, nmt_average_grade, course, subjects):
    student = {
        "last_name": last_name,
        "first_name": first_name,
        "patronymic": patronymic,
        "age": age,
        "nmt_average_grade": nmt_average_grade,
        "course": course,
        "subjects": subjects
    }
    students_data["group_number"] = group_number
    students_data["students"].append(student)

# Функція для розрахунку середнього балу студенту по предметам     
def calculate_average_grade(student):
    grades = student["subjects"].values()
    if grades:
        average = sum(grades) / len(grades)
        return average
    return 0


# Приклад використання функції додавання студента
add_student(
    group_number="КНд-21с",
    last_name="Ivanov",
    first_name="Ivan",
    patronymic="Ivanovich",
    age=20,
    nmt_average_grade=190,
    course=3,
    subjects={
        "Math": 90,
        "Physics": 85,
        "Chemistry": 92
    }
)

add_student(
    group_number="КНд-21с",
    last_name="Petrov",
    first_name="Petr",
    patronymic="Petrovich",
    age=19,
    nmt_average_grade=180,
    course=2,
    subjects={
        "Math": 80,
        "Physics": 88,
        "Chemistry": 91
    }
)

# Виведення словника
print(json.dumps(students_data, indent=4, ensure_ascii=False))

# Виведення середнього балу для кожного студента
print("\nСередній бал кожного студента:")
for student in students_data["students"]:
    average_grade = calculate_average_grade(student)
    print(f"{student['last_name']} {student['first_name']} {student['patronymic']}: {average_grade:.2f}")


# Завдання для другого студента: розробити функцію видалення даних у словнику
