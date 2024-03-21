import csv
import numpy as np
import matplotlib.pyplot as plt
import sys

file_name = "population.csv"


def get_country_data(country="Ukraine", year_range=range(2000, 2016), file_name="population.csv"):
	try:
		reader = csv.DictReader(open(file_name))
		x = []
		y = []
		for row in reader:
			if row["Country Name"] == country and row["Series Name"] == "Population, total":
				for year in year_range:
					x.append(year)
					y.append(row[f'{year} [YR{year}]'])
		y = [int(element) for element in y]
		if not x:
			print("No data for this country name")
		return x, y
	except Exception as err:
		print(err)


def print_column_grafik(x3, y3, label3):
	y_pos = np.arange(len(x3))
	plt.bar(y_pos, y3, align='center', alpha=0.5, label=label3)
	plt.xticks(y_pos, x3, rotation=45)
	plt.ylabel("Quantity")
	plt.title("Population ages 2000-2016")
	plt.legend()
	plt.show()


def print_grafik(x, y1, y2, label1, label2):
	if not y2:
		print("The country has no information and cant be compared")
		return
	np.array(x)
	np.array(y1)
	np.array(y2)
	plt.plot(x, y1, linestyle='-', color='blue', linewidth=2, label=label1)
	plt.plot(x, y2, linestyle='-', color='red', linewidth=2, label=label2)
	plt.title("Population ages 2000-2016", fontsize=16)
	plt.xlabel("Year")
	plt.ylabel("Quantity")
	plt.legend()
	plt.grid(True)
	plt.show()


country1 = "Ukraine"
country2 = input("Enter Country Name: ")
x1, y1 = get_country_data(country1)
x2, y2 = get_country_data(country2)
print_grafik(x1, y1, y2, country1, country2)
country3 = input("Enter Country Name: ")
x3, y3 = get_country_data(country3)
print_column_grafik(x3, y3, country3)
