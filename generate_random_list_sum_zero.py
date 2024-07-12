N=4
l = random.sample(range(-10, 10), k=3)
print(l)
print(l + [-sum(l)])

def sumzero(n):
    
    ls = []
    sum = 0
    ls = [ i for i in range(1,n//2+1)] # generate half of N numberes
    ls += [-i for i in ls] # generate half of opposite sign numbers
    print(ls)
    return ls if n%2 ==0 else ls + [0]  return list if N is even otherwise add 0 to the list(in odd)
