 def closest(x,n):
  '''
  list -> list
  takes in a list of numbers and a number, n, and returns the single value in the list closet to that number

  >>> closest([1,2,3,4,5],2.1)
  2
  >>> closest([6.7,8,13],7)
  6.7
  >>> closest([12,5,1],11)
  12
  >>>closest([2,7,10,15],3)
  2
  '''
  closest_num= x[0]
  for num in x:
    distance1= num-n if num> n else n-num
    distance2= closest_num -n if closest_num > n else n- closest_num
    if distance1 < distance2:
      closest_num = num
  return closest_num
