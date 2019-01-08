# Uses python3
import sys

def gcd_eff(a, b):
    if(b==0):
        return a
    else:
        return gcd_eff(b,a%b)

def lcm_eff(a, b):

    return (a*b)//gcd_eff(a,b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_eff(a, b))

