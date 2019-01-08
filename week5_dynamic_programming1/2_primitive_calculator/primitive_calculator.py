# Uses python3
import sys
sys.setrecursionlimit(1000000)
count1=0
def dp_sequence(n,d):
    global count1
    count1+=1
    if(n==1):
        return 0
    else:
        if( n in d.keys() ):
            return d[n]

        else:
            n2 = 9999999999
            n3 = 9999999999
            if(n%3 ==0 ):
                if(n//3 in d.keys()):
                    n3 = d[n//3]
                else:
                    n3 = dp_sequence(n//3,d)
            if(n%2==0):
                if(n//2 in d.keys()):
                    n2 = d[n//2]
                else:
                    n2 = dp_sequence(n//2,d)
            if(n-1 in d.keys()):
                n1 = d[n-1]
            else:
                n1 = dp_sequence(n-1,d)
            d[n] = min(n1,n2,n3)+1
            return d[n]

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

#input = sys.stdin.read()
n = int(input())

d = dict()
d[1] = 0
d[0] = 0

sequence = (dp_sequence(n,d))
#print(len(sequence) - 1)
'''for x in sequence:
    print(x, end=' ')'''
#print(d)
print(sequence)
print(count1)
 
