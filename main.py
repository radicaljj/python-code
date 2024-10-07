#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:45:35 2024

@author: jeffmarstell
"""
from car import Car

        
car1 = Car("Corvette", 2024, "red", False)
car2 = Car("Mustang", 2025, "blue", True)
car3 = Car("Charger", 2026, "Yellow", True)


car1.drive()
car2.stop()
car3.drive()

car1.describe()
car2.describe()
car3.describe()

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)