inv = [
    "Gem",
    "sword",
    "sheild",
    "health Potion"
]

indx = inv.index("Gem")
item = inv.pop(indx)
inv.append(item)

print(inv)