"""Розробити програму, яка: 
а) створює текстовий файл TF2_1 із символьних рядків різної довжини; 
б) читає вміст файла TF2_1, знаходить всі послідовності  цифр, довжиною більше двох і записує  їх у файл TF2_2 в один рядок через пробіл; 
в) читає вміст файла TF2_2 і виводить його на екран."""


def open_file(file_name: str, action: str):
	try:
		file = open(file_name, action)
	except:
		print("File", file_name, "wasn't opened!")
		return None
	else:
		print("File", file_name, "was opened!")
		return file


file_1 = "TF2_1"
file_2 = "TF2_2"
file1_w = open_file(file_1, "w")
if file1_w != None:  
	file1_w.write("Today is 13 of March the year is 2024, lesson 9 try 123 ")
	file1_w.close()

file_2_r = open_file(file_1, "r")
file_2_w = open_file(file_2, "w")
if file_2_r != None:
	word = ""
	for block in file_2_r.read().split(","):
		for word in block.split(" "):
			if word.isnumeric() and len(word) > 1:
				file_2_w.write(word + " ")
	file_2_r.close()
	file_2_w.close()

file_2_r = open_file(file_2, "r")
if file_2_r != None:
	print(file_2_r.read())
	file_2_r.close()
