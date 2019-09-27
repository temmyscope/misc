import math

a = int(input('Enter the co-efficient of a \n'))
b = int(input('Enter the co-efficient of b \n'))
c = int(input('Enter the co-efficient of c \n'))

def quad(a, b, c):
	p = math.sqrt(b**2)
	q = 4 * a * c
	r = 2 * a
	x = (0-b +  (p-q) ) / r
	y = (0-b -  (p-q) ) / r
	#y = (0-b - math.sqrt((b**2) - (4 * a * c))) /(2 * a)
	return [ "The first value of x is " + str(x), "The second value of x is "+ str(y)]

ls = quad(a , b , c)

print(ls[0])
print(ls[1])