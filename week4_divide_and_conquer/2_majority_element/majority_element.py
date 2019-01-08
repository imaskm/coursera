# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    a.sort()
    #print(a)
    maj = right/2
    #print(maj)
    c =1
    while(left <= right-2):
        if(a[left] == a[left+1]):
            c+=1
            if(c>maj):
                
                return 1
        else:
            c=1
        left+=1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
