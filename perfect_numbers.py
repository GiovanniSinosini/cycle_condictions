def main():
    n=0
    while n <= 0:
        n = int(input("Enter value greather than zero:"))
        if n<=0:
            print("ERROR - Invalid number") 
    
    # Determine if the number is perfect   - Em Matemática, um número perfeito é um número natural para o qual a soma de todos os seus divisores naturais próprios (excluindo ele mesmo) é igual ao próprio número.[1]Por exemplo, o número 28 é , pois: {\displaystyle \,\!28=1+2+4+7+14}\,\!28=1+2+4+7+14.

    soma = 0
    for x in range (1, n): 
        if n % x == 0:
            soma += x

    # mostrar resultado

    if n == soma:
        print ("Number %d is perfect. " %(n))
    else:
        print ("Number %d is not perfect" %(n))













main()