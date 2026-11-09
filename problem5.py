def rotate_by_n(x,n):
  '''
  list->list
  takes in a list and a number n ans returns a list with each value shifted down n positions

  >>> rotate_by_n([1,2,3,4],3)
  [2, 3, 4, 1]
  >>> rotate_by_n([1,2,3,4],1)
  [4, 1, 2, 3]
  >>> rotate_by_n([10, 20, 30, 40, 50],2)
  [40, 50, 10, 20, 30]
  >>> rotate_by_n([-1,-2,-3],2)
  [-3, -1, -2]
  '''
  result=[]
  for i in x:
    result.append(i)
  for i in range(n):
    result = [result[-1]+result[:-1]]
  return result 
