def count_vowels(x):
  """
  string -> number
  counts the number of vowels in a given character string, only counting "a","e","i","o","u" as vowels
  
  >>> count_vowels("my name is Earl")
  5
  >>> count_vowels("hello world")
  3
  >>> count_vowels("i ate lunch today")
  6
  """
  return len([i for i in x if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U")])
  count_vowels("madison")
