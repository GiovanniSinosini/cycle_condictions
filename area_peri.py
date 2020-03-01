
pi = 3.1415

# Calculator perimeter and area

radius = float(input("Enter radius value (in centimeters): "))

area = pi * (radius **2)
perimeter = 2 * pi * radius

print("The area value is:{:.2f}".format(area))
print( "The perimeter value is:{:.2f}".format(perimeter))