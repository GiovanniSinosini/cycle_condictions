def main():

    nomePessoaMaisNova = ""
    idadePessoaMaisNova = 150


    '''name = "vazio"

    while name != "STOP":
        name = input("Enter name: ")
        age = int(input("Enter age: "))

    print (name, age)'''

    while True:
        nomeAtual = input("Digite um nome -> ")

        if nomeAtual == "STOP" or nomeAtual == "stop":
            break

        if nomeAtual != " ":
            while True:
                idadeAtual = input("Digite a idade do " + nomeAtual + " -> ")
                if idadeAtual.isnumeric() and int(idadeAtual) > 0 and int(idadeAtual) <= 150:
                    if int(idadeAtual) < idadePessoaMaisNova:
                        idadePessoaMaisNova = int(idadeAtual)
                        nomePessoaMaisNova = nomeAtual
                    break
                else: 
                    print("ERRO - Invalid age!!")
        else: 
            print ("ERROR - Invalid name!!!!")

#mostrar os resultados
    if nomePessoaMaisNova == "":
        print ("Não foi introduzido qualquer nome e idade!!!")
    else:
        print("A pessoa mais nova é ", nomePessoaMaisNova, "que tem", idadePessoaMaisNova, "anos!")








main()