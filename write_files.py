#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:29:31 2024

@author: jeffmarstell
"""
import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
    }


file_path = "/Users/jeffmarstell/Desktop/pyprogroamming/output.json"

try:
    
    with open(file_path, "a") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")

