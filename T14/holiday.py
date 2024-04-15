
# Calculate user's totdal holiday cost using user defined function

# Flight cost per destination city
city_Fcost = {'paris' : 150,
              'rome' : 200,
              'new york': 400,
              'barcelona' : 145,
              'amsterdam' : 150,
              'edinburgh' : 80}


# Options for Hotels and charge per nights 
hotel_pernight = {'1' : 80,
                  '2' : 65,
                  '3' : 70,
                  '4' : 120,
                  '5' : 134,
                  '6' : 165        
                  }

# Options available for Car rentals for number of days 
car_rentals = {6 : 50,
               5 : 65,
               4 : 70,
               3 : 73,
               2 : 84,
               1 : 90        
                  }

# Input destination city name for flight cost. City to be entered only from 
# the available list else raise exception and exit
city_flight = None
while city_flight is None:
    try:
        city_flight = input('''Enter the City you are travelling to. 
                       \n Choose from Paris, Rome, New York, Barcelona, Amsterdam, Edinburgh: ''').lower()

        if city_flight not in city_Fcost.keys():
            raise Exception("Please enter destination only from the list given")
    except Exception as e:
        print(e)
 #       exit()
        city_flight = input('''Enter the City you are travelling to. 
                       \n Choose from Paris, Rome, New York, Barcelona, Amsterdam, Edinburgh: ''').lower()
           
# Take input from user for number nights holiday stay.
# Stay should not be less than 1        
num_nights = int(input("Enter number of nights you are staying at hotel: "))
if num_nights <= 0:
    print("Please enter number for nights more than zero!")
#    exit()

repeat = False

while repeat == False:
    rental_days = int(input("Enter number of days you want to hire a car: "))
    if rental_days > num_nights:                                                                         # Check Car retnal days should not be more than totalholiday stay
        print("Ideally car rental requirement should be less or equal to number of holiday nights.")
    else:
        repeat = True


print("\nBelow are the options for hotels with charge per night is GBP")
print(hotel_pernight)

hotel_selected = input("\nPlease choose options from 1 to 6: ")

# Get the hotel cost per night from the dictionary
hotel_price = hotel_pernight.get(hotel_selected)

# Function to calculate hotel cost for total stay
def hotel_cost(nights, hotel_price):
    '''Function imports number of nights and hotel price as variables. Multiply to get total hotel cost for the stay'''
    hotel_cost = nights * hotel_price
    return hotel_cost

# Get flight cost from dictionary as per Key destination
def plane_cost(city_flight):
    '''Function imports city_flight as name of city from user. Fetch the cost of flight from dictionary city_fcost
    retrn the cost as plane_cost'''
    plane_cost = city_Fcost.get(city_flight)                    
    return plane_cost


def car_rental(rental_days):
    '''Function imports number of days for car rental. Fetch the cost of car based on days entered from dictionary object
    car_rentals. Then multiple number of days with per day cost to get total car_rental. Returns parameter car_rental'''
    if rental_days >= 6:
        temp_rental_days = 6 
    else:
        temp_rental_days = rental_days                               # If number of days more than or equals to 6 days the car costs the same per day
    car_cost = car_rentals.get(temp_rental_days)                     # Get car rental from dictionary as per number days as key in dictionary
    car_rental = car_cost * rental_days
    return car_rental


# Calculate total cost of holiday 
def holiday_cost(hotel_cost, plane_cost, car_rental):
    '''Function import 3 parameter values hotel_Cost, plane_cost, car_rental. Add them to get total holiday_cost. Return holiday_cost'''
    holiday_cost = hotel_cost + plane_cost + car_rental
    return holiday_cost



def holiday_cost1(hotel_cost, plane_cost, car_rental):
    '''Call functions hotel_cost, plane_cost, car_rental to calculate hotel, plane and car rental respectively
    then add those 3 cost to get total holiday cost. Return 4 variables'''
    hotel_cost = hotel_cost(num_nights, hotel_price)
    plane_cost = plane_cost(city_flight)
    car_rental = car_rental(rental_days)

    holiday_cost = hotel_cost + plane_cost + car_rental

    return holiday_cost, plane_cost, hotel_cost, car_rental




# Collect all function return values into variables so pass to holiday_cost function 
#hotel_cost = hotel_cost(num_nights, hotel_price)
#plane_cost = plane_cost(city_flight)
#car_rental = car_rental(rental_days)
holiday_cost, hotel_cost, plane_cost, car_rental = holiday_cost1(hotel_cost, plane_cost, car_rental)


print("***********************************************************************************************")
print()
print(f"Flight cost to city '{city_flight.capitalize()}' is : {plane_cost} GBP")
print(f"Hotel cost for {num_nights} nights is : {hotel_cost} GBP")
print(f"Car rental cost for {rental_days} days is : {car_rental} GBP")
print()
print(f"Total holiday cost for '{city_flight.capitalize()}' for {num_nights} nights with rental car for {rental_days} days is : {holiday_cost} GBP")
print()
print("***********************************************************************************************")

