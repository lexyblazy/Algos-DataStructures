class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return "{} <-> {}".format(self.data, self.next)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        return "{}".format(self.head)

    def insertFirst(self, data):
        newNode = Node(data)
        self.size += 1
        if not self.head:
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1

    def removeLast(self):
        if not self.head:
            return
        if self.size <= 1:
            self.head = None
            self.tail = None
            return
        poppedTail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return poppedTail

    def removeFirst(self):
        if not self.head:
            return
        if self.size <= 1:
            self.head = None
            self.tail = None

        self.head = self.head.next
        self.head.next.previous = None

    def getAt(self, index):
        if not self.head:
          return None
        if index >= self.size or index < 0:
          return None
        if index <= (self.size/2):
            counter = 0
            node = self.head
            while node:
                if counter == index:
                    return node
                node = node.next
                counter += 1
        else:
            node = self.tail
            counter = self.size
            while node:
                if counter == index:
                    return node
                node = node.prev
                counter -= 1
    def setAt(self, data,index):
        node = self.getAt(index)
        if node:
          node.data = data
          return True
        return False
    
    def insertAt(self,data,index):
        if(index < 0 or index > self.size):
          return None
        if index == 0:
          self.insertFirst(data)
          return
        if index == self.size:
            return self.insertAtEnd(data)
        newNode = Node(data)        
        prevNode = self.getAt(index - 1)
        nextNode = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        newNode.next = nextNode
        nextNode.prev = newNode
        self.size += 1

    def removeAt(self,index):
      if index < 0 or index >= self.size:
        return 
      if index == 0:
        self.removeFirst()
      else: 
        prevNode = self.getAt(index -1)
        prevNode.next = prevNode.next.next
        prevNode.next.prev = prevNode
      self.size -= 1

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev

            prev = current
            current = next
        self.head = prev

        
        


list = DoublyLinkedList()
list.insertAtEnd(12)
list.insertAtEnd(3)
list.insertAtEnd(9)
list.insertAtEnd(6)
list.insertFirst(1)
list.insertFirst(7)
list.insertAt(15,4)
list.insertAt(12,4)

print(list)
list.reverse()
print(list)
