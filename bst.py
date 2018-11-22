class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return '{}'.format(self.data)


class Bst:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if not self.root:
            self.root = newNode
            return self
        else:
            current = self.root
            while True:
                if data > current.data:
                    if not current.right:
                        current.right = newNode
                        return self
                    else:
                        current = current.right
                else:
                    if not current.left:
                        current.left = newNode
                        return self
                    current = current.left

    def find(self, data): #search iteratively
        current = self.root
        found = False
        while current and not found:
            if current.data > data:
                current = current.left
            elif current.data < data:
                current = current.right
            else:
                found = True
        return found

    def find2(self, root, data): #Search recursively
        if root:
            if root.data == data:
                return True
            if root.data < data:
                return self.find2(root.right, data)
            elif root.data > data:
                return self.find2(root.left, data)
        return False

    def BFS(self):
        current = self.root
        visited = [current]
        result = []
        while len(visited) > 0:
            node = visited.pop(0)
            if node:
                result.append(node.data)
                visited.append(node.left)
                visited.append(node.right)

        return result

    def DFSPreOrder(self): #Depth First traversal - (PreOrder iteratively)
      current = self.root
      visited = [current]
      result = []
      while len(visited) > 0:
        node = visited.pop(0)
        if node:
            result.append(node.data)
            visited.insert(0,node.right)
            visited.insert(0,node.left)
      return result

    def DFSPostOrder(self): #Depth First traversal - (PostOrder recursively)
      current = self.root
      result = []

      def traverse(current):
        if current:
          if current.left:
            traverse(current.left)
          if current.right:
            traverse(current.right)
          result.append(current.data)
      traverse(current)
      return result
    
    def DFSInOrder(self): #Depth First traversal - (InOrder recursively)
      current = self.root
      result = []

      def traverse(current):
        if current:
          if current.left:
            traverse(current.left)
          result.append(current.data)
          if current.right:
            traverse(current.right)
      traverse(current)
      return result


    def __repr__(self):
        return "{}".format(self.root)


bst = Bst()
bst.insert(10)
bst.insert(6)
bst.insert(15)
bst.insert(3)
bst.insert(8)
bst.insert(20)

"""
            10
      6           15
    3   8             20
"""
print(bst.BFS())
print("DFSPreOrder {}".format(bst.DFSPreOrder()))
print("DFSPostOrder {}".format(bst.DFSPostOrder()))
print("DFSInOrder {}".format(bst.DFSInOrder()))
