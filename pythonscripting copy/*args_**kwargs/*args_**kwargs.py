def order_pizza(size, *toppings, **kwargs):
    print(f"Ordered a {size} pizza")
    for topping in toppings:
        print(f"- {topping}")


order_pizza("large", "pepperoni", "peppers")
