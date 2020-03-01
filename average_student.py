def main():

    nota1 = float(input ("Enter Math value: "))
    nota2 = float(input ("Enter Portuguese value: "))
    nota3 = float(input ("Enter English value: "))
    nota4 = float(input ("Enter Geography value: "))

    avarege= (nota1 + nota2 + nota3 + nota4)/4

    if avarege > 9.5:
        print ("Approved student with {:.2f} " .format(avarege))
    else:
        print ("Failed student with {:.2f}" .format(avarege))





#star program
main()

