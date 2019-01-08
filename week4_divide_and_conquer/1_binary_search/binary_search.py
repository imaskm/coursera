# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here
    
    while(left<len(a) and right>=0 and left <= right):
        mid = (left+right)//2
        if(a[mid] == x):
            return mid
        elif( x > a[mid]):
            left=mid+1
        else:
            right = mid-1
    return -1

'''def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1
'''
if __name__ == '__main__':
    #input = sys.stdin.read()
    data = list(map(int, input().split()))
    n = data[0]
    a = data[1 : n + 1]
    data1 = list(map(int, input().split()))
    
    for x in data1[1:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
