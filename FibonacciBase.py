#  File: FibonacciBase.py

#  Description: inputs a decimal number and outputs the fibonacci binary representation of that number

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 05/02

#  Date Last Modified: 05/02

def fib(n):

	a,b = 0,1

	list_fib = []

	while a<n:

		list_fib.append(a)

		a, b = b, (a+b)

	if a == n:

		list_fib.append(a)

	return list_fib

def main():

	num = eval(input('Enter a number: '))

	list_fib = fib(num)

	list_fib.reverse()

	list_bin = [1]

	prod = list_fib[0]*list_bin[0]

	for i in range(1,len(list_fib)-2):

		if len(list_fib) != len(list_bin):

			if list_bin[i-1] == 1:

				list_bin.append(0)

			else: 

				if prod >= num:

					list_bin.append(0)

				else:

					if list_fib[i]+prod > num:

						list_bin.append(0)

					else:

						list_bin.append(1)

		prod += list_fib[i]*list_bin[i]

	st = ''

	for i in list_bin:

		st += str(i)

	print(str(num)+ ' = '+st+' (fib)')

main()

				







	