#Вставка нового елемента в список перед вказаним елементом.


def list_operation() -> list:

	my_list = []
	print("Якщо Ви бажаєте зикінчити ввод елементів - введіть '000' ")

	while True:
		element = int(input("Ведіть елемент: "))
		if element == 000:
			break
		my_list.append(element)
		
	print(f'Ваш список: {my_list}')	
	index = int(input("Введіть номер елемента, перед яким Ви хочете додати новий елемент: "))
	new_element = int(input("Введіть елемент, який Ви хочете вставити: "))
	my_list.insert(index - 1, new_element)
	print(f'Ваш змінений список: {my_list}')


list_operation()
