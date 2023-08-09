def BMI(height, weight):
    bmi = weight/(height**2)
    return bmi

height =float(input("Please enter your height in meters:"))
weight = int(input("Please enter your weight in kg:"))
 
bmi = BMI(height, weight)
print("THE BMI IS :",bmi)
print ("You're",end=" ") 
if (bmi < 18.5):
    print("underweight")
 
elif ( bmi >= 18.5 and bmi < 24.9):
    print("Healthy")
 
elif ( bmi >= 24.9 and bmi < 30):
    print("overweight")
 
elif ( bmi >=30):
    print("Suffering from Obesity")