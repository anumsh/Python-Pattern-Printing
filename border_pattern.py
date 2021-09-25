def borderPattern(size):
  size = 5
  inner_size = size - 2
  print ('* ' * size)
  for i in range(inner_size):
    print ('*' + '  ' * ((2*size-3)) + '*')
  print ('* ' * size)
  
      
print borderPattern(5)

"""
output:

* * * * *
*       *
*       *
*       *
* * * * *
"""
