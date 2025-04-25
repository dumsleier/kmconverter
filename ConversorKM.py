print("Hello! What's your name and your desired distance (in km?)")

name = input('My name is: ')
distancekm = input('My distance in km is: ')

# Replace comma(,) with period(.) if needed
if ',' in distancekm:
    distancekm = distancekm.replace(',', '.')

try:
    distancekm = float(distancekm)
    distancemiles = distancekm / 1.609

    print(f'Hi, {name.title()} :) Your distance of {distancekm}km in miles is: {distancemiles:.2f}mi')

except ValueError:
    print("Please enter a valid number for the distance.")

input('Press ENTER to exit. . . ')
