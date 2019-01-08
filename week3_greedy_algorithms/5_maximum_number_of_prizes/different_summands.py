# Uses python3
import sys,math

def optimal_summands(n):
    summands = []
    #write your code here
    a=1
    b=1
    c=-2*n
    d = math.sqrt( (b*b)-4*(a*c) )
    
    r1 = (-b+d)//2
    r2 = (-b-d)//2

    if(r1>0):
        r=int(r1)
    else:
        r=int(r2)

    #print(r)

    s=0
    for i in range(1,r):
        s+=i
        summands.append(i)

    summands.append(n-s)

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
