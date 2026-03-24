# ================================================
# Task 1: Lists and Loops
# ================================================

print("=" * 50)
print("Task 1: Lists and Loops")
print("=" * 50)

even_numbers = []
odd_numbers = []

# a) Get 10 numbers from the user
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"  Number {i + 1}: "))

    # b) Separate into even and odd lists
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# c) Print both lists
print("Odd numbers: ", odd_numbers)
print("Even numbers:", even_numbers)


# ================================================
# Task 2: Recursive Functions
# ================================================

print("\n" + "=" * 50)
print("Task 2: Recursive Functions")
print("=" * 50)

# a) Recursive function: convert integer n to binary string
def to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return to_binary(n // 2) + str(n % 2)

# b) Recursive function: sum of all elements in a list
def list_sum(lst):
    if len(lst) == 0:      # base case: empty list
        return 0
    return lst[0] + list_sum(lst[1:])

# Tests - binary conversion
for num in [0, 5, 10, 255]:
    print(f"  to_binary({num}) = {to_binary(num)}")

# Tests - list sum
for lst in [[1, 2, 3], [10, 20, 30, 40], []]:
    print(f"  list_sum({lst}) = {list_sum(lst)}")


# ================================================
# Task 3: File Processing and Data Analysis
# ================================================

print("\n" + "=" * 50)
print("Task 3: File Processing")
print("=" * 50)

def write_user():
    """Gets first name, last name, and birth year from user and saves to user.txt"""
    first_name  = input("Enter first name:  ")
    last_name   = input("Enter last name:   ")
    birth_year  = input("Enter birth year:  ")

    with open("user.txt", "w") as f:
        f.write(f"First name: {first_name}\n")
        f.write(f"Last name:  {last_name}\n")
        f.write(f"Birth year: {birth_year}\n")

    print("User data saved to user.txt.")

def print_age():
    """Opens user.txt and prints the user's age in 2025"""
    with open("user.txt", "r") as f:
        lines = f.readlines()

    # Extract birth year from the third line
    birth_year = int(lines[2].split(":")[1].strip())
    age = 2025 - birth_year
    print(f"Age in 2025: {age}")

write_user()
print_age()


# ================================================
# Task 4: OOP - EqTriangle and RightTriangle
# ================================================
# https://tinyurl.com/2p9runb7

print("\n" + "=" * 50)
print("Task 4: OOP - EqTriangle and RightTriangle")
print("=" * 50)

import math

class EqTriangle:
    """Equilateral triangle with one private property: side."""

    def __init__(self, side):
        self.__side = side

    def surface(self):
        """Area of equilateral triangle: S = (sqrt(3) / 4) * a^2"""
        return (math.sqrt(3) / 4) * self.__side ** 2

    def perimeter(self):
        """Perimeter = 3 * side"""
        return 3 * self.__side

    def __str__(self):
        return (f"EqTriangle(side={self.__side}) | "
                f"Area={self.surface():.2f}, Perimeter={self.perimeter()}")


class RightTriangle:
    """Right triangle with two private properties: leg1 and leg2."""

    def __init__(self, leg1, leg2):
        self.__leg1 = leg1
        self.__leg2 = leg2 

    def surface(self):
        """Area = (leg1 * leg2) / 2"""
        return (self.__leg1 * self.__leg2) / 2

    def perimeter(self):
        """Perimeter = leg1 + leg2 + hypotenuse"""
        hypotenuse = math.sqrt(self.__leg1 ** 2 + self.__leg2 ** 2)
        return self.__leg1 + self.__leg2 + hypotenuse

    def __str__(self):
        return (f"RightTriangle(leg1={self.__leg1}, leg2={self.__leg2}) | "
                f"Area={self.surface():.2f}, Perimeter={self.perimeter():.2f}")


# Tests
eq = EqTriangle(6)
print(eq)
print(f"  Area:      {eq.surface():.2f}")
print(f"  Perimeter: {eq.perimeter()}")

rt = RightTriangle(3, 4)
print(rt)
print(f"  Area:      {rt.surface():.2f}")
print(f"  Perimeter: {rt.perimeter():.2f}")   # 3 + 4 + 5 = 12
