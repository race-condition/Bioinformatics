def fib(n,k):
    fib_table=[]
    for i in range(n):
        if i<2:
            fib_table.append(1)
        else:
            fib_table.append(fib_table[-1]+fib_table[-2]*k)
    return fib_table[-1]
