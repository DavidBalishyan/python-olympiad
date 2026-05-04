import random

# Task 1: Arithmetic operations on list
def task1():
    a = int(input())
    b = int(input())
    c = int(input())
    lst = [a, b, c]
    new_lst = [24, lst[1] + 7, lst[2] ** 3]
    print(new_lst)

# Task 2: Conditional operators
def check_number(num):
    if num % 2 == 0:
        print("Թիվը զույգ է։")
    elif num > 10:
        print("Թիվը 10֊ից մեծ կենտ թիվ է։")
    else:
        print("Թիվը 10֊ից փոքր կենտ թիվ է։")

# Task 3: Set, loop, random
def task3():
    n = int(input())
    numbers = set()
    while len(numbers) < n:
        numbers.add(random.randint(1, 100))
    m = int(input())
    if m in numbers:
        print("YES")
    evens = [x for x in numbers if x % 2 == 0]
    even_sum = sum(evens)
    print(even_sum)

# Task 4: Recursive function for sum of even digits
def sum_even_digits(n):
    if n == 0:
        return 0
    digit = n % 10
    if digit % 2 == 0:
        return digit + sum_even_digits(n // 10)
    else:
        return sum_even_digits(n // 10)

# Example usage
if __name__ == "__main__":
    # Task 1
    task1()

    # Task 2
    num = int(input())
    check_number(num)

    # Task 3
    task3()

    # Task 4
    n = int(input())
    print(sum_even_digits(n))