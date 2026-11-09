def merge(x,y):
  '''
  list,list->list
  takes two sorted lists and returns new list contain all elements in the two lists in sorted order

  >>> merge([1,2,3,4],[5,6])
  [1, 2, 3, 4, 5, 6]
  >>> merge([1,3,6],[2,3,5])
  [1, 2, 3, 3, 5, 6]
  >>> merge([4,6,7,9],[2,3,8])
  [2, 3, 4, 6, 7, 8, 9] 
  >>> merge([1,5,9],[8,7,3])
  [1, 3, 5, 7, 8, 9])
  '''
  result=[]
  while len(x) > 0 and len(y)> 0:
    if x[0] <= y[0]:
        result.append(x[0])
        x = x[1:]
    else:
        result.append(y[0])
        y= y[1:]
  for item in x:
      result.append(item)
  for item in y:
      result.append(item)
  return result
