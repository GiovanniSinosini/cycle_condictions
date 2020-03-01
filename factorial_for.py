def main():

    while True:
        counter = int(input("Enter number: "))
        if counter > 0:
            break
        else:
            print ("Input ERROR !!!! Enter positive number. ")

    print ('The factorial of {} is: '.format(counter))
    f = 1
    for i in range (counter, 0, -1):
        print (i, end = '')
        print (' x ' if i > 1 else ' = ', end = '')

        f *= i
    print ('{}'.format(f))        

     













main()