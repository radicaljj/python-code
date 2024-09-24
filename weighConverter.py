#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:10:32 2024

@author: jeffmarstell
"""

weight = float(input("enter your weight: "))
unit = input("fKilograms or pounds?  (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid")
    
print(f"Your weight is : {round(weight, 1)} {unit}")
    