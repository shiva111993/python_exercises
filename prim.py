import os
os.system('cls')
to = 100
result = 0
for x in range(2, 1000):
    for i in range(2, x):
      if x%i ==0:
          result = 0
          break
      else:
          result = 1 
    if result == 1:
        print(x)