def fib_iter(n):
    a,b = 0,1
    
    for i in range(n):
        a,b = b, a+b
        
    return a
    
print(fib_iter(10))

def fib_recursive(n):
        if n == 0 or n == 1:
                return n
                
        return fib_recursive(n-1) + fib_recursive(n-2)
        
print(fib_recursive(11))

n = 12
cache = [None] *(n+1)

def fib_dynamic(n):
        if n == 0 or n == 1:
                return n
        
        if cache[n] != None:
                return cache[n]
        
        cache[n] = fib_dynamic(n-1) + fib_dynamic(n-2)
        
        return cache[n]
        
print(fib_dynamic(12))