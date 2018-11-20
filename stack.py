class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{} -> {}'.format(self.data, self.next)


class Stack:
    def __init__(self):
        self.first = None
        self.size = 0
        self.last = None

    def push(self, data):
        # insert first
        newNode = Node(data)
        if not self.first:
            self.first = newNode
        else:
            newNode.next = self.first
            self.first = newNode
        self.size += 1
        return self.size

    def pop(self):
        data = None
        if not self.first:
          return None
        if self.size == 1:
          self.first = None
          data = self.first.data
        else:
          temp = self.first
          self.first = self.first.next
          data = temp.data
        return data
          


    def __repr__(self):
        return '{}'.format(self.first)


s = Stack()
print(s.push(10))
print(s.push(20))
print(s.push(30))
print(s.push(40))
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
