import random 

def get_number():
	need = round(random.random() * 100)

	return need

def say_number(num, need):
	if need > num:
		return 1
	elif need < num:
		return 0
	else:
		return 'Ура!'



if __name__ == "__main__":
	need = get_number()
	num = round(max / 2)
	max = 100
	min = 0
	

	while True:
		ans = say_number(num, need)

		if ans == 1:
			num = num + round(num/2)
		elif ans == 0:
			num = num - round(num/2)
		else:
			break

		print(num)
			

	print(need)