#Дано одномірний масив, що складається з N дійсних елементів. Масив користувач має ввести з клавіатури. Знайти максимальний елемент.
numbers = []


def input_numbers():
	n = int(input("Введіть довжину масиву: "))
	for i in range(n):
		numbers.append(int(input(f"Елемент {i + 1}: ")))


input_numbers()
print("Найбільше число масиву: ", max(numbers))
