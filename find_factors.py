def prod(target, mag):
    '''
    Uses a squeeze algorithm to find factors
    that may yield a given product. 
    '''
    high = 10**mag - 1
    low = 10**(mag - 1)
    while 1:
        if high < 10**(mag-1) or low > 10**mag - 1:
            high, low = 0, 0
            break
        elif high * low < target:
            low += 1
        elif high * low > target:
            high -= 1
        elif high * low == target:
            break
    return (high, low)