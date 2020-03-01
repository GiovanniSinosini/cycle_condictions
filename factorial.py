def inicio():

    while True:
        n = int(input("Digite um numero positivo -> "))
        if n >= 0:
            break

    fat = 1

    if n > 1:
        for i in range(n, 0, -1):
            fat *= i # fat = fat * i
            print(i, end=' ')
            print (' x ' if i>1 else ' = ', end='')

    print(fat)






inicio()