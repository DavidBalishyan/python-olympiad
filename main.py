import random
import math

n: int = int(input("Enter count: "))
arr: list = []

for i in range(n):
    arr.append(math.floor(random.random() * 100))

print(arr)

