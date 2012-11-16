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
        elif high * low < target:
            low += 1
        elif high * low > target:
            high -= 1
        elif high * low == target:
            break
    return (high, low)