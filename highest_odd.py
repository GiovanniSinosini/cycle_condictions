def main():
    
    greatestOdd = 0
    position =0

    while True:
        n = int(input("Enter positive interger number: "))
        if n == 0:
            print ("Program terminated.")
            break
        if n < 0:
            print("Input error. Enter positive integer value.")

        if n > 0:
            position +=1
            if n % 2==1 and n > greatestOdd:
                greatestOdd = n
                position = position
     
    # mostrar resultado 
    if greatestOdd == 0:
        print ("No valid value entered")
    
    else:
        print ("The largest odd number entered was %d in position %d." %(greatestOdd, position))



main()