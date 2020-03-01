def main(): #else-if

    letra = input("Enter letter(L / D / F)")


#testar casos e escrever mensagens

    if letra == "L" or letra == "l":
        print ("LIGAR")
    elif letra == "D" or letra == "d":
        print ("DESLIGAR")
    elif letra == "F" or letra =="f":
        print ("FURAR")
    else:
        print("Operacao invalida")    

main()
