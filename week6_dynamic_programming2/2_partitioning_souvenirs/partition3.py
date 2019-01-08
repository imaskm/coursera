# Uses python3
import sys
import itertools


def part3(A,n,s1,s2,s3):
    
    if(s1==0 and  s2==0 and s3 == 0):
        return 1
    '''if(n==0):
        return 0'''

    a1 = 0
    
    if(s1- A[n-1] >= 0):

        a1 = part3(A,n-1,s1-A[n-1],s2,s3)


    a2 = 0

    if(a1!=1 and s2 - A[n-1] >= 0):
        a2 = part3(A,n-1,s1,s2-A[n-1],s3)

    a3 = 0

    if(a2!=1 and s3-A[n-1] >= 0 ):
        a3 = part3(A,n-1,s1,s2,s3-A[n-1])


    if( a1==1 or a2==1 or a3==1 ):
        return 1
    else:
        return 0



    


'''def partition3(A):
    res =itertools.product(range(3), repeat=len(A))
    print(list(res))
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0'''

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    s = sum(A)
    if(s%3 != 0):
        print(0)
    else:
        print(part3(A,n,s//3,s//3,s//3))

