# Imports required for meal picker.
from random import choice
import random
import webbrowser


# List of meal choices
meat=['chicken', 'beef', 'lamb',]
vego=['salad', 'vege stirfry', 'vego meal']
sides=['pasta', 'rice', 'salad', 'couscous', 'chips']


meal = input("would you like meat or vego?: ")

if meal == "meat":
    random_meat = random.choice(meat)
    print(random_meat)
else:
    meal == "vego"
    random_vego = random.choice(vego)
    print(random_vego)
extras = input("do you want sides?: " )
if extras == "yes":
    random_sides = random.choice(sides)
meal = (random_meat + " and " + random_sides)

print("Your dinner is " + meal)

#open recipe website depensing on choice
recipe = input("do you want a recipe?: ")
if recipe == "yes":
    match meal:
        case "beef":
            webbrowser.open("https://www.taste.com.au/dinner/search?i1=%3A%3Abeef&i2=&i3=")
        case "chicken and rice":
            webbrowser.open("https://www.taste.com.au/dinner/search?i1=%3A%3Achicken&i2=%3A%3Arice&i3=")
        case "chicken and pasta":
            webbrowser.open("https://www.taste.com.au/dinner/search?i1=%3A%3Achicken&i2=4%3APasta%3Apasta&i3=")
        case "chicken and salad":
            webbrowser.open("https://www.bbcgoodfood.com/recipes/chicken-satay-salad")
        case "chicken and chips":
            webbrowser.open("https://www.taste.com.au/recipes/fancy-chicken-chips/fb41c1ef-44d1-46c6-a844-65e5ff9e6e1b")
        case "chicken and couscous":
            webbrowser.open("https://www.bbcgoodfood.com/recipes/one-pan-chicken-couscous")
        case "lamb and pasta":
            webbrowser.open("https://www.taste.com.au/dinner/search?i1=4%3APasta%3Apasta&i2=%3A%3Alamb&i3=")
        case "lamb and rice":
            webbrowser.open("https://www.taste.com.au/dinner/search?i1=%3A%3Alamb&i2=%3A%3Arice&i3=")
        case "lamb and salad":
            webbrowser.open("https://www.taste.com.au/recipes/warm-balsamic-lamb-salad/e55bfb2e-65ce-4a69-ab37-a8c07c2aa6b2")
        case "lamb and chips":
            webbrowser.open("https://sharedappetite.com/recipes/loaded-mediterranean-lamb-fries/")
        case "lamb and couscous":
            webbrowser.open("https://www.taste.com.au/recipes/15-minute-moroccan-lamb-couscous/231954af-09e9-4406-8d2a-c7aa099cbb4b")
        case "beef and pasta":
            webbrowser.open("https://www.recipetineats.com/slow-cooked-shredded-beef-ragu-pasta/")
        case "beef and rice":
            webbrowser.open("https://www.tasteofhome.com/recipes/korean-beef-and-rice/")
        case "beef and salad":
            webbrowser.open("https://www.recipetineats.com/thai-beef-salad-2/")
        case "beef and chips":
            webbrowser.open("https://www.taste.com.au/recipes/steak-chips-garlic-sauce/8154e583-535a-4adb-b27b-92447fd971ad")
        case "beef and couscous":
            webbrowser.open("https://www.beefitswhatsfordinner.com/recipes/recipe/46/beef-stir-fry-with-couscous")