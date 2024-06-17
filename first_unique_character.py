# Online Python-3 Compiler (Interpreter)
def first_unique_character(s):
    n = len(s)
    s = s.lower()
    counts = {}
    
    for c in s:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
            
    for i in range(len(s)):
        if counts[s[i]] == 1:
            return i
    return -1        

if __name__ == '__main__':
    for s in ['Appsilon', 'Appsilon Poland', 'abcabc']:
        print(f"Index: {first_unique_character(s=s)}")
