
#input age

age = int(input("Enter your age: "))

if (age > 40 and age < 65):
    print("You are over the hill.")
elif (age > 65 and age <= 100):
    print("Enjoy your retirement!")
elif age > 100:
    print("Sorry, you're dead.")
elif age < 13:
    print("You qualify for kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is just the number.")
    