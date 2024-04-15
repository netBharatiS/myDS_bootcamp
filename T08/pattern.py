#print the pattern
#*
#**
#***
#****
#*****
#****
#***
#**
#*
# using 2 for loops

rows = ""
num = 1

for i in range (1, 10):
  if i < 6:
    for j in range(i):
      #rows += "*"
      print("*", end= "")
    print()
  else:
    numdown = i - (2 * num)        #to reduce the pattern number for increasing row
    for j in range(numdown):
      print("*", end = "")
    num +=1
    print() 


#print the pattern
#*
#**
#***
#****
#*****
#****
#***
#**
#*
# using if condition and not 2 for loops

pattern = "*"

num = 1
to_print = pattern * num
for i in range(1,10):
  if i < 6:
  #  num = i
    to_print = pattern * i
    print(to_print)
  else:
    numdown = i -(2*num)         #to get number for * for increasing row number
    to_print = pattern * numdown
    print(to_print)
    num += 1





