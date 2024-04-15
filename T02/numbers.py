
#take user input 3 integers
num1, num2, num3 = map(int, input("Enter 3 different integers:").split())

#print sum of 3 numbers
sum_ofall = num1+ num2 + num3

print("Sum of all numbers = " + str(sum_ofall))

#first number minus second number
v_minus = num1 - num2
print("num1 - num2 = " + str(v_minus))

#third number multiplied by the first number
v_product = num3 * num1
print("num3 * num1 = " + str(v_product))

#the sum of all three numbers divided by the third number
v_div = sum_ofall / num3

print("Sum of all divide num3 = " + str(v_div))

