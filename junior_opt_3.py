import random

# Task 1: Arithmetic operations on list
def task1():
    a = int(input())
    b = int(input())
    c = int(input())
    lst = [a, b, c]
    lst[1] = int(str(lst[1]) + '4')  # Append 4 to second element
    max_elem = max(lst)
    average = sum(lst) / len(lst)
    print(lst)
    print(f"Ամենամեծ տարրը {max_elem}֊ն է։")
    print(f"Ցուցակի թվաբանական միջինը {int(average)}֊ն է։")

# Task 2: Conditional operators for string
def check_string(s):
    if len(s) > 10:
        print("Տողի երկարությունը մեծ է 10֊ից։")
    elif '#' in s:
        print("Տողի երկարությունը 10֊ից երկար չէ և պարունակում է # սիմվոլը։")
    else:
        print("Տողի երկարությունը 10֊ից երկար չէ և չի պարունակում # սիմվոլը։")

# Task 3: Tuple, loop, random
def task3():
    n = int(input())
    numbers = [random.randint(1, 100) for _ in range(n)]
    doubled = tuple(x * 2 for x in numbers)
    has_duplicates = len(set(doubled)) < len(doubled)
    print("Tuple has duplicates" if has_duplicates else "No duplicates")
    m = int(input())
    if doubled[0] < m:
        print("YES")
    odds = [x for x in doubled if x % 2 != 0]
    odd_sum = sum(odds)
    print(odd_sum)

# Task 4: Recursive function
def sum_k(n):
    if n == 0:
        return 0
    return n + sum_k(n - 1)

def sum_expression(n):
    return n * sum_k(n)

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
    print(sum_expression(n))