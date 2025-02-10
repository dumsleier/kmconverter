# Just another quick newbie project

# Welcome message
print("Hello stranger! What's your name and your desired distance in km?")

# User input to name and distance
name = input('My name is: ')
distancekm = input('My distance in km is: ')

# Replace comma with period if needed
if ',' in distancekm:
    distancekm = distancekm.replace(',', '.')

# Conversion of distance from km to miles
distancekm = float(distancekm)
distancemiles = distancekm / 1.609

# Output of the distance in miles
print(f'How you doing, {name.title()}? Your distance of {distancekm}km in miles is: {distancemiles:.2f} mi')

# Makes sure the user sees the result and press Enter to exit
input('Press ENTER to exit.')