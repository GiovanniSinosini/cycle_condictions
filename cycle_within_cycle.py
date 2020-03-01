def main():

    i = 1
    while i <= 3:
        print ("EXTERNAL CYCLE", i)
        for x in range(1,6):
            print ("\tinternal cycle", x)
        i += 1







#start program
main()
