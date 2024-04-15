


number1 = int(input("Enter a number: "))

temp = 0
rev = 0

while number1 > 0:
    modulus_of_number = number1 % 10
    print(modulus_of_number)
    rev =rev * 10 +modulus_of_number
    print(rev)
    number1 = number1//10
    print(number1)

    print("_____________")

if temp ==rev:
    print("the number is palindrome")
else:
    print("The number is not palindrome")