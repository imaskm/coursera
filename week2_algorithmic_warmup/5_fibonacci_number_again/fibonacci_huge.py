# Uses python3
import sys
# Uses python3
def calc_fib(n,fib):
    if (n in fib.keys() ):
        return fib[n]
    fib[n] = calc_fib(n-2,fib) + calc_fib(n-1,fib)
    return fib[n]


if __name__ == '__main__':
    #input = sys.stdin.read();
    n, m = map(int, input().split())
    n=n%(m*m-1)
    print(n)
    fib={0:0,1:1}
    print(calc_fib(n,fib)%m)
