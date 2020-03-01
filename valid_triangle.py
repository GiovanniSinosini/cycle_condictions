def main():

    x1 = float(input("Enter x1 coordinate value: "))
    y1 = float(input("Enter y1 coordinate value: "))

    x2 = float(input("Enter x2 coordinate value: "))
    y2 = float(input("Enter y2 coordinate value: "))

    x3 = float(input("Enter x3 coordinate value: "))
    y3 = float(input("Enter y3 coordinate value: "))

    a = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)     #**(1/2)   = square root
    b = (((x3 - x2)**2) + ((y3 - y2)**2))**(1/2)
    c = (((x3 - x1)**2) + ((y3 - y1)**2))**(1/2)

    if a < b+c and b< a+c and c < b+a:
        print ("The three points form a triangle")
    else:
        print("The three points DO NOT form a triangle")





#start program
main()
