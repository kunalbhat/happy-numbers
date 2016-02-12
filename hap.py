# Find Happy Numbers by known terminating integer (4)
# https://en.wikipedia.org/wiki/Happy_number

def is_happy(n):
    if n == 1:
        return True
    elif n == 4:
        return False
    else:
        digits_squared = sum(int(ch) ** 2 for ch in str(n))
        return is_happy(digits_squared)

# Happy Numbers (e.g. 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68...)
print(is_happy(32)) # True
