# Getting user input
user_height = float(input('Enter your height in meters: '))
user_weight = float(input('Enter your weight in kg: '))

# Calculating BMI
user_bmi = str(round(user_weight/user_height**2))

# Printing BMI
print("Your BMI is: "+ user_bmi)