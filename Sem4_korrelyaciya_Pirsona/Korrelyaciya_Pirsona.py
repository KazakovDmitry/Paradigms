from functools import reduce

def pirson(arr_X, arr_Y):
    avrX = reduce(lambda x, y: x + y, arr_X) / len(arr_X)
    # avrY = reduce(lambda x, y: x + y, arr_Y) / len(arr_Y)
    avrY = sum(arr_Y) / len(arr_Y) # альтернатива reduce
    xi_avrX = [x - avrX for x in arr_X]
    yi_avrY = [y - avrY for y in arr_Y]
    r_1 = reduce(lambda a, b: a + b, [x * y for x, y in zip(xi_avrX, yi_avrY)])
    print(xi_avrX, yi_avrY)
    print(r_1)
    r_2x = reduce(lambda a, b: a + b, [x ** 2 for x in xi_avrX]) ** 0.5
    r_2y = reduce(lambda a, b: a + b, [y ** 2 for y in yi_avrY]) ** 0.5
    print(r_2x, r_2y)
    r_2 = r_2x * r_2y
    r_xy = r_1 / r_2
    return r_xy


array_X = [2, 4, 6]
array_Y = [4, 8, 24]
print(pirson(array_X, array_Y))