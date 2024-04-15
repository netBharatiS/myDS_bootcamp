

str_manip = input("Enter any sentence: ")

#find length of string
length = len(str_manip)           

print("Length of string: " + str(length))

#Find last letter of string
last_char = str_manip[length-1: :1]
print(last_char)

# replace this letter by @ and print
str_manip1 = str_manip.replace(last_char,"@")

print(str_manip1)

# Find last 3 characters of string and print reverse
last_3char = str_manip[length-3: :1]
print(last_3char[::-1])

#find first 3 characters and last 2 chars of str_manip, concatenate and print
first_3char = str_manip[:3]
last_2char = str_manip[length-2: :1]

print(first_3char + last_2char)


