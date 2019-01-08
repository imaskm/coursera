# Uses python3
import sys


def get_change(m,d):
    #write your code here
    if(m==0):
        return 0

    elif(m<0):
        return 9999999

    if(m in d.keys() ):
        return d[m]
    else:
        c1 = get_change(m-1,d)+1
        c2 = get_change(m-3,d)+1
        c3 = get_change(m-4,d)+1
        d[m] = min(c1,c2,c3)
        return d[m]




    #return m // 4

if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m=int(input())
    d= dict()
    d[1]=1
    d[3]=1
    d[4]=1
    print(get_change(m,d))
    print(len(d))
