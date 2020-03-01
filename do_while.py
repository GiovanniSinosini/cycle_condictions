def main():

    # variáveis de saída
    nomeMelhorAluno = ""
    notaMelhorAluno = 0.0
    media = 0.0
    totalAlunos = 0


    while True:
        nomeAluno = input("Digite um nome do Aluno -> ")

        if nomeAluno == "STOP" or nomeAluno == "stop":
            break

        if nomeAluno != "":
            while True:
                notaPortugues = input("Digite a nota de Portugues do " + nomeAluno + " -> ")
                if notaPortugues.isnumeric() and int(notaPortugues) >= 0 and int(notaPortugues) <= 20:
                    if int(notaPortugues) < notaMelhorAluno:
                        notaMelhorAluno = int(notaPortugues)
                        nomeMelhorAluno = nomeAluno
                    media += int(notaPortugues)   
                    totalAlunos += 1
                    break
                else: 
                    print("ERRO - Invalid nota!!")
        else: 
            print ("ERROR - Invalid name!!!!")

#mostrar os resultados
    if nomeMelhorAluno == "":
        print ("Não foi introduzido qualquer nome e nota!!!")
    else:
        print("O aluno melhor classificado é ", nomeMelhorAluno, "com ", notaMelhorAluno, "valores!")
        media = media / totalAlunos
        print("Media de notas da turma a Portugues -> ", media, "valores.")














#start program
main()