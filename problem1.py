def remove_duplicates(x):
  '''
  list->list
  takes in a list with possibly repeating elements and returns a new list containing only unique items in the list, maintaining order of elements
 
  >>> remove_duplicates([63,67,27,25,63,8])
  [63,67,27,25,8]
  >>> remove_duplicates([1,1,1,1])
  [1]
  '''
  doubles= []
  for i in x:
