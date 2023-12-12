import time
import random


def func(array):
    t = []
    z = 0
    for i in array:
        if i != 0:
            t.append(i)
        else:
            z += 1
    t.extend(z * [0])
    return t


n = 20000000
arr = [random.randint(0, 9) for _ in range(n)]
start = time.time()
x = func(arr)
stop = time.time()
print(stop-start)


# arr = [1, 2, 0, 3, 0, 4, 5]
# print(func(arr))
