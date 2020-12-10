import math

def displayWelcome():
    print("Welcome to my area and perimeter calculator")
    print("======================================================")

def calcAreaCircle(radius):
    return math.pi * (radius ** 2)

def calcPerimeterCircle(radius):
    return radius * 2 * math.pi

def calcAreaSquare(side):
    return side ** 2

def calcPerimeterSquare(width):
    return 4 * width

def calcAreaRect(width, height):
    return width * height

def calcPerimeterRect(width, height):
    return (2 * width) + (2 * height)

def calcAreaTriangle(base, height):
    return calcAreaRect(base, height) / 2

# =====================================================================

# Main Code - DO NOT EDIT ANYTHING BELOW.  Add your functions above

displayWelcome()


radius = 3.56

area = calcAreaCircle(radius)

perimeter = calcPerimeterCircle(radius)

print('Circle   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


side = 9.23

area = calcAreaSquare(side)

perimeter = calcPerimeterSquare(side)

print('Square   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


width = 2.9

height = 14.22

area = calcAreaRect(width, height)

perimeter = calcPerimeterRect(width, height)

print('Rectangle: area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


base = 7.97

height = 5.31

area = calcAreaTriangle(base, height)

print('Triangle : area = {0:.2f}'.format(area))
