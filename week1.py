# Create lower triangular, upper triangular and pyramid containing the "*" character.
n=4
# lower traingle
for i in range (0,n):
    for j in range(0,i):
        print("*",end=" ")
    print('\n')
    
# upper traingle
for i in range(n):
  for j in range(n):
    if j >= i: 
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print('\n')   

# pyramid
for i in range(n):
  
  for j in range(n - i - 1):
    print(" ", end="")
  for j in range(2 * i + 1): 
    print("*", end="")
  print()