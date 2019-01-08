# Uses python3
def calc_fib(n,fib):
    if (n in fib.keys() ):
        return fib[n]
    fib[n] = calc_fib(n-2,fib) + calc_fib(n-1,fib)
    return fib[n]
n = int(input())
fib={0:0,1:1}
print(calc_fib(n,fib))
