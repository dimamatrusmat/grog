import random 
import math


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
	max = 100
	num = max/2

	ost = 50

	while True:
		ans = say_number(num, need)
		
		ost = math.ceil(ost/2)
		
		if ans == 1:
			num = num + ost
		elif ans == 0:
			num = num - ost
		else:
			break
		print(num)
			

	print(need)