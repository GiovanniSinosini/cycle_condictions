def main():

    while True:
        base = int(input("Enter positive value base: "))
        exponent = int(input("Enter positive value exponent: "))

        if base>0 and exponent>0:
            break
        else:
            print("Input ERROR. Try again.")

    mult =1
    for i in range(1, exponent+1):
       print(base, 'x ' if i < exponent else '= ' , end='')
       mult *=base
        
    print (mult)
    print ("The number %d raised to %d is = %d " %(base, exponent, mult))   












#star program
main ()

