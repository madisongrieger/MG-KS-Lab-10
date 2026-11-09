def square(x):
    """
    list -> list
    takes a list and returns a list of all numbers squared
    
    >>> square([1,-1,9,3.1])
    [1, 1, 81, 9.610000000000001]
    >>> square([3,4,5,6])
    [9, 16, 5, 6]
    >>>square([1,2,7,8])
    [1,4,49,64]
    """
    return [i**2 for i in x]
