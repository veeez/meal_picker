# Imports required for meal picker.
from random import choice
import random
import webbrowser


# List of meal choices
meat=['chicken', 'beef', 'lamb', 'pork', 'fish']
vego=['salad', 'vege stirfry', 'vego meal']
sides=['veges', 'rice', 'salad', 'couscous', 'chips']


meal = input("would you like meat or vego?: ")

if meal == "meat":
    random_meat = random.choice(meat)
    print(random_meat)
else:
    veg = choice(vego)
    print(veg)
extras = input("do you want sides?: " )
if extras == "yes":
    side = choice(sides)
    print(side)
recipe = input("do you want a recipe?: ")
if recipe == "yes":
    match random_meat:
        case "chicken":
            webbrowser.open("https://www.taste.com.au/dinner/search?i1=1%3AChicken%3Achicken&i2=&i3=")
        case "lamb":
            webbrowser.open("https://www.taste.com.au/dinner/search?i1=%3A%3Alamb&i2=&i3=")
        case "pork":
            webbrowser.open("https://www.taste.com.au/dinner/search?i1=%3A%3Apork&i2=&i3=")
        case "fish":
            webbrowser.open("https://www.taste.com.au/dinner/search?i1=%3A%3Afish&i2=&i3=")
        case "beef":
            webbrowser.open("https://www.taste.com.au/dinner/search?i1=%3A%3Abeef&i2=&i3=")
