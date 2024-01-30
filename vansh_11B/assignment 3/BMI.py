print ("")

height = float(input("Enter height:"))

weight = float(input("Enter Weight"))

BMI = weight/height**2

print ("")

print ("Your BMI is", BMI)

print ("")


if BMI <= 18.4 :
    print ("Your status according to your BMI is UNDERWEIGHT")

elif BMI > 18.4 and BMI <= 24.9 :
    print ("Your status according to your BMI is NORMAL")

elif BMI > 24.9 and BMI <= 39.9 :
    print ("Your status according to your BMI is OVERWEIGHT")
    
elif BMI > 39.9 :
    print ("Your status according to your BMI is OBESE")

