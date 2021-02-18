#!/usr/bin/python3                          
'''
This exercise expands on the calculator, which was made in chapter 4, exercise 4. In this exercise, add sin() and cos() -calculations from the library module math to the calculator. Add these actions as selections 5 and 6, simultaneously moving the "change numbers" feature to 7 and "Quit" to 8. When the user calls either of the new features, the first number is the divident and second the divider like this: sin(number_1/number2). When correctly implemented, the program prints the following:




			
>>> 

Calculator
Give the first number: 1
Give the second number: 2
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 1 2
Please select something (1-6): 5
The result is: 0.479425538604203
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 1 2
Please select something (1-6): 6
The result is: 0.8775825618903728
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 1 2
Please select something (1-6): 8
Thank you!
>>> 

Example output:
Calculator
Give the first number: 6
Give the second number: 2
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 6 2
Please select something (1-6): 7
Give the first number: 8
Give the second number: 4
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 8 4
Please select something (1-6): 1
The result is: 12
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 8 4
Please select something (1-6): 4
The result is: 2.0
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 8 4
Please select something (1-6): 8
Thank you!

'''

from math import sin
from math import cos


print("Calculator")
number1 = int(input("Give the first number: "))
number2 = int(input("Give the second number: "))
select = True
resultFloat = 0.0

while select:
	print("(1) + \n (2) - \n (3) *\n (4) / \n (5)sin(number1/number2) \n (6)cos(number1/number2) \n (7) Change numbers \n (8) Quit ")
	print("Current numbers: ", number1, " ", number2)
	option = int(input("Please select something (1-6):"))
	if option == 1:
		result = number1 + number2
		print("The result is: ", result)
	elif option == 2:
		result = number1 - number2
		print("The result is: ", result)
	elif option == 3:
		result = number1 * number2
		print("The result is: ", result)
	elif option == 4:
		result = number1 / number2
		print("The result is: ", result)
	elif option == 5:
		resultFloat = sin(number1/number2)
		print("The result is: ", resultFloat)
	elif option == 6:
		resultFloat = cos(number1/number2)
		print("The result is: ", resultFloat)
	elif option ==7:
		number1 = int(input("Give the first number: "))
		number2 = int(input("Give the second number: "))
	elif option == 8:
		select = False
		print("Thank you!")
