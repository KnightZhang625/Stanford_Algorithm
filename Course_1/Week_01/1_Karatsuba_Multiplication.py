from functools import lru_cache

def split_number(number):
	length = len(number)
	if length % 2 == 0:
		index = int(length // 2)
	else:
		index = int(length // 2 + 1)
	return int(number[: index]), int(number[index :])

@lru_cache()
def multiply(x, y):
	x = str(x)
	y = str(y)

	# for numbers with different lengths
	padding = 0
	if len(x) != len(y):
		padding = len(x) - len(y)
		if padding < 0:
			x += '0' * abs(padding)
		else:
			y += '0' * padding

	if len(x) == 1 or len(y) == 1:
		return int(x) * int(y)

	a, b = split_number(x)
	c, d = split_number(y)

	ac = multiply(a, c)
	bd = multiply(b, d)
	adbc = multiply(a+b, c+d) - ac - bd

	string = str(a) + str(b)
	if len(string) % 2 == 0:
		n = len(string)
	else:
		n = len(string) - 1

	ac = int(str(ac) + '0' * n)
	adbc = int(str(adbc) + '0' * (n // 2))
	divide = int('1' + '0' * abs(padding))

	return int((ac + adbc + int(bd)) / divide)

print(multiply(12345678, 987654321))





