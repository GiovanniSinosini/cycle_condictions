
import math 

adjacent = float(input ("Enter the value of the side adjacent: "))

opposite = float(input("Enter the value of the side opposite: "))

#hypotenuse = math.sqrt((math.pow(adjacent, 2) + math.pow(opposite,2)))
#print ("Hypotenuse has a value of: ", hypotenuse)

#hypotenuse = ((adjacent ** 2) + (opposite ** 2)) **(1/2)
#print("Hypotenuse has a value of: {:.2f} " .format(hypotenuse))

hypotenuse = math.hypot(adjacent, opposite)
print("Hypotenuse has a value of: {:.2f}" .format(hypotenuse))