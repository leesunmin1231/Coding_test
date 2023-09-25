class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.list = None
    def addNode(self, data):
        node = Node(data)
        if not self.list:
            self.list = node
            return
        cur = self.list
        while cur.next:
            cur = cur.next
        cur.next = node
    def search(self, data):
        cur = self.list
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None
    def traverse(self):
        cur = self.list
        while cur:
            print(cur.data, end="")
            if cur.next:
                print(" -> ", end="")
            cur = cur.next
        print("")

list = LinkedList()
list.addNode(3)
list.addNode(4)
list.addNode(5)
list.addNode(6)
list.traverse()