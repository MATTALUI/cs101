from math import pi

def calc_circle():
    radius = float(input("Radius: "))
    return pi * (radius ** 2)

def calc_rectangle():
    width = float(input("Width: "))
    height = float(input("Height: "))
    return width * height

def calc_triangle():
    return calc_rectangle() / 2

def invalid_input(*args):
    print("GET THAT CORN OUTTA MA FACE!")
    exit()

def get_shape():
    print("Options:\nr - rectangle\nt - triangle\nc - circle")
    return input("What shape would you like? ")

def get_calculator(shape_code):
    try:
        return {
            "r": calc_rectangle,
            "t": calc_triangle,
            "c": calc_circle
        }[shape_code.lower()]
    except:
        return invalid_input


def main():
    shape = get_shape()
    calculator = get_calculator(shape)
    area = calculator()
    print(f"Your area is: {area}")


if __name__ == "__main__":
    main()
