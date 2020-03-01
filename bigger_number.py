def main():

    n1 = float(input("Enter number1: "))
    n2 = float(input("Enter number2: "))
    n3 = float(input("Enter number3: "))

    if n1 > n2 and n1 > n3:
        print ('The %.2f is bigger number' % n1)
    elif n2 > n3:
        print ('The %.2f is bigger number' % n2)
    else:
        print ('The %.2f is bigger number' % n3)



#start program
main()

