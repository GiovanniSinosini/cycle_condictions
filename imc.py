from math import pow

# IMC calculation   formula = wight / height * height

weight = float(input("Enter weight value: "))
height = float(input("Enter height value: "))

#imc = weight / (height * height)

imc = weight / (pow(height,2))    #with pow imported need no declaration (math.pow) 

print("Your BMI is: {:.2f}" .format(imc))

