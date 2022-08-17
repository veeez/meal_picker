# meal picker
from multiprocessing.connection import wait
from random import choice
import random
from subprocess import call
from time import sleep
import webbrowser
#What kind of meal would you like

meat=['chicken', 'beef', 'lamb', 'pork', 'fish']

vego=['salad', 'vege stirfry', 'vego meal']

sides=['veges', 'rice', 'salad', 'couscous', 'chips']

random_meat = random.choice(meat)
random_vego= random.choice(vego)
random_side= random.choice(sides)

meal = input("would you like meat or vego? \n")
if meal == "meat":
    print(random_meat)
elif meal == "vego":
    print(random_vego)
extras = input("do you want sides? \n" )
if extras == "yes":
    print(random_side)
recipe = input("do you want a recipe? \n")
if recipe == "yes" and random_meat == 'chicken':
  webbrowser.open("https://www.taste.com.au/dinner/search?i1=1%3AChicken%3Achicken&i2=&i3=")
elif random_meat == 'lamb':
    webbrowser.open("https://www.taste.com.au/dinner/search?i1=%3A%3Alamb&i2=&i3=")
elif random_meat == 'pork':
    webbrowser.open("https://www.taste.com.au/dinner/search?i1=%3A%3Apork&i2=&i3=")
elif random_meat == 'fish':
    webbrowser.open("https://www.taste.com.au/dinner/search?i1=%3A%3Afish&i2=&i3=")