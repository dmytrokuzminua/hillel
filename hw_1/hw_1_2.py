"""Homework 1 task 2"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width:int|float, height:int|float):
        """class Rectangle constructor"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of object instance"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimetr of object instance"""
        return (self.width*2)+(self.height*2)

    def is_square(self):
        """Get the instance is square"""
        return self.width == self.height

    def resize(self, new_width, new_height):
        """Set new options of object instance"""
        self.width = new_width
        self.height = new_height


def main():
    """main def"""
    curr_rectangle = Rectangle(5, 4)

    print("area = "+str(curr_rectangle.area()))
    print("perimetr = "+str(curr_rectangle.perimeter()))
    print("is square = "+str(curr_rectangle.is_square()))

    curr_rectangle.resize(6, 7)
    print("area = "+str(curr_rectangle.area()))
    print("perimetr = "+str(curr_rectangle.perimeter()))
    print("is square = "+str(curr_rectangle.is_square()))

    curr_rectangle.resize(5, 5)
    print("area = "+str(curr_rectangle.area()))
    print("perimetr = "+str(curr_rectangle.perimeter()))
    print("is square = "+str(curr_rectangle.is_square()))


if __name__ == "__main__":
    main()
