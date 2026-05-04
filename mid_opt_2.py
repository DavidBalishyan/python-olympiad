# Task 1: Lists and Strings
print("=" * 50)
print("Task 1: Lists and Strings")
print("=" * 50)
 
# a) Get 5 words from the user and store in a list
words = []
print("Enter 5 words:")
for i in range(5):
    word = input(f"  Word {i + 1}: ")
    words.append(word)
 
# b) Create a new list with only words whose length is greater than 4
long_words = [w for w in words if len(w) > 4]
 
# c) Print both lists
print("Original list:", words)
print("Words longer than 4:", long_words)
 
 
# Task 2: Recursive Functions
print("\n" + "=" * 50)
print("Task 2: Recursive Functions")
print("=" * 50)
 
# a) Recursive function to check if n is a prime number
#    Helper checks divisors from 2 up to sqrt(n)
def is_prime(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:   # no divisor found → prime
        return True
    if n % divisor == 0:        # divisible → not prime
        return False
    return is_prime(n, divisor + 1)
 
# b) Recursive function to check if a string is a palindrome
def is_palindrome(s):
    if len(s) <= 1:             # base case: 0 or 1 characters
        return True
    if s[0] != s[-1]:           # first and last chars differ
        return False
    return is_palindrome(s[1:-1])  # check the inner substring
 
# Tests - prime
for num in [2, 7, 10, 13, 25]:
    print(f"  is_prime({num}) = {is_prime(num)}")
 
# Tests - palindrome
for word in ["racecar", "hello", "madam", "python", "level"]:
    print(f"  is_palindrome('{word}') = {is_palindrome(word)}")
 
 
# Task 3: File Processing and Data Analysis
print("\n" + "=" * 50)
print("Task 3: File Processing")
print("=" * 50)
 
def write_numbers():
    """Reads 10 numbers from the user and saves them to numbers.txt"""
    numbers = []
    print("Enter 10 numbers:")
    for i in range(10):
        num = float(input(f"  Number {i + 1}: "))
        numbers.append(num)
 
    with open("numbers.txt", "w") as f:
        for num in numbers:
            f.write(str(num) + "\n")
 
    print("Numbers saved to numbers.txt.")
 
def calculate_average():
    """Opens numbers.txt and prints the arithmetic mean of all numbers"""
    with open("numbers.txt", "r") as f:
        numbers = [float(line.strip()) for line in f if line.strip()]
 
    if not numbers:
        print("The file is empty.")
        return
 
    average = sum(numbers) / len(numbers)
    print(f"Arithmetic mean: {average:.2f}")
 
write_numbers()
calculate_average()
 
 
# ================================================
# Task 4: OOP - Circle and Square
# ================================================
 
print("\n" + "=" * 50)
print("Task 4: OOP - Circle and Square")
print("=" * 50)
 
import math
 
class Circle:
    """Represents a circle with a given radius."""
 
    def __init__(self, radius):
        self.radius = radius
 
    def surface(self):
        """Calculates and returns the area of the circle."""
        return math.pi * self.radius ** 2
 
    def length(self):
        """Calculates and returns the circumference of the circle."""
        return math.tau * self.radius
 
    def __str__(self):
        return (f"Circle(radius={self.radius}) | "
                f"Area={self.surface():.2f}, Circumference={self.length():.2f}")
 
 
class Square:
    """Represents a square with a given side length."""
 
    def __init__(self, side):
        self.side = side
 
    def surface(self):
        """Calculates and returns the area of the square."""
        return self.side ** 2
 
    def perimeter(self):
        """Calculates and returns the perimeter of the square."""
        return 4 * self.side
 
    def __str__(self):
        return (f"Square(side={self.side}) | "
                f"Area={self.surface()}, Perimeter={self.perimeter()}")
 
 
# Tests
c = Circle(5)
print(c)
print(f"  Area:          {c.surface():.2f}")
print(f"  Circumference: {c.length():.2f}")
 
sq = Square(4)
print(sq)
print(f"  Area:      {sq.surface()}")
print(f"  Perimeter: {sq.perimeter()}")
 
