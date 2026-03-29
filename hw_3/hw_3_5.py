""" Homework 3 task 5 """


class MyNumbers:
    """Class My numbers"""
    def __init__(self, data) -> None:
        self.data = data

    def __len__(self) -> int:
        """dunder method for custom_len method"""
        return len(self.data)

    def __iter__(self):
        """dunder method for custom_sum и custom_min methods"""
        return iter(self.data)


def custom_len(obj: MyNumbers) -> int:
    """Custom len method"""
    return obj.__len__()

def custom_sum(iterable) -> int|float:
    """Custom sum method"""
    total = 0
    for x in iterable:
        total += x
    return total

def custom_min(iterable) -> int|float:
    """Custom min method"""
    it = iter(iterable)
    res = next(it)
    for x in it:
        if x < res:
            res = x
    return res


def main():
    """main def"""
    nums = MyNumbers([5, 2, 10, 1])

    print(custom_len(nums) == 4)
    print(custom_sum(nums) == 18)
    print(custom_min(nums) == 1)

    print("Тесты для MyNumbers пройдены успешно!")


if __name__ == "__main__":
    main()
