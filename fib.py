
dict = {}
dict[0]=0
dict[1]=1

def fib(x):
    
    if x in dict:
        return dict[x]
            
    else:
        dict[x] = fib(x-1) + fib(x-2)     
        return dict[x]

print fib(input())
    
