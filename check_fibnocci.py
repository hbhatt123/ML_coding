# Python 3 program to find the ones in
# a given sorted array

# if x is present in arr[] then
# returns the index of FIRST
# occurrence of x in arr[0..n-1],
# otherwise returns -1
def Fibnocci(n):
    if n < 0:
        return -1
    elif n ==0:
        return 0
        
    elif n==1 or n==2:
        return 1
    else:
        return Fibnocci(n-1) + Fibnocci(n-2)
    
      
    

    
if __name__ =='__main__':    
    # Driver program
    ls = [100, 180, 260, 310, 40, 535, 695]
    res = Fibnocci(10)
    print("ans", res)
    
