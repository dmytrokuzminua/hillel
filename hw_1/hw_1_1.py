"""Homework 1 task 1"""


def main():
    """main def"""
    calculate_circle_area(input("Set circles`s radius:"))


def calculate_circle_area(radius:int|float):
    """Calculate the area of circle by radius"""
    print("The area of the circle with radius "+radius+ " is "+ str(3.14*float(radius)**2))


if __name__ == "__main__":
    main()
