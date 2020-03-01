def main():

    # Read a number
    print ("calculate the multiplication table of a number")
    numero = int(input("Enter number: "))
    
    
    
    i = 1    #contador

    while i <=10:
        res = numero * i
        print ("%d x %d = %d" % (numero, i, res) )
        i += 1 

    print ("End for program")



    #início programa
main()
