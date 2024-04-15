
# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")                     #brackets(parantheses) added to the print
print("\n")                                               #this line was too indented and brackets added to print

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"                                           #== is wrongly used instead = , changing value to "24" to as explained below
age = int(age_Str)                                       #valueError, age_str is a string with characters casting it into Integer gives error as hence correcting
print("I'm " + str(age) + " years old.")                        #print can only concatenate string hence typecasted 'age' to string

    # Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = age + int(years_from_now)                      #TypeError as int and string is concatenated. as per program logic total_years need number value by adding 

print("The total number of years:" + "answer_years")      #added parantheses

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12                                                        #variable total is not defined wrong variable used, replaced it with total_years 
print("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old")              #added parantheses and type casted total_months to string 
                                                                                                #& need to added 6 months more in total_months as per program requirement
#HINT, 330 months is the correct answer