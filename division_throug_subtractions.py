def main():

    
    while True: 
        divisor = int(input("Enter divisor value: "))
        dividend = int(input("Enter dividend value: "))

        if divisor>dividend and dividend!=0:
            break
        else:
            print ("Input error ! Divisor must be greater than dividend and nonzero dividend. ")



    result=1
    saida = str(divisor) + "/" + str(dividend) + " = "
    

      
    while divisor - dividend >= dividend:
        print(divisor, " - ", dividend, " = ", divisor-dividend)   
        divisor = divisor - dividend
        result += 1
    else:
        print(divisor, " - ", dividend, " = ", divisor-dividend)         
            
        
    saida += str(result)
    print (saida)    

main()
