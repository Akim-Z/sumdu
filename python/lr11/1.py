# Варіант 2. Знайти дані GDP per capita growth (annual %) для уcіх країн світу за 2019 рік. 
# Вивести вміст .csv файлу на екран. Організувати пошук даних для введених користувачем назв країн та записати результат пошуку у новий .csv файл.

import csv 

YEAR = "2019"
file_name = "gdp_data.csv"


def print_data(YEAR, file_name):
	try:
		reader = csv.DictReader(open(file_name))
		for row in reader:
			print(row.get("Country Name"), ":", (row.get(YEAR) or "No Data"))
	except:
		print("File", file_name, "wasn't opened!")
		return None		
				

def search_country_and_year(country, YEAR, file_name):
	reader = csv.DictReader(open(file_name))
	for row in reader:
		if row["Country Name"] == country and row[YEAR]:
			result = (row.get(YEAR) or "No Data")
			print(row.get("Country Name"), ":", result)
			with open("output.csv", "w", newline= "") as output:
				writer = csv.writer(output)
				writer.writerow(
					(
						country,
						result
					)
				)
			return


print_data(YEAR, file_name)
print("------------------------------")
country = input("Enter your country: ")
search_country_and_year(country, YEAR, file_name)
