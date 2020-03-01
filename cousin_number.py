def main():

    #inserir numero maior que zero
    num = 0
    while num <=0:
        num = int(input("Enter number: "))

    ePrimo = True #flag

#verificar se numero é primo
    for x in range(2, num):
        if num % x == 0:
            ePrimo = False
            break
#mostrar resultado
    if ePrimo == True: #<=> if ePrimo:
        print ("Number %d is cousin "%(num))
    else:
        print ("Number %d is not cousin" %(num))






#start program
main()