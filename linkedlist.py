class Node:
    def __init__(self, val, nextLink=None):
        self.val = val
        self.nextLink = nextLink

    def __repr__(self):
        return "{} -> {}".format(self.val, self.nextLink)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtBeginning(self, data):
        self.head = Node(data, self.head)

    def getFirst(self):
        return self.head.val

    def getLast(self):
        node = self.head
        while node.nextLink:
            node = node.nextLink
        return node

    def size(self):
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.nextLink
        return counter

    def size2(self, node):
        if not node:
            return 0
        return 1 + self.size2(node.nextLink)

    def insertAtEnd(self, data):
        node = self.getLast()
        node.nextLink = Node(data)

    def clear(self):
        self.head = None

    def removeFirst(self):
        self.head = self.head.nextLink

    def removeLast(self):
        slow = self.head
        fast = self.head.nextLink
        while fast.nextLink:
            slow = slow.nextLink
            fast = fast.nextLink
        slow.nextLink = None

    def removeAt(self, index):
        if index == 0:
            self.removeFirst()
            return
        prev = self.getAt(index - 1)
        if (not prev) or (not prev.nextLink):
            return
        prev.nextLink = prev.nextLink.nextLink

    def getAt(self, index):
        counter = 0
        node = self.head
        while node:
            if counter == index:
                return node
            counter += 1
            node = node.nextLink
        return None

    def insertAt(self, data, index):
        if index <= 0:
            self.insertAtBeginning(data)
            return
        prevNode = self.getAt(index-1) or self.getLast()
        prevNode.nextLink = Node(data, prevNode.nextLink)

    def find(self, data):
        node = self.head
        while node:
            if data == node.val:
                return node
            node = node.nextLink
        return 'Not found'

    def find2(self, node, data):
        if not node:
            return 'Not found'
        if node.val == data:
            return node
        return self.find2(node.nextLink, data)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nextLink = current.nextLink
            current.nextLink = prev
            prev = current
            current = nextLink
        self.head = prev

    def midpoint(self):
        slow = self.head
        fast = self.head
        while fast.nextLink and fast.nextLink.nextLink:
            slow = slow.nextLink
            fast = fast.nextLink.nextLink
        return slow.val

    def __repr__(self):
        return "{}".format(self.head)

    def __iter__(self):
        node = self.head
        while(node):
            yield(node)
            node = node.nextLink


list = LinkedList()
list.insertAtBeginning(10)
list.insertAtEnd(1)
list.insertAtBeginning(7)
list.insertAtEnd(12)
list.insertAtBeginning(4)
list.insertAt(3, 6)
print(list)
list.reverse()
print(list)
