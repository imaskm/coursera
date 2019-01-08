# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
      self.result = []
      current = 0
      list1 = []
      while True:
          if current != -1:
              list1.append(current)
              current = self.left[current]
          elif list1:
              current = list1.pop()
              self.result.append(self.key[current])
              current = self.right[current]
          else:
              break
      return self.result

  def preOrder(self):
      self.result = []
      current = 0
      list1 = []
      while True:
          if current != -1:
              self.result.append(self.key[current])
              list1.append(current)
              current = self.left[current]
          elif list1:
              current = list1.pop()
              current = self.right[current]
          else:
              break
      return self.result

  def postOrder(self):
      self.result = []
      list1 = [0]
      list2 = []
      while list1:
          current = list1.pop()
          list2.append(self.key[current])

          left = self.left[current]
          right = self.right[current]
          if left != -1:
              list1.append(left)
          if right != -1:
              list1.append(right)

      while list2:
          self.result.append(list2.pop())
      return self.result
def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
