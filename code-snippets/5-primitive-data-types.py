# Python is a dynamically and strongly typed language which means:
    # Dynamically type: Dynamic typing means that the type of the variable is determined only during runtime.
    # Strongly Typed: Strong typing means that variables do have a type and that the type matters when performing operations on a variable

# string datatype
user_name = 'ajax123'
print(type(user_name))

# int type
user_age = 18

# float type
user_net_income = 123456.789012

# big numbere improved representation and seperation by _
#user_net_income = 123_456.789_012
print(type(user_age))
print(type(user_net_income))

# boolean
is_eligible_to_vote = True
print(type(is_eligible_to_vote))

# type error 
# Below generated TypeError: TypeError: can only concatenate str (not "int") to str
random_number = 15
# print('Your auto generated number is: '+ random_number)

# type conversion
print('Your auto generated number is: '+ str(random_number))