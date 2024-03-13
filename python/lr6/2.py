import random

my_list = []
list_leng = random.randint(5, 20)

for i in range(list_leng):
	x = random.randint(0, 20)
	my_list.append(x)


def search(num: int) -> str:
	if num in my_list:
		print(f'{my_list} \n Число {num} наявне в даному масиві')
	else:
		print(f'{my_list} \n Число {num} відсутнє в даному масиві')		
	

num = int(input("Введіть число яке ви бажаєте перевірити в масиві: "))
search(num)		
