print("=" * 50)
print("Task 1: List Operations")
print("=" * 50)

numbers = []
print("Enter 5 numbers:")
for i in range(5):
    num = int(input())
    numbers.append(num)

unique = [x for x in numbers if numbers.count(x) == 1]

print("Original list:", numbers)
print("Unique elements:", sorted(unique))

print("\n" + "=" * 50)
print("Task 2: Recursive Functions")
print("=" * 50)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def digit_sum(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

print(f"GCD(48, 18)   = {gcd(48, 18)}")
print(f"GCD(100, 75)  = {gcd(100, 75)}")
print(f"Digit sum of 1234 = {digit_sum(1234)}")
print(f"Digit sum of 9999 = {digit_sum(9999)}")  # 36
 
 
# Task 3: File Processing and Data Analysis
print("\n" + "=" * 50)
print("Task 3: File Processing")
print("=" * 50)
 
def write_to_file():
    """Reads 5 lines from the user and saves them to string.txt"""
    lines = []
    print("Enter 5 lines:")
    for i in range(5):
        line = input(f"  Line {i + 1}: ")
        lines.append(line)
 
    with open("string.txt", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
 
    print("Lines saved to string.txt.")
 
def find_longest_word():
    """Opens string.txt and prints the longest word"""
    with open("string.txt", "r", encoding="utf-8") as f:
        content = f.read()
 
    words = content.split()
    if not words:
        print("The file is empty.")
        return
 
    longest = max(words, key=len)
    print(f"Longest word: '{longest}' ({len(longest)} characters)")
 
write_to_file()
find_longest_word()
 
 
# Task 4: OOP - Rectangle and Square
 
print("\n" + "=" * 50)
print("Task 4: OOP - Rectangle and Square")
print("=" * 50)
 
class Rectangle:
    """Represents a rectangle with width and height."""
 
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def surface(self):
        """Calculates and returns the area."""
        return self.width * self.height
 
    def perimeter(self):
        """Calculates and returns the perimeter."""
        return 2 * (self.width + self.height)
 
    def __str__(self):
        return (f"Rectangle(width={self.width}, height={self.height}) | "
                f"Area={self.surface()}, Perimeter={self.perimeter()}")
 
 
class Square(Rectangle):
    """Represents a square. Inherits from Rectangle."""
 
    def __init__(self, side):
        super().__init__(side, side)  # width == height == side
 
    def __str__(self):
        return (f"Square(side={self.width}) | "
                f"Area={self.surface()}, Perimeter={self.perimeter()}")
 
 
# Tests
rect = Rectangle(5, 3)
print(rect)
print(f"  Area:      {rect.surface()}")
print(f"  Perimeter: {rect.perimeter()}")
 
sq = Square(4)
print(sq)
print(f"  Area:      {sq.surface()}")
print(f"  Perimeter: {sq.perimeter()}")
 
# Confirm inheritance
print(f"\nIs Square an instance of Rectangle? {isinstance(sq, Rectangle)}")
