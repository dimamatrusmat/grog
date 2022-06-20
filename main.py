import random 

def get_number():
	need = round(random.random() * 100)

	return need

def say_number(num, need):
	if need > num:
		return 'больше'
	elif need < num:
		return 'меньше'
	else:
		return 'Ура!'



if __name__ == "__main__":
	need = get_number()
	max = 100
	min = 0

	while True:
		num = input('Введите число: \n')
		num = int(num)
		ans = say_number(num, need)

		print(ans)
		if ans == 'Ура!':
			break
			

	print(need)