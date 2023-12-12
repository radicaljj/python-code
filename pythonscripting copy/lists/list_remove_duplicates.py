old = ["a", "b", "c", "d", "b", "a"]

new = list(dict.fromkeys(old).keys())

print(new)