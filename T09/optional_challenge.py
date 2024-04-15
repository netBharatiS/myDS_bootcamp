#import math

####### calculate area of triangle

#input 3 sides of triangle
a, b, c = map(float, input("Enter length of three sides of Triangle: ").split())          #Runtime error will occur if more than 3 values entered by user
                                                                                          #Hence exception handling is required

# calculate semi perimeter s= (a+b+c)/2
s = a + b + c / 2                                               ## logical error would occur as / by 2 is for total of a, b, c. but this line consider it as a+b+c/2
                                                                #if a=12, b=4 c=15 then this expression gives answer 23.5 instead (15.5), hence need to correct to s= (a+b+c)/2

if s != 0                                                       #if without : gives compilation error
print("Semiperimeter of triangle = " + s)                       #Comapilation Error: wrong indentation of print, s needs casting to str(s)

# calculate area of triangle Area = sqrt(s(s-a)*(s-b)(s-c))

temp = s * (s - a) * (s - b) * (s - c)                        #Logical Error - expression will give wrong value than expected due to Logical Error because correct brackets are missing
                                                              #expression should be temp = s * ((s - a) * (s - b) * (s - c))

area_triangle = math.sqrt(temp)                               #would be runtime error - 'math' function is not defined - as import math liabrary is required

    print "Area of triangle = " + str(area_triangle)          #Compilation Error - wrong indentation and missing paranthesis