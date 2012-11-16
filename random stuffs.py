def next_pali(mag):
    '''
    Increment down for mag series (e.g. 98889 -> 97779)
    UGLY!
    Still have to check we aren't at something like 90009 
    because we get a situation like:
      >>> 98889 + t(5)
      97779
      >>> 90009 + t(5)
      88899
    '''
    return -int('1'*(mag-2)+'0')