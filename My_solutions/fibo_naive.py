
def fibbo(n,fib):
    if( n in fib.keys() ):
        return fib[n]

    else:
        fib[n]=  fibbo(n-1,fib)+fibbo(n-2,fib)
        return fib[n]



if __name__ == '__main__':

    n = int(input("Enter a integer"))
    fib = {0:0,1:1}
    print(fibbo(n,fib))
    print(fib)
