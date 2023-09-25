import sys
sys.setrecursionlimit(10 ** 9)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    def addNode(self, node):
        if not self.root:
            self.root = node
        else:
            tmp = self.root
            while tmp:
                if tmp.data < node.data:
                    if not tmp.right:
                        break
                    tmp = tmp.right
                elif tmp.data > node.data:
                    if not tmp.left: 
                        break
                    tmp = tmp.left
            if not tmp:
                return
            if tmp.data < node.data:
                tmp.right = node
            else:
                tmp.left = node
    def traverse(self):
        self.dfs(self.root)
    
    def dfs(self, node):
        if node.left:
            self.dfs(node.left)
        if node.right:
            self.dfs(node.right)
        print(node.data)
        


input = sys.stdin.readline
tree = Tree()
num = int(input())

while True:
    try:
        node = Node(num)
        tree.addNode(node)
        num = int(input())
    except:
        break

tree.traverse()