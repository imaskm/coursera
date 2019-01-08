#Uses python3

import sys

def lcs2(a, b,n,m,dp):

    if(n==0 or m==0 ):
        return 0

    if(dp[n-1][m-1] is not None):
        return dp[n-1][m-1]
    else:

        if( a[n-1] == b[m-1] ):
            dp[n-1][m-1]= lcs2(a,b,n-1,m-1,dp)+1
            return dp[n-1][m-1]
        else:
            dp[n-1][m-1] = max( lcs2(a,b,n-1,m,dp) ,lcs2(a,b,n,m-1,dp) )
            return dp[n-1][m-1]

    #write your code here
    #return min(len(a), len(b))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    dp=[]

    for i in range(n):
        dp.append([])
        for j in range(m):
            dp[i].append(None)

    print(lcs2(a, b,n,m,dp))
