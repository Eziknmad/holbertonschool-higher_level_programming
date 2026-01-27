#!/usr/bin/python3
Square = __import__('6-square').Square

# Test 1: Default position (0, 0)
print("Test 1: Default position (0, 0)")
s1 = Square(2)
s1.my_print()

# Test 2: Position with vertical offset
print("\nTest 2: Position (0, 2)")
s2 = Square(2, (0, 2))
s2.my_print()

# Test 3: Position with horizontal offset
print("\nTest 3: Position (5, 0)")
s3 = Square(2, (5, 0))
s3.my_print()

# Test 4: Position with both offsets
print("\nTest 4: Position (2, 1)")
s4 = Square(2, (2, 1))
s4.my_print()

# Test 5: Size 0
print("\nTest 5: Size 0 with position")
s5 = Square(0, (3, 3))
s5.my_print()

# Test 6: Change position
print("\nTest 6: Change position")
s6 = Square(3, (1, 0))
s6.my_print()
print("After changing position to (0, 1):")
s6.position = (0, 1)
s6.my_print()

# Test 7: Invalid position - not a tuple
print("\nTest 7: Invalid position - not a tuple")
try:
    s7 = Square(3, [1, 1])
except TypeError as e:
    print(e)

# Test 8: Invalid position - negative number
print("\nTest 8: Invalid position - negative number")
try:
    s8 = Square(3, (1, -1))
except TypeError as e:
    print(e)

# Test 9: Invalid position - not 2 elements
print("\nTest 9: Invalid position - 3 elements")
try:
    s9 = Square(3, (1, 1, 1))
except TypeError as e:
    print(e)

# Test 10: Invalid position - float
print("\nTest 10: Invalid position - float")
try:
    s10 = Square(3, (1.5, 0))
except TypeError as e:
    print(e)
