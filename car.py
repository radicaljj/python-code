#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:54:06 2024

@author: jeffmarstell
"""

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"you drive {self.color} {self.model}")
        
        
    def stop(self):
        print(f"you stopped {self.color} {self.model}")
   
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")