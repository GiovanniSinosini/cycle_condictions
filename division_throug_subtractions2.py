def main():

    divisor = int(input("Enter divisor value: "))
    dividend = int(input("Enter dividend value: "))
    
    result=1
    saida = str(divisor) + "/" + str(dividend) + " = "
    
      
    while True:
        
            print(divisor, " - ", dividend, " = ", divisor-dividend)   
            divisor = divisor - dividend
            result += 1
            if (divisor - dividend < dividend):
                print(divisor, " - ", dividend, " = ", divisor-dividend) 
                break
                        
    saida += str(result)
    print (saida)    

main()
