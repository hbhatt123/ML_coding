# Online Python-3 Compiler (Interpreter)
def defang_ip_address(ip):
    
    ip1 = ip.split('.')
    print(ip1)
    return '[.]'.join(ip1)
    
   

if __name__ == '__main__':
    ip = '1.0.0.0'
    print(defang_ip_address(ip))
