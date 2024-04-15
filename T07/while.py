import math
sum = 0
i = 0
x = True
num = 0

while x == True:
  num = int(input("Enter a number: "))
  
  if num == -1:,.    
    break
  else:
    i = i + 1                                             # counter for numbers entered
    sum = sum + num                                  # calculate sum at end of every number entered 
    avg = sum / i                                    #calculate average
    print(f"Sum of numbers entered = {sum}")
    print(f"Number entered so far: {i}")
    print(f"Average of entered numbers is: {avg}")
