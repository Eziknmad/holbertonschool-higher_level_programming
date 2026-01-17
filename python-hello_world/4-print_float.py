#!/usr/bin/python3


number = 3.14159265359  # or try "3.14" (string) for error case


try:
    print(f"Float: {number:.2f}")
except (ValueError, TypeError) as e:
    print("ValueError: " + str(e))
