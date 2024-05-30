# Задано прізвища всіх n=10 співробітників фірми та їх адреси.
# Скласти програму, яка визначає, чи працюють у фірмі люди з прізвищем: Кузін, Куравльов, Кудін, Кульков або Кубиків.
# У разі позитивної відповіді надрукувати їх адреси.

company = [
    {"lastname": "Кузін", "address": "вул. Кайбушева 3"},
    {"lastname": "Шевченко", "address": "пр. Свободи 21 "},
    {"lastname": "Фінхе", "address": "вул. Січових стрільців 8"},
    {"lastname": "Кубиків", "address": "вул. Сарантики 10"},
    {"lastname": "Коваль", "address": "вул. Оболонська 67"},
    {"lastname": "Зінченко", "address": "вул. Правди 89"},
    {"lastname": "Рональду", "address": "вул. Франка 69"},
    {"lastname": "Мосійчук", "address": "вул. Антуана Сірого 16"},
    {"lastname": "Зеленський", "address": "Офіс президента"},
    {"lastname": "Шольц", "address": "вул. Берлінська 12"}
]

def search_worker(lastname):
    for worker in company:
        if worker["lastname"] == lastname:
            print(worker.get("lastname"), "-", worker.get("address"))
            print(worker.get("salary", "Заробітна плата засекречена"))
            return
    print(f'Працівник з прізвищем {lastname} не працює в компанії')
    print(worker.get("salary", "Не може мати заробітну плату, бо не працює в компанії"))

def write_dict(company):
    for worker in company:
        print("------------------------")
        for key, value in worker.items():
            print(f"{key}: {value}")

def add_employee(lastname, address):
    company.append({"lastname": lastname, "address": address})
    print(f"\nНовий співробітник {lastname} доданий успішно. \n")

def remove_employee(lastname):
    for worker in company:
        if worker["lastname"] == lastname:
            company.remove(worker)
            print(f"Співробітник {lastname} видалений успішно.")
            return
    print(f"Співробітник {lastname} не знайдений в компанії.")

def sort_by_lastname(company):
    return sorted(company, key=lambda worker: worker["lastname"])

# Меню
def menu():
    while True:
        print("\nМеню:")
        print("1. Виведення на екран всіх значень словника")
        print("2. Додавання нового запису до словника")
        print("3. Видалення запису зі словника")
        print("4. Перегляд вмісту словника за відсортованими ключами")
        print("5. Пошук працівників за прізвищами (Кузін, Куравльов, Кудін, Кульков, Кубиків)")
        print("6. Вихід")
        choice = input("Виберіть опцію (1-6): ")

        if choice == '1':
            write_dict(company)
        elif choice == '2':
            lastname = input("Введіть прізвище: ")
            address = input("Введіть адресу: ")
            add_employee(lastname, address)
        elif choice == '3':
            lastname = input("Введіть прізвище для видалення: ")
            remove_employee(lastname)
        elif choice == '4':
            sorted_company = sort_by_lastname(company)
            write_dict(sorted_company)
        elif choice == '5':
            for lastname in ["Кузін", "Куравльов", "Кудін", "Кульков", "Кубиків"]:
                search_worker(lastname)
        elif choice == '6':
            print("Вихід із програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Запуск меню
menu()
