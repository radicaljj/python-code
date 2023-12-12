def split_integer(number, parts):

    qoutient, remainder = divmod(number, parts)

    base_parts_count = parts - remainder

    base_parts = base_parts_count * [qoutient]

    extra_parts = remainder * [qoutient + 1]

    return base_parts + extra_parts


def test():
    test = {
        "1": [2, 2, 3] == split_integer(7, 3),
        "2": [0, 0, 1, 1, 1] == split_integer(3, 5),
        "3": [2, 2, 3, 3,] == split_integer(10, 4),
        "4": [9, 10] == split_integer(19, 2),
        "5": [1, 1, 1, 2] == split_integer(5, 4),
    }
    for k, v in test.items():
        print(f'{k} {"Passed" if v else "Failed"}')


if __name__ == '__main__':
    test()
