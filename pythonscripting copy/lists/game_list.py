hotbar = [
    "Torch",
    "Rock",
    "Potion",
    "Sword",
    "sheild"
]
index = hotbar.index("Sword")
item = hotbar.pop(index)
hotbar.insert(0, item)
print(hotbar)
