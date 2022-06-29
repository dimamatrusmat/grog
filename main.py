def sum(square):

    if (square[0] > square[1]):
        max, min = square[0], square[1]
    else:
        min, max = square[0], square[1]

    if (max % min == 0):
        return [min, min]
    else:
        e = max // min
        o = max - min * e
        return sum([min, o])

print(sum([15, 130]))
