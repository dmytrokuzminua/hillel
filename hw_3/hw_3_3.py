""" Homework 3 task 3 """


class Person:
    """ Class Person"""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __lt__(self, other) -> bool:
        """ Returns the result of comparing `age1 < age2`  of Person instances """
        return self.age < other.age

    def __eq__(self, other) -> bool:
        """ Returns the result of comparing ages of Persons for equality """
        return self.age == other.age

    def __gt__(self, other) -> bool:
        """ Returns the result of comparing `age1 > age2`  of Person instances """
        return self.age > other.age

    def __repr__(self) -> str:
        """ Returns Person`s representation """
        return f"{self.name}  ({self.age}) "

def main():
    """main def"""
    people = [
        Person("Anna", 25),
        Person("Ivan", 20),
        Person("Olga", 30),
        Person("Petro", 22)
    ]

    print(people)

    for i in range(len(people)):
        change_flag = False
        for j in range(0, len(people) - i - 1):
            if people[j] > people[j+1]:
                people.insert(j+1, people.pop(j))
                change_flag = True
        if not change_flag:
            break

    print(people)


if __name__ == "__main__":
    main()
