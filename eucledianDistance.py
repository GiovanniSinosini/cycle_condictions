def main():

    x1 = float(input("Enter x1 coordinate value: "))
    y1 = float(input("Enter y1 coordinate value: "))

    x2 = float(input("Enter x2 coordinate value: "))
    y2 = float(input("Enter y2 coordinate value: "))

    distance = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)     #**(1/2)   = square root

    if distance == 0:
        print ("Coincident points")
    else:
        print("The Eucledian distance between points is: {:.2f}" .format(distance))

#start program
main()
