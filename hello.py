for i in [1,2,3]:
    print i
    for j in [1,2,3]:
        print j
        print 'i '+str(i)+' j '+str(j)
print "done"    


def square(x):
    print x*x

square(5)


def fib(x):
    if x<=0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

print fib(input())
