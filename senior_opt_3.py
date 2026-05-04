import random
from datetime import datetime

# Task 1: List filtering using List Comprehension and Lambda functions
def task1():
    n = int(input("Enter n: "))
    original_list = [random.randint(1, 20) for _ in range(n)]
    multiples_of_3 = list(filter(lambda x: x % 3 == 0, original_list))
    print(original_list)
    print(multiples_of_3)

# Task 2: Operations in nested loops
def task2(matrix):
    # Row sums
    row_sums = [sum(row) for row in matrix]
    max_sum = max(row_sums)
    print(f"Տողերի տարրերի գումարներից ամենամեծը {max_sum} է։")

    # Min element
    min_element = min(min(row) for row in matrix)
    print(f"Փոքրագույն տարրը {min_element} է։")

    # Sum of diagonal elements (both diagonals)
    diagonals = [matrix[i][i] for i in range(3)] + [matrix[i][2-i] for i in range(3)]
    diagonal_sum = sum(diagonals)
    print(f"Անկյունագծերի տարրերի գումարը {diagonal_sum} է։")

# Task 3: Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    barrier = arr[len(arr) // 2]
    less = [x for x in arr if x < barrier]
    equal = [x for x in arr if x == barrier]
    greater = [x for x in arr if x > barrier]
    return quick_sort(less) + equal + quick_sort(greater)

# Task 4: OOP
class Ebook:
    def __init__(self, title, year, author, genre, size, page, format_):
        self.title = title
        self.__year = year
        self.author = author
        self.genre = genre
        self.__size = size
        self.page = page
        self.format = format_

    def age(self):
        current_year = datetime.now().year
        return current_year - self.__year

    def info(self):
        return f"{self.author} {self.title}"

    def compress(self):
        self.__size = max(self.__size / 2, 10)

    def add_new_page(self, count):
        self.page += count

class KindleBook(Ebook):
    def set_drm(self):
        self.format = "DRM"

# Example usage
if __name__ == "__main__":
    # Task 1
    task1()

    # Task 2
    matrix = [
        [12, -7, 1],
        [14, 3, 16],
        [-3, 14, 6]
    ]
    task2(matrix)

    # Task 3
    arr = [-14, 102, 54, 0, -17]
    sorted_arr = quick_sort(arr)
    print(sorted_arr)

    # Task 4
    ebook = Ebook("Title", 2020, "Author", "Genre", 100, 200, "PDF")
    kindle = KindleBook("Title2", 2021, "Author2", "Genre2", 50, 150, "PDF")