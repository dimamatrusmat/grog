# import random
# import math
#
#
# def get_number():
#     need = round(random.random() * 100)
#
#     return need
#
#
# def say_number(num, need):
#     if need > num:
#         return 1
#     elif need < num:
#         return 0
#     else:
#         return 'Ура!'
#
#
# if __name__ == "__main__":
#     need = get_number()
#     max = 100
#     num = max / 2
#
#     ost = 50
#
#     while True:
#         ans = say_number(num, need)
#
#         ost = math.ceil(ost / 2)
#
#         if ans == 1:
#             num = num + ost
#         elif ans == 0:
#             num = num - ost
#         else:
#             break
#         print(num)
#
#     print(need)


name = [100, 240]

width = name[0]
height = name[1]


def square(name):
    if (name[0] > name[1]):
        max = name[0]
        min = name[1]
    else:
        max = name[1]
        min = name[0]

    if (max % min) == 0:
        return name

    else:
        ever = max // min
        r = max - ever * min
        new_square = [min, r]

        if max > 20:
            square(new_square)
        else:
            return min


print(square(name))
