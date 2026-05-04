# Task 1: Dictionaries and Sets
print("=" * 50)
print("Task 1: Dictionaries and Sets")
print("=" * 50)

students = {}

# a) Get 5 student names and their ages
print("Enter 5 student names and ages:")
for i in range(5):
    name = input(f"  Name {i + 1}: ")
    age  = int(input(f"  Age  {i + 1}: "))
    students[name] = age

# b) Print the dictionary
print("Students dictionary:", students)

# c) Print the youngest student's age
youngest_age = min(students.values())
print("Youngest age:", youngest_age)


# Task 2: Recursive Functions
print("\n" + "=" * 50)
print("Task 2: Recursive Functions")
print("=" * 50)

# a) Recursive function to reverse a string
def reverse_string(s):
    if len(s) <= 1:          # base case: empty or single character
        return s
    return reverse_string(s[1:]) + s[0]

# b) Recursive function to find the product of all elements in a list
def list_product(lst):
    if len(lst) == 0:        # base case: empty list
        return 1             # neutral element for multiplication
    return lst[0] * list_product(lst[1:])

# Tests - reverse string
for s in ["Hello world", "Python", "a"]:
    print(f"  reverse_string('{s}') = '{reverse_string(s)}'")

# Tests - list product
for lst in [[1, 2, 3, 4], [5, 6], [7]]:
    print(f"  list_product({lst}) = {list_product(lst)}")


# Task 3: File Processing and Data Analysis
print("\n" + "=" * 50)
print("Task 3: File Processing")
print("=" * 50)

def write_text():
    """Gets a string from the user and saves it to text.txt"""
    text = input("Enter a string: ")
    with open("text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Text saved to text.txt.")

def find_most_frequent():
    """Opens text.txt, finds the most repeated word(s), saves result to count.txt"""
    with open("text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Clean punctuation and split into words
    import string
    clean = text.translate(str.maketrans("", "", string.punctuation))
    words = clean.lower().split()

    if not words:
        print("No words found.")
        return

    # Count word frequencies
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    # Find the maximum frequency
    max_count = max(freq.values())

    # Collect all words that share the maximum frequency
    most_frequent = [w for w, c in freq.items() if c == max_count]

    # Build result lines and save to count.txt
    lines = [f'"{w}" has been repeated {max_count} times' for w in most_frequent]
    result = "\n".join(lines)

    with open("count.txt", "w", encoding="utf-8") as f:
        f.write(result + "\n")

    print("Result saved to count.txt:")
    print(result)

write_text()
find_most_frequent()


# Task 4: OOP - Hexagon and Square

print("\n" + "=" * 50)
print("Task 4: OOP - Hexagon and Square")
print("=" * 50)

import math

class Hexagon:
    """Regular hexagon with one private property: side."""

    def __init__(self, side):
        self.__side = side          # private attribute

    def surface(self):
        """Area of regular hexagon: S = (3 * sqrt(3) / 2) * a^2"""
        return (3 * math.sqrt(3) / 2) * self.__side ** 2

    def perimeter(self):
        """Perimeter = 6 * side"""
        return 6 * self.__side

    def __str__(self):
        return (f"Hexagon(side={self.__side}) | "
                f"Area={self.surface():.2f}, Perimeter={self.perimeter()}")


class Square:
    """Square with one private property: side."""

    def __init__(self, side):
        self.__side = side          # private attribute

    def surface(self):
        """Area = side^2"""
        return self.__side ** 2

    def diagonal(self):
        """Diagonal = side * sqrt(2)"""
        return self.__side * math.sqrt(2)

    def __str__(self):
        return (f"Square(side={self.__side}) | "
                f"Area={self.surface()}, Diagonal={self.diagonal():.2f}")


# Tests
h = Hexagon(4)
print(h)
print(f"  Area:      {h.surface():.2f}")
print(f"  Perimeter: {h.perimeter()}")

sq = Square(5)
print(sq)
print(f"  Area:     {sq.surface()}")
print(f"  Diagonal: {sq.diagonal():.2f}")
