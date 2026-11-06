def remove_duplicates(x):
    """
    list->list
    takes in a list with possibly repeating elements and returns a new list containing only unique items in the list, maintaining order of elements
 
    >>> remove_duplicates([63,67,27,25,63,8])
    [63, 67, 27, 25, 8]
    >>> remove_duplicates([1,1,1,1])
    [1]
    >>> remove_duplicates([2,4,6,6,8])
    [2, 4, 6, 6, 8]
    >>> remove_duplicates([1,1,5,6,7])
    [1, 5, 6, 7]
    """
    result =[]
    for i in x:
        if i not in result:
            result.append(i)
    return result
