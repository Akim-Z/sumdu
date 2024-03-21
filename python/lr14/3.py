import json
import numpy as np
import matplotlib.pyplot as plt

company = [
	{"lastname": "Кузін", "address": "вул. Кайбушева 3", "position": "Chief"},
	{"lastname": "Гевченко", "address": "пр. Свободи 21 ", "position": "Business Analyst"},
	{"lastname": "Фінхе", "address": "вул. Січових стрільців 8", "position": "Manager"},
	{"lastname": "Субиків", "address": "вул. Сарантики 10", "position": "Manager"},
	{"lastname": "Поваль", "address": "вул. Оболонська 67", "position": "Bookkeeper"},
	{"lastname": "Зінченко", "address": "вул. Правди 89", "position": "Bookkeeper"},
	{"lastname": "Рональду", "address": "вул. Франка 69", "position": "Manager"},
	{"lastname": "Мосійчук", "address": "вул. Антуана Сірого 16", "position": "Business Analyst"},
	{"lastname": "Зеленський", "address": "Офіс президента", "position": "Business Analyst"},
	{"lastname": "Шольц", "address": "вул. Берлінська 12", "position": "Manager"}
]

jsonData = json.dumps(company)

with open("data.json", "wt") as file:
    file.write(jsonData)


def print_pie_grafik():
	with open("data.json", "rt") as file:
		company = json.loads(jsonData)
		my_dict = {}
		for worker in company:
			position = worker["position"]
			if position in my_dict:
				my_dict[position] += 1
			else:
				my_dict[position] = 1
		labels = my_dict.keys()
		sizes = my_dict.values()
		fig, ax = plt.subplots()
		ax.pie(sizes, labels=labels, autopct='%1.1f%%')
		plt.show()


print_pie_grafik()
