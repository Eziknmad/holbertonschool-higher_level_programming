#!/usr/bin/python3

number = 3.14159265359

try:
    print(f"Float: {number:.2f}")
except ValueError as e:
    print(e)
