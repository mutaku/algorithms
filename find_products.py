def prod(target, mag):
    high = 10**mag - 1
    low = 10**(mag - 1)
    while 1:
        if high * low < target:
            low += 1
        elif high * low > target:
            high -= 1
        elif high * low == target:
            break
    return (high, low)