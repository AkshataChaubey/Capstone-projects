height=float(input("Enter your height in centimetre: "))
weight=float(input("Enter your weight in kilogram: "))
height=height/100
bmi=weight/(height *height)

print("Your Body mass index is: ",bmi)
if bmi==16:
    print("Severe thinness")
elif bmi<=18.5:
    print("Normal")
elif bmi<=25:
    print("Overweight")
else:
    print("Obesity")   
       
        
