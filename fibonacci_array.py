def main():
    print('--'*40)
    print ("Fibonacci sequency")
    print('--'*40)
     
    
    while True:
        n = int(input("How many terms do you want to show ? "))
        if n < 0 :
            print ("Input error. Enter positive integer value.")
        if n > 0:
            break
    res = []
    t1 = 0
    t2 = 1
    
    res.append(t1)
    res.append(t2)

    cont = 3
    while cont <= n:
        t3 = t1 + t2
        res.append(t3)
        t1 = t2
        t2 = t3
        cont +=1
    
    print(res)
























main()