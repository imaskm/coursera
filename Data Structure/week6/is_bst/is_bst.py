#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def isBST(tree,mini,maxi,root):

    if(root == -1):
        return True
    if(  tree[root][0] < mini or tree[root][0] > maxi ):
        #print( tree[root][0] , "index",root,"mini",mini,"maxi",maxi )
        #if( tree[root][1] != -1 and tree[root][2] != -1 ):
        #print("Here",tree[root][0],mini,maxi)
        return False

    if(tree[root][1] == -1 and tree[root][2] == -1 ):
        return True
    
        

    return isBST(tree,mini,tree[root][0]-1,tree[root][1]) and isBST(tree,tree[root][0]+1,maxi,tree[root][2])
    #if(x == False):
    #print(tree[root][0] , root)
    #return x

'''def IsBinarySearchTree(tree):


    # Implement correct algorithm here
    root= 0
    return ( isBST(tree, -99999999999999, 999999999999999 , root )) 
	
    for i in range(len(tree)):

    if( i ==0  ):
        left = tree[i][0]
        right = tree[i][0]

      
    if( tree[i][1] != -1 and ( tree[i][0] <= tree[ tree[i][1] ][0]  ) ):
        return False

            
    if( tree[i][2] != -1 and ( tree[i][0] >= tree[ tree[i][2] ][0]  ) ):
        return False
    
    print("left",left," right :",right)
    return True'''


def main():
  nodes = int(sys.stdin.readline().strip())
  if(nodes == 0):
      print("CORRECT")
      return
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if isBST(tree,-99999999999,999999999999,0):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
