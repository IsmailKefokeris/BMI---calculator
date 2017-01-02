import math

print ("This is my BMI calculator Enjoy :)")

heightFeet = float(input("Enter Your height (Feet) "))
heightInches = float(input("Enter Your height (Inches) "))
weight = float(input("Enter your weight in Pounds: "))

def convertHtoM(x,y):
    convertI = (x * 12) + y
    convertM = convertI / 39.3701
    convert = convertM * convertM
    return (convert)

def pound2kilogram(x):
    convertKG = x / 2.204623
    return (convertKG)


def BMI(x,y):
    BMI = x / y
    return (BMI)


print (convertHtoM(heightFeet,heightInches))
print (pound2kilogram(weight))

heightM = convertHtoM(heightFeet,heightInches)
weightKG = pound2kilogram(weight)

print (BMI(weightKG,heightM))
