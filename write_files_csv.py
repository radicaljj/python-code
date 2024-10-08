#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:29:31 2024

@author: jeffmarstell
"""
import json
import csv

employees =[["Name", "age", "Job"],
           ["Spongebob", 30, "cook"],
           ["Patrick", 37, "Unemployed"],
           ["Sandy", 27, "Scientist"]]

file_path = "/Users/jeffmarstell/Desktop/pyprogroamming/output.csv"

try:
    
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")

