# bounce.py
#
# Exercise 1.5

height = 100 # Meters
bounce_ratio = 3/5 # Ratio of bounce to last height
bounces = 0 # Number of bounces

while bounces <= 9:
    bounces = bounces + 1
    height = height * bounce_ratio
    print(bounces, round(height, 4))