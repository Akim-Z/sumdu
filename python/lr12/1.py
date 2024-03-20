# Задано прізвища всіх n=10 співробітників фірми, їх адреси та посада. 
# Скласти програму, яка визначає, чи працюють у фірмі люди з прізвищем, яке починається на введену користувачем літеру. 
# У разі позитивної відповіді надрукувати їх адреси.
import json

company = [
	{"lastname": "Кузін", "address": "вул. Кайбушева 3", "position": "Chief"},
	{"lastname": "Гевченко", "address": "пр. Свободи 21 ", "position": "Business Analyst"},
	{"lastname": "Фінхе", "address": "вул. Січових стрільців 8", "position": "Project Manager"},
	{"lastname": "Субиків", "address": "вул. Сарантики 10", "position": "Manager"},
	{"lastname": "Поваль", "address": "вул. Оболонська 67", "position": "Bookkeeper"},
	{"lastname": "Зінченко", "address": "вул. Правди 89", "position": "Sales Representative"},
	{"lastname": "Рональду", "address": "вул. Франка 69", "position": "Human Resources Manager"},
	{"lastname": "Мосійчук", "address": "вул. Антуана Сірого 16", "position": "Marketing Specialist"},
	{"lastname": "Зеленський", "address": "Офіс президента", "position": "Customer service"},
	{"lastname": "Шольц", "address": "вул. Берлінська 12", "position": "Finance Manager"}
]

jsonData = json.dumps(company)

with open("data.json", "wt") as file:
    file.write(jsonData)
file.close()

while True:    
	print("Select an option:\n 1 - Add data\n 2 - View data\n 3 - Find a worker, whos lastname starts with letter: \n 4 - Exit") 
	i = input("Choose an option:\n") 
	i = int(i)
	if i == 1:
		with open("data.json", "at") as file:
			company = json.loads(jsonData)
			def add_employee(data):
				print("Add: ")
				lastname = input("lastname:")
				address = input("address:")
				position = input("position:")
				data.append({"lastname": lastname, "address": address, "position": position})
				return data
			company = add_employee(company)
			jsonData = json.dumps(company)
			with open("output.json", "wt") as file:
				file.write(jsonData)
			file.close()
		file.close()
	if i == 2:
		with open("data.json", "rt") as file:
			company = json.loads(jsonData)
			print(*company, sep='\n')
	if i == 3:
		with open("data.json", "rt") as file:
			company = json.loads(jsonData)
			letter = input("Enter letter: ")
			def search_worker(letter):
				for worker in company:
					if worker["lastname"].startswith(letter):
						print(worker.get("lastname"),"-", worker.get("address"))
					elif worker["lastname"].startswith(letter) == None:
						print(f'Працівник з прізвищем  на букву "{letter}" не працює в компанії')
			search_worker(letter)
	if i == 4:
		quit(0)
