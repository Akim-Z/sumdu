"""виведення на екран всіх значень словника;
додавання (видалення) нового запису до (зі) словника;
перегляд вмісту словника за відсортованими ключами (перетворити об‘єкт подання ключів в список
або скористатися функцією sorted, застосувавши її до словника, або об‘єкту, який повертає метод keys)
розв’язання завдань відповідно до варіанту."""

#Задано прізвища всіх n=10 співробітників фірми та їх адреси. 
#Скласти програму, яка визначає, чи працюють у фірмі люди з прізвищем: Кузін, Куравльов, Кудін, Кульков або Кубиків.
#У разі позитивної відповіді надрукувати їх адреси.

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
            print(worker.get("lastname"),"-", worker.get("address"))
            print(worker.get("salary", "Заробітна плата засекречена"))
            return
    print(f'Працівник з прізвищем {lastname} не працює в компанії')
    print(worker.get("salary", "Не може мати заробітну плату, бо не працює в компанії"))


search_worker("Кузін")
search_worker("Куравльов")
search_worker("Кудін")
search_worker("Кульков")
search_worker("Кубиків")


def write_dict(company):
    for worker in company:
        print("------------------------")
        for key, value in worker.items():
            print(f"{key}: {value}")


write_dict(company)


def add_employee(lastname, address):
	company.append({"lastname": lastname, "address": address})
	print(f"\nНовий співробітник {lastname} доданий успішно. \n")


add_employee("Коршунков","вул. Гоміса 12")


def remove_employee(lastname):
	for worker in company:
		if worker["lastname"] == lastname:
			company.remove(worker)
			print(f"Співробітник {lastname} видалений успішно.")
			return
	print(f"Співробітник {lastname} не знайдений в компанії.")


remove_employee("Шевченко")
remove_employee("Ручко")


write_dict(company)
