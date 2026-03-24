# Solutions for python olympiad

***This olymiad is held by DIGI.code() in Armenia***

---

## opt. 1

### Task 1
- Uses a list comprehension + `count()` to keep values appearing exactly once.
- Result sorted with `sorted()` to match expected output.

### Task 2
- `gcd(a, b)`: Euclidean algorithm. If `b == 0` return `a`, else recurse `gcd(b, a % b)`.
- `digit_sum(n)`: adds `n % 10` and recurses on `n // 10` until a single digit remains.

### Task 3
- `write_to_file()`: collect 5 lines and write to `string.txt`.
- `find_longest_word()`: reads `string.txt`, splits words, selects longest with `max(words, key=len)`.

### Task 4
- `Rectangle`: stores `width`, `height`; methods `surface()`, `perimeter()`.
- `Square(Rectangle)`: `super().__init__(side, side)` avoids duplicate logic.

---

## opt. 2

### Task 1
- reads 5 words into a list.
- filters with `[w for w in all_words if len(w) > 4]`.
- drops `kiwi` (length 4), keeps expected output semantics.

### Task 2
- `is_prime(n, divisor=2)`: recursive divisor trial until `divisor**2 > n` (prime) or divides evenly.
- `is_palindrome(s)`: compare `s[0] == s[-1]`, recurse on `s[1:-1]`.

### Task 3
- `write_numbers()`: store 10 user numbers in `numbers.txt` (one line each).
- `calculate_average()`: read numbers, `sum(values)/len(values)`.

### Task 4
- `Circle`: `surface` = `math.pi * r**2`, `length` = `2 * math.pi * r`.
- `Square`: `surface` = `side**2`, `perimeter` = `4 * side`.

---

## opt. 3

### Task 1
- routes input to `even_numbers` or `odd_numbers` with `num % 2`.

### Task 2
- `to_binary(n)`: recursion with base `0`/`1`, compute `to_binary(n//2) + str(n%2)`.
- `list_sum(lst)`: base `[]` returns `0`; otherwise `lst[0] + list_sum(lst[1:])`.

### Task 3
- `write_user()`: saves `firstname`, `lastname`, `birth_year` to `user.txt`.
- `print_age()`: reads birth year line, computes `2025 - birth_year`.

### Task 4
- `EqTriangle`: private `__side`, area `(sqrt(3)/4) * a**2`, perimeter `3*a`.
- `RightTriangle`: private `__leg1`, `__leg2`, area `(leg1*leg2)/2`, perimeter includes `sqrt(leg1**2 + leg2**2)`.

---

## opt. 4

### Task 1
- map `students[name] = age`.
- find youngest with `min(students.values())`, handles ties.

### Task 2
- `reverse_string(s)`: recursion `s[0] + reverse_string(s[1:])` until final char.
- `list_product(lst)`: product recursion with base `1`.

### Task 3
- `write_text()`: saves a string into `text.txt`.
- `find_most_frequent()`: normalize, count words, gather top frequency, write to `count.txt`.

### Task 4
- `Hexagon`: side `__side`, area `(3*sqrt(3)/2) * a**2`, perimeter `6*a`.
- `Square`: side `__side`, area `side**2`, diagonal `side * sqrt(2)`.

---

## Notes
- keep this README as a concise reference; use the corresponding `opt_*.py` scripts for code details.
- all major algorithms are explained in plain phrasing with code snippets where helpful.
