# Uses python3
import sys

def get_change(m):
    #write your code here
    ten = m//10
    x =m%10
    five = (x)//5
    one = x%5

    return ten+five+one

if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m=int(input())
    print(get_change(m))
