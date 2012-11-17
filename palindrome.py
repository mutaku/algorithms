#########################################
# Find the maximum numerical palindrome
# product from multiplying together two
# factors of a certain magnitude
#
# e.g. What is the maximum palindromic 
# product for 4digit x 4digit?
#
# >>> palindrome.get_pali(4)
# ((9999, 9901), '99000099')
#
# So the maximum palindromic product for
# 4digit*4digit is 99000099 yielded by
# 9999*9901.
#
#    - Matthew Martz 2012
#########################################

def gen_pali(digits, limit_digits=True):
    '''
    Makes palindromes and tries to see if we can
    find factors to create it.
    '''
    max_pali = None
    mag = digits * 2
    start = 10**mag - 1
    counter = start
    print start, digits
    symmetry = int(str(start)[:mag / 2])
    if limit_digits:
        stop = 10**(mag - 1)
    else:
        stop = 0
    while counter >= stop:
        if mag % 2 == 0:
            num = str(symmetry)+str(symmetry)[::-1]
            if is_pali(num):
                to_make = factors(int(num), digits)
                if to_make != (0, 0):
                    max_pali = (to_make, num)
                    break
        else:
            for i in range(9, -1, -1):
                num = str(symmetry)+str(i)+str(symmetry)[::-1]
                if is_pali(num):
                    to_make = factors(int(num), digits)
                    if to_make != (0, 0):
                        max_pali = (to_make, num)
                        break
        counter -= 1
        symmetry -= 1
    return max_pali

def is_pali(num):
    '''
    Determines if number is palindromic.
    '''
    return str(num) == str(num)[::-1]

def factors(target, mag):
    '''
    Uses a squeeze algorithm to find factors
    that may yield a given product.
    '''
    start_high = 10**mag - 1
    start_low = 10**(mag - 1)
    symmetry = start_low * 2
    high, low = start_high, start_low
    while 1:
        if high <= symmetry and low >= symmetry:
            high, low = 0, 0
            break
        elif high**2 < target:
            high, low = 0, 0
            break
        elif high * low < target:
            low += 1
        elif high * low > target:
            high -= 1
        elif high * low == target:
            break
    return (high, low)