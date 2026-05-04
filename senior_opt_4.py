import random
from datetime import datetime

# Task 1: List processing with Lambda
def task1():
    n = int(input("Enter n: "))
    original_list = [random.randint(1, 20) for _ in range(n)]
    double_func = lambda x: x * 2
    doubled_list = list(map(double_func, original_list))
    print(original_list)
    print(doubled_list)

# Task 2: Operations in nested loops
def task2(matrix):
    # Column sums
    col_sums = [sum(matrix[i][j] for i in range(3)) for j in range(3)]
    max_col_sum = max(col_sums)
    print(f"Սյուների տարրերի գումարներից ամենամեծը {max_col_sum} է։")

    # Negative elements
    negatives = [num for row in matrix for num in row if num < 0]
    print(f"Բացասական տարրերն են {', '.join(map(str, negatives))}։")

    # Sum of even numbers
    evens = [num for row in matrix for num in row if num % 2 == 0]
    even_sum = sum(evens)
    print(f"Զույգ թվերի գումարը կլինի {even_sum}։")

# Task 3: Quick Sort by string length
def quick_sort_strings(arr):
    if len(arr) <= 1:
        return arr
    barrier = len(arr[len(arr) // 2])
    less = [x for x in arr if len(x) < barrier]
    equal = [x for x in arr if len(x) == barrier]
    greater = [x for x in arr if len(x) > barrier]
    return quick_sort_strings(less) + equal + quick_sort_strings(greater)

# Task 4: OOP
class Footballer:
    def __init__(self, name, year, weight, height, nationality, current_club, position):
        self.name = name
        self.__year = year
        self.weight = weight
        self.height = height
        self.__nationality = nationality
        self.current_club = current_club
        self.position = position

    def age(self):
        current_year = datetime.now().year
        return current_year - self.__year

    def info(self):
        return f"{self.name} {self.age()} {self.__nationality} {self.current_club}"

    def update_weight(self, new_weight):
        self.weight = new_weight

    def change_club(self, new_club):
        self.current_club = new_club

    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

class ExFootballer(Footballer):
    def retire(self):
        self.current_club = None

    # Does not inherit change_club, so override to do nothing or raise error
    def change_club(self, new_club):
        pass  # or raise NotImplementedError

# Example usage
if __name__ == "__main__":
    # Task 1
    task1()

    # Task 2
    matrix = [
        [12, -7, 1],
        [14, 3, 16],
        [-2, 14, 6]
    ]
    task2(matrix)

    # Task 3
    arr = ["apple", "new", "all", "sort", "avocado", "or"]
    sorted_arr = quick_sort_strings(arr)
    print(sorted_arr)

    # Task 4
    footballer = Footballer("Name", 1990, 70, 180, "Nationality", "Club", "Position")
    ex_footballer = ExFootballer("ExName", 1985, 75, 175, "ExNat", "ExClub", "ExPos")