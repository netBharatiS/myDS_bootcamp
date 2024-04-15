
# ### Determines award a person receives after completing triathlon

swimming = 0
cycling = 0
running = 0

swimming, cycling, running= [int(x) for x in input("Enter time taken by Athlete in Swimming, cycling and running respectively in minutes:  ").split()]

if swimming == "" or cycling == "" or running == "":
    print("Please Enter 3 values respectively for Swimming, Cycling and Running: ")


total_timetaken = swimming + cycling + running

print(f"\nAthlete completed Swimming in {swimming} mins, Cycling in {cycling} mins and Running in {running} mins")
print()
print(f"Total time taken by athlete to complete this Triathlon is {total_timetaken} mins")
print()

if total_timetaken <= 100:
    print("Congratualtions!!!")
    print("Athlete is awarded with 'Provincial Colours'")
elif total_timetaken >= 101 and total_timetaken <= 105:
    print("Congratualtions!!!")
    print("Athlete is awarded with 'Provincial Half Colours'")
elif total_timetaken >= 106 and total_timetaken <=110:
    print("Congratualtions!!!")
    print("Athlete is awarded with 'Provincial Scroll'")
elif total_timetaken >= 111:
    print("Sorry")
    print("Athlete is not qualified for award. 'No Award'")

print()




