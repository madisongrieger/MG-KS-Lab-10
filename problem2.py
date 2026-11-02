def merge(x,y):
  '''
  list,list->list
  takes two sorted lists and returns new list contain all elements in the two lists in sorted order

  >>> merge([1,2,3,4],[5,6])
  [1,2,3,4,5,6]
  >>> merge([1,3,6],[2,3,5])
  [1,2,3,3,5,6]
  '''
  result=[]
  while (len(x)<0 and len(y)<0):
    minimum=min(x[0],y[0])
    result.append(minimum)
    if minimum==x[0]:
      x=x[1:]
      
