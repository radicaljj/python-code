inv = {
    "sword": 1,
    "potion": 3
}

loot = {
    "sword": 1,
    "potion": 2,
    "sheild": 1
}

new_inv = {
    k: inv.get(k,0) + loot.get(k, 0) \
    for k in set(inv | loot)
}

print(new_inv)