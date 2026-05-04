import random

# Task 1: Arithmetic operations on list
def task1():
    a = int(input())
    b = int(input())
    c = int(input())
    lst = [a, b, c]
    new_lst = [lst[0] * 3, lst[1] / 2, lst[2] ** 2]
    print(new_lst)

# Task 2: Conditional operators
def check_number(num):
    if num % 7 == 0:
        print("Թիվը բաժանվում է 7-ի։")
    elif num % 3 == 0:
        print("Թիվը բաժանվում է 3-ի, բայց ոչ 7-ի։")
    else:
        print("Թիվը ո՛չ 3-ի, ո՛չ 7-ի չի բաժանվում։")

# Task 3: Tuple, loop, random
def task3():
    n = int(input())
    numbers = tuple(random.randint(1, 100) for _ in range(n))
    m = int(input())
    if m in numbers:
        print("YES")
    evens = [x for x in numbers if x % 2 == 0]
    if evens:
        even_sum = sum(evens)
        even_avg = even_sum / len(evens)
        print(even_sum)
        print(even_avg)
    else:
        print(0)
        print(0)

# Task 4: Recursive function
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
    num = int(input())
    check_number(num)

    # Task 3
    task3()

    # Task 4
    n = int(input())
    print(sum_even(n))