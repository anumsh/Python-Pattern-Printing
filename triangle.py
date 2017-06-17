def triangle(n):
  for row in range(0,n):
    for col in range(0,n-row-1):
       print(" ")
    for col in range(0,row+1):
       print("*")
  print()
  
  
  
  
  
print triangle(5)
