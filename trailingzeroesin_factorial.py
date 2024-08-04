def factorial(n):
  if n == 0 or n==1:
    return 1
  else:
    for i in range(n):
      return n*factorial(n-1)
    
def trailing_zeroes(n): # O(n)
  fact = factorial(n)
  print(fact)
  a = str(fact)
  a = a[::-1]
  count = 0
  for i in a:
    if i !='0':
      break
    else:
      print("i",i)
      count += 1
  return count    
  
def findTrailingZeros(n): O(logn)
    count = 0
    i = 5
    while n/i >= 1:
        count += int(n/i)
        i *= 5
        print(i,count)
    return count
print(findTrailingZeros(3))    
print(trailing_zeroes(25)) 
  
