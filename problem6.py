def closest(x,n):
  '''
  list -> list
  takes in a list of numbers and a number, n, and returns the single value in the list closet to that number

  >>> closest([1,2,3,4,5],2.1)
  2
  >>> closest([6.7,8,13],7)
  6.7
  '''
  closest_num= x[0]
  for num in x:
    if (num-n if num>n else 
    
