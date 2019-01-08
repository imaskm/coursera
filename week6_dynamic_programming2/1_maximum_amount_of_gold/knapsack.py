# Uses python3
import sys

def optimal_weight(W, w,d):
    # write your code here
    '''result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result'''
    if(W==0 or len(w)==0 ):
        return 0
    if(w[-1] in d.keys()  ):
        return d[w[-1]]
    
    if(w[-1] > W):
        return optimal_weight(W, w[:-1],d)
        
    else:
        d[w[-1]] =  max( ( w[-1]+optimal_weight(W-w[-1], w[:-1],d) ), optimal_weight(W, w[:-1],d)  )
        return d[w[-1]]
        




if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    d=dict()
    print(optimal_weight(W, w,d))
