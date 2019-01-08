# python3

import sys
#input = sys.stdin.readline()
n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = []

for i in range(n):
    parent.append([i,-1])
ans = max(lines)

def getParent(index):
    # find parent and compress pat
    while( parent[index][1] != -1 ):
        new = parent[index][1]
        if(parent[new][1] == -1 ):
            return parent[index][1]
        else:
            index = new
    return -1

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    #print(realDestination,realSource , "Passed",destination,source)
    if realDestination == realSource and realDestination != -1:
        return 

    else:
        if(realDestination == -1):
            realDestination = destination

        if(realSource == -1 ):
            realSource = source
        
        if(realDestination == realSource):
            return

        #print(lines)
        lines[realDestination]+=lines[realSource]
        
        lines[realSource] = 0
        #print(lines)
        parent[realSource][1] = realDestination
        #print(parent)

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(max(lines))
    
