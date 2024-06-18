# Python 3 program to find the ones in
# a given sorted array

# if x is present in arr[] then
# returns the index of FIRST
# occurrence of x in arr[0..n-1],
# otherwise returns -1
def max_subaray(ls):
    n = len(ls)
    max_sum = -10000000000
    cur_sum = 0
    s = 0
    start = 0
    end = 0
    for i in range(n):
        cur_sum += ls[i]
        if max_sum < cur_sum:
            max_sum = cur_sum
            start = s
            end = i
        if cur_sum < 0:
            cur_sum = 0
            s = s+1
            
    return max_sum , start, end       
    

    
if __name__ =='__main__':    
    # Driver program
    ls = [-2, -3, 4, -1, -2, 1, 5, -3]
    res = max_subaray(ls)
    print("ans", res)
    
