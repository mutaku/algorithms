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

from math import sqrt

def get_pali(digits, limit_digits=True, square_sieve=True):
    '''
    Finds the maximum numerical palindrome for
    n-digits*n-digits.
    '''
    max_pali = None
    mag = digits * 2 # magnitude of product
    start = 10**mag - 1
    counter = start
    # Cut the number into symmetrical elements
    # we will then flip to make palindromes
    symmetry = int(str(start)[:mag / 2])
    # We set limit_digits if we want to ensure
    # factors have to have no less than n digits
    if limit_digits:
        stop = 10**(mag - 1)
    else:
        stop = 0
    # assign our desired factorization function
    # sqrt is fastest and will find only n-digit factors
    # the other version is slower but can potentially
    # find all factors as well as any primes
    if square_sieve:
        factorization = factors_sqrt
    else:
        factorization = factors
    while counter >= stop:
        # If we have even magnitude our sequence
        # is symmetrical and we just flip
        if mag % 2 == 0:
            # make palindrome by flipping first half
            # and joining together with string slicing
            # and then convert back to integer
            num = int(str(symmetry)+str(symmetry)[::-1])
            # check to see if we can make this
            # from our possible factors of n digits
            to_make = factorization(num)
            if to_make != (0, 0):
                max_pali = (to_make, num)
                # we've found a possible palindrome
                # since we are working top down, we
                # know this is the maximum possible
                # so we break out of the loop
                break
        else:
            # since we are not symmetrical, we have a
            # digit in the middle that can change and
            # we need to iterate over it's 10 possible
            # values working down from 9 to 0 with each
            # part of the first half symmetry we test
            for i in range(9, -1, -1):
                num = int(str(symmetry)+str(i)+str(symmetry)[::-1])
                # check to see if we can make this
                # from our possible factors of n digits
                to_make = factorization(num)
                if to_make != (0, 0):
                    max_pali = (to_make, num)
                    # we've found a possible palindrome
                    # since we are working top down, we
                    # know this is the maximum possible
                    # so we break out of the loop
                    break
        # increment down the couter so that we can stop
        # when we hit our stop point we've set by digits
        counter -= 1
        # increment down the first half symmetry component
        # that we are generating the palindromes with
        # 9889 has symmetry of 98 and will now be 97 to
        # give us a palindrome next loop of 9779
        symmetry -= 1
    # return our palindrome if we have it in the form of
    # ((factor high, factor low), palindrome)
    return max_pali

def factors(target, full_range=False, inclusive=False):
    '''
    Uses a squeeze algorithm to find factors
    that may yield a given product. We are not
    identifying multiple possible factor sets, we
    only car if we can find at least one set to
    yield the target product.
    '''
    # set our max and minimum values
    # e.g. 3 digit factors would be
    # 999-100 based on mag=3
    # we can set full range to be all inclusive
    # from 0 to mag to use this as a more generic
    # factorization
    mag = len(str(target)) / 2
    if full_range:
        start_low = 0
        start_high = target
    else:
        start_low = 10**(mag - 1)
        start_high = 10**mag - 1
    # get symmetry (half way point) of our
    # target product
    symmetry = start_low * 2
    # set our squeeze factors to the
    # high and low start points
    high, low = start_high, start_low
    # setup a container for all the possible
    # factors if we want inclusivity
    if inclusive:
        factor_list = []
    while 1:
        # if our target is greater than the square
        # of the highest possible factor, we cannot
        # make this product and break
        if high**2 < target:
            high, low = 0, 0
            break
        # if high and low iterators hit the
        # symmetry point, we can't make product
        # and going further is operating on factors
        # we've already tried with opposite
        # symmetry so we break
        elif high <= symmetry and low >= symmetry:
            high, low = 0, 0
            break
        # if we are less than the product, we need
        # to increase the low squeeze factor
        elif high * low < target:
            low += 1
        # if we are greater than the product, we
        # need to decrease the high squeeze factor
        elif high * low > target:
            high -= 1
        # if we've hit the target, break
        elif high * low == target:
            if inclusive:
                factor_list.append((high, low))
                high -= 1
                low += 1
            else:
                break
    # return our squeeze factors
    if inclusive:
        return factor_list
    return (high, low)

def factors_sqrt(target):
    '''
    Uses sqrt sieving to find factors
    of target
    '''
    # find our sqrt symmetry point and
    # since we want integers we round and
    # use the integer form of this value
    symmetry = int(round(sqrt(target)))
    mag = len(str(target))
    factor_ceiling = 10**(mag / 2) - 1
    factor_floor = 10**(mag / 2 - 1)
    high, low = symmetry, symmetry
    while 1:
        if factor_ceiling**2 < target:
            high, low = 0, 0
            break
        elif high < factor_floor or low < factor_floor:
            high, low = 0, 0
            break
        elif high > factor_ceiling or low > factor_ceiling:
            high, low = 0, 0
            break
        elif high * low < target:
            low += 1
        elif high * low > target:
            high -= 1
        elif high * low == target:
            break
    return (high, low)
