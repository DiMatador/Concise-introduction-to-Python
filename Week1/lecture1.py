# Lecture 1 coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
def hello():
    print("Hello< World!!")
    
    #%%
def myName():
    print("My name is Julio")
    

#%% 
# """this is a function """
def myAge():
    print(" is 48 years old")


#%%
def areacircle(radius):
    """Computes the area of a circle"""
    area = 3.14 * radius**2
    print("The area of the circle radius ", radius, "is: ", area)
    

#%%
""" Write a fuction 'def areaTriangle(b,h) to compute the area of a triangle
formula is: area = .5*b*h
output should look like:
    The ara of a triangle of base 3 and height 5 is 7.5"""

def areaTriangle(b,h):
    area = .5*b*h
    print("The area of a triangle of base ",b," and ", "height " ,h," is: ", area)
    
#%%
""" Create a script to convert celsius to fahrenheit.
#     Formula  (°C) = (Fahrenheit - 32) / 1.8 """


def fahrenheit_to_celsious(temp):
    new_temp = (temp - 32) / 1.8
    print("The Fahrenheit temperature ",temp, "is equal to ", new_temp,end='')
    print(" degrees Celsius")
    
#%%
""" Write a Script to convert fahrenheit to celsius.
     Fahrenheit (°F) = (Celsius x 1.8) + 32 """
     
def celsius_to_fahren(temp):
    temp2 = (temp * 1.8) + 32
    print("The Celsius temperature is: ",temp, " is equal to " ,temp2,end=' ')
    print(" degrees Fahrenheit")
    
#%%
""" input from user and print to the screen.
    your could create a variable and store the city and province together than print them in one shot
    example: city_province =  city + ", " + province """

name = input("what's your name? ")
print(f"Hello, {name}, Python is great isnt it? ")
city = input(f"So what city do you live at ? {name} ")
print(f"{city} is a beautiful place? {name} ")
province = input("What province is that at? ")
print(f"{province} is in Canada ")
cold = input("It must be cold up there? ")
print(f"\'{cold}\' ooohh i dont know {name} i think your not telling the truth...... lol ")

#%%
""" if statements 
    Here we have 3 slitely different if statements.
    Examp: if, if-else, if-elif-else"""
    
""" declaire some variables """
x = 5
y = 0
z = 0

if x >= 0:
    print("x is positive")

if y > 0:
    print("y is positive")
    
else:
    print("y is not positive")
    
#elif can be repeated as often as necesarry

if z > 0:
    print("z is positive")
    
elif z < 0:
    print("z is negative")
    
else:
    print("z must be 0")
    

     
     

    
    
