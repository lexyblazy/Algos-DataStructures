class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{} -> {}'.format(self.data, self.next)

class Queue:
  def __init__(self):
    self.first = None
    self.last = None

  def __repr__(self):
    return "{}".format(self.first)

  def enqueue(self,data):
    newNode = Node(data)
    if not self.first:
      self.first = newNode
      self.last = newNode
    else:
      self.last.next = newNode
      self.last = newNode
  
  def dequeue(self):
    if not self.first:
      return None
    temp = self.first
    self.first = self.first.next
    return temp.data



q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q)