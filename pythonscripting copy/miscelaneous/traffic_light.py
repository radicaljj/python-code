import time
from itertools import cycle
lights = [
    ("Green", 2),
    ("Yellow", 0.5),
    ("red", 2)
]
colors = cycle(lights)
while True:
    c, s = next(colors)
    print(c)
    time.sleep(s)
