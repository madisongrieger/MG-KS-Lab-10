def square(x):
    """
    list -> list
    takes a list and returns a list of all numbers squared
    
    >>> square([1,-1,9,3.1])
    [1,1,81,9.610000000000001]
    """
    return [i**2 for i in x]
    
