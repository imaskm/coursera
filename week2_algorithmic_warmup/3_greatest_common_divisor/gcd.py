# Uses python3
import sys

def gcd_eff(a, b):
    if(b==0):
        return a
    else:
        return gcd_eff(b,a%b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_eff(a, b))
