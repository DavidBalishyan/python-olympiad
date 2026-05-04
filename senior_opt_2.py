import random
from datetime import datetime

# Task 1: List filtering using List Comprehension and Lambda functions
def task1():
    n = int(input("Enter n: "))
    original_list = [random.randint(1, 20) for _ in range(n)]
    odd_list = list(filter(lambda x: x % 2 != 0, original_list))
    print(original_list)
    print(odd_list)

# Task 2: Operations in nested loops
def task2(matrix):
    # First row product
    first_row_product = 1
    for num in matrix[0]:
        first_row_product *= num
    print(f"Առաջին տողի տարրերի արտադրյալը {first_row_product} է։")

    # Second column product
    second_col_product = 1
    for row in matrix:
        second_col_product *= row[1]
    print(f"Երկրորդ սյան տարրերի արտադրյալը {second_col_product} է։")

    # Average of diagonal elements (main and anti-diagonal)
    diagonals = [matrix[i][i] for i in range(3)] + [matrix[i][2-i] for i in range(3)]
    average = sum(diagonals) / len(diagonals)
    print(f"Անկյունագծերի տարրերի միջինը {average} է։")

# Task 3: Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = None
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            result = arr[mid]
            right = mid - 1
        else:
            left = mid + 1
    return result

# Task 4: OOP
class Car:
    def __init__(self, year, brand, model, max_speed, color, price):
        self.year = year
        self.brand = brand
        self.model = model
        self.__max_speed = max_speed
        self.color = color
        self.price = price

    def age(self):
        current_year = datetime.now().year
        return current_year - self.year

    def info(self):
        return f"{self.brand} {self.model} {self.year}"

    def update_color(self, new_color):
        self.color = new_color

    def price_rate(self, rate):
        return self.price * rate

class Ecar(Car):
    def __init__(self, year, brand, model, max_speed, color, price, battery_size):
        super().__init__(year, brand, model, max_speed, color, price)
        self.battery_size = battery_size

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
    arr = [3, 6, 24, 102, 201, 205]
    target = 104
    result = binary_search(arr, target)
    print(result)

    # Task 4
    car = Car(2020, "Toyota", "Camry", 200, "Red", 25000)
    ecar = Ecar(2021, "Tesla", "Model 3", 140, "White", 35000, 75)