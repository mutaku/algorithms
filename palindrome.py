##############
# Numerical
# Palindromes
##############

from time import time

def is_pali(num):
    return str(num) == str(num)[::-1]

def get_max_pali(mag):
    start = 10**mag - 1
    end = 10**(mag - 1)
    symmetry = 10**mag / 2
    palindrome = [0, 0, 0]
    begin_time = time()
    for x in range(start, symmetry, -1):
        for y in range(start, end, -1):
            prod = x * y
            if is_pali(prod) and prod > palindrome[2]:
                palindrome = [x, y, prod]
                break
    end_time = time()
    complete_time = end_time - begin_time
    return palindrome, complete_time
