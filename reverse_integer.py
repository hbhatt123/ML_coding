# Online Python-3 Compiler (Interpreter)
def reverse_integer(x):
    assert -21**31 < x < 21**31 -1, 'invalid number range'
    
    is_negative = True if x<0 else False
    if is_negative:
        x = x * -1
        
    # removed trailing zeros
    x_rstripped = int(str(x).rstrip('0'))
    print("**", x_rstripped)
    
    x_reversed = 0
    x = str(x_rstripped)
    c = []
    print(len(x))
    for s in range(len(x)-1,-1,-1):
        c.append(str(x[s]))
    c = ''.join(c)
    print("reverse,integer = ", c)
        
    # for a in str(x_rstripped):
    #     print(a)
        
    # while(x_rstripped > 0):
    #     a = x_rstripped % 10
    #     print("a =",a, "stripped = ", x_rstripped)
    #     x_reversed = x_reversed * 10 + a
    #     print(x_reversed)
    #     x_rstripped = x_rstripped // 10
    
    # Check if the input number was negative
    if is_negative:
        return -c
    return c



if __name__ == '__main__':
   for x in [120,12001]:
    print(f"IntReversed({x}) = {reverse_integer(x=x)}")
