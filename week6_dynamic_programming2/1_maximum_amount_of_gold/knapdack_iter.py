# Uses python3
import sys

def optimal_weight(W, w):
    dp=[]
    for i in range(len(w)+1):
        dp.append([])
        for j in range(W+1):
            dp[i].append(0)
    flag=False
    if(W<w[0]):
        return 0
    #print(dp)
    for i in range(1,len(w)+1):
        
        for j in range(1,W+1):

            if(j == w[i-1] ):
                dp[i][j] = max( w[i-1]+dp[i][j-w[i-1]],dp[i-1][j])
            elif(j >  w[i-1] ):

                dp[i][j] = max(w[i-1]+ dp[i-1][ j-w[i-1] ],dp[i-1][j])
            else:
                dp[i][j] = max( dp[i][j-1],dp[i-1][j])


            
    

    '''for i in range(len(w)+1):
        print(dp[i])'''


    return dp[len(w)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    w.sort()
    print(optimal_weight(W, w))

