# How big is the room?
# Build a program that asks the user to enter the length 
# and width of a room, in meters, then prints the room's area 
# in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# length = float(input("Enter the length of the room in meters: "))
# width = float(input("Enter the width of the room in meters: "))

# area_in_meters = length * width
# area_in_feet = area_in_meters * 10.7639

# print(f"The area of the room is {area_in_meters:.2f} "
#       f"square meters ({area_in_feet:.2f} square feet).")

# Further Exploration
# Modify the program to let the user specify the measurement type (meters or feet). 
# Compute the area accordingly and print it and its conversion in parentheses.

while True:
    measurement_type = (input("Would you like the area calculated in"
                            " meters or in feet? (meters or feet) "))
    
    length = float(input("Enter the length of the room: "))

    width = float(input("Enter the width of the room: "))

    area_in_meters = length * width

    area_in_feet = area_in_meters * 10.7639

    if measurement_type == 'meters':
        print(f"The area of the room is {area_in_meters:.2f} in square meters.")
        print(f"The area of the room is ({area_in_feet:.2f} in square feet).")
    elif measurement_type == 'feet':
        print(f"The area of the room is {area_in_feet:.2f} in square feet.")
        print(f"The area of the room is {area_in_meters:.2f} in square meters.")
    break
 
  

    

    

    


     


# def get_length():
#     length = float(input('Enter the length of the room, in meters: '))
#     return length

# def get_width():
#     width = float(input('Enter the width of the room, in meters: '))
#     return width

# def get_area_meters(length, width):
#     area = float(length * width)
#     return area

# def get_area_sqft(area_meters):
#     area = float(area_meters * 10.7639)
#     return area

# def validate_float(input):
#     return input == float


# l = get_length()
# w = get_width()

# area_meters = get_area_meters(l, w)

# print(f'{area_meters} meters')

# area_sqft = get_area_sqft(area_meters)

# print(f'{area_sqft:.2f} square feet')

