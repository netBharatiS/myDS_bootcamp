
number_builder = ""
i = 0

while i <= 50:
  if i % 2 == 0:
    number_builder += str(i) + " "
  i += 1

print(number_builder)

#************************************************************

number_list = []

j = 0

while j <= 50:
  if j % 2 == 0:
    number_list.append(str(j))
  j += 1

print(" ".join(number_list))
