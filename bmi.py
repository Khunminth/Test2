def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = "+ str(weight))

    bmi = weight / (height*height)
    print ("BMI = ",bmi)
    if bmi < 18.5:
        print("User is under weight")
    elif bmi >= 18.5 and bmi<=25.0:
        print("user is normal weight")
    else :
        print("User is overweight")
calculate_bmi(weight = 65,height= 1.73)
