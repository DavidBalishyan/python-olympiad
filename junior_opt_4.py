import random

# Task 1: Arithmetic operations on list
def task1():
    a = int(input())
    b = int(input())
    c = int(input())
    lst = [a, b, c]
    lst[0] = 23
    lst[1] *= 2
    print(lst)
    max_val = max(lst)
    min_val = min(lst)
    print(max_val + min_val)

# Task 2: Conditional operators for string
def check_string(s):
    if s.startswith("A"):
        print("Տողը սկսում է “A” տարրով։")
    elif len(s) > 5:
        print("Տողի երկարությունը մեծ է 5֊ից և այն չի սկսում “A”֊ով։")
    else:
        print("Տողի երկարությունը մեծ չէ 5֊ից և այն չի սկսվում “A”-ով։")

# Task 3: Tuple, loop, random
def task3():
    numbers = [random.randint(1, 100) for _ in range(8)]
    tuple1 = tuple(numbers[:4])
    tuple2 = tuple(numbers[4:])
    m = int(input())
    if m in tuple1 or m in tuple2:
        print("YES")
    evens1 = [x for x in tuple1 if x % 2 == 0]
    even_sum1 = sum(evens1)
    print(even_sum1)
    max_both = max(max(tuple1), max(tuple2))
    print(max_both)

# Task 4: Recursive function for sum of even numbers
def sum_even(n):
    if n < 2:
        return 0
    if n % 2 == 0:
        return n + sum_even(n - 2)
    else:
        return sum_even(n - 1)

# Example usage
if __name__ == "__main__":
    # Task 1
    task1()

    # Task 2
    s = input()
    check_string(s)

    # Task 3
    task3()

    # Task 4
    n = int(input())
    print(sum_even(n))