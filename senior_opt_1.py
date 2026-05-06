import random

# Task 1: List filtering using List Comprehension and Lambda functions
def task1():
    n = int(input("Enter n: "))
    original_list = [random.randint(1, 20) for _ in range(n)]  # Generate random numbers between 1 and 20
    even_list = list(filter(lambda x: x % 2 == 0, original_list))
    print(original_list)
    print(even_list)

# Task 2: Operations in nested loops
def task2(matrix):
    for i, row in enumerate(matrix, 1):
        row_sum = sum(row)
        print(f"Առաջին տողի տարրերի գումարը {row_sum} է։"
              if i == 1 else f"Երկրորդ տողի տարրերի գումարը {row_sum} է։"
              if i == 2 else f"Երրորդ տողի տարրերի գումարը {row_sum} է։")

    total_sum = sum(sum(row) for row in matrix)
    average = total_sum / 9  # Since it's 3x3
    print(f"Բոլոր տարրերի թվաբանական միջինը {average} է։")

# Task 3: Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Task 4: OOP
class Pc:
    def __init__(self, year, model, ram, os, screen_size, memory):
        self.year = year
        self.model = model
        self.__ram = ram
        self.os = os
        self.screen_size = screen_size
        self.__memory = memory

    def change_os(self, new_os):
        self.os = new_os

    def update_ram(self, new_ram):
        self.__ram = new_ram

    def update_memory(self, new_memory):
        self.__memory = new_memory

class Notebook(Pc):
    def __init__(self, year, model, ram, os, screen_size, memory, battery_size):
        super().__init__(year, model, ram, os, screen_size, memory)
        self.battery_size = battery_size

# Example usage
if __name__ == "__main__":
    # Task 1
    task1()

    # Task 2
    matrix = [
        [12, -7, 0],
        [14, 23, 16],
        [-3, 14, 6]
    ]
    task2(matrix)

    # Task 3
    arr = [3, 6, 24, 104, 201, 205]
    target = 104
    if binary_search(arr, target):
        print(f"{target} թիվը կա ցուցակում։")
    else:
        print(f"{target} թիվը չկա ցուցակում։")

    target = 37
    if binary_search(arr, target):
        print(f"{target} թիվը կա ցուցակում։")
    else:
        print(f"{target} թիվը չկա ցուցակում։")

    # Task 4
    pc = Pc(2020, "Dell", 8, "Windows", 15.6, 512)
    notebook = Notebook(2021, "HP", 16, "Linux", 14, 1024, 50)