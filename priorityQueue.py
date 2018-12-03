class Task:
    def __init__(self, action, priority):
        self.action = action
        self.priority = priority

    def __repr__(self):
        return "Todo ->{} priority -> {}".format(self.action, self.priority)
        


class PriorityQueue:
    def __init__(self):
        self.values = []

    def enqueue(self, task):
        self.values.append(task)
        self.bubbleUp(task)

    def dequeue(self):
        max = self.values[0]
        last = self.values.pop()

        if len(self.values) > 0:
            self.values[0] = last

            self.sinkDown()
        return max

    def bubbleUp(self, task):
        lastTaskIndex = len(self.values) - 1

        while True:
            parentTaskIndex = int((lastTaskIndex - 1)/2)
            lastTask = self.values[lastTaskIndex]
            parentTask = self.values[parentTaskIndex]

            if lastTask.priority < parentTask.priority:
                self.values[lastTaskIndex] = self.values[parentTaskIndex]
                self.values[parentTaskIndex] = task
                lastTaskIndex = parentTaskIndex
            else:
                break

    def sinkDown(self):
        rootIndex = 0
        lastIndex = len(self.values) - 1
        while True:
            rootValue = self.values[rootIndex]
            leftChildIndex = 2*rootIndex + 1
            rightChildIndex = 2*rootIndex + 2
            leftChild = None
            rightChild = None

            if leftChildIndex > lastIndex:
                break
            if leftChildIndex <= lastIndex:
                leftChild = self.values[leftChildIndex]

            if rightChildIndex <= lastIndex:
                rightChild = self.values[rightChildIndex]

            if rightChild:
                childIndex = rightChildIndex if rightChild.priority < leftChild.priority else leftChildIndex
            else:
                childIndex = leftChildIndex

            child = self.values[childIndex]
            if child.priority < rootValue.priority:
                self.values[rootIndex] = child
                self.values[childIndex] = rootValue
                rootIndex = childIndex
            else:
                break

    def __repr__(self):
        return "{}".format(self.values)


PQ = PriorityQueue()

task1 = Task("low fever", 10)
PQ.enqueue(task1)
task2 = Task("cold flu", 4)
PQ.enqueue(task2)
task3 = Task("concussion", 3)
PQ.enqueue(task3)
task4 = Task("GunShot wound", 1)
PQ.enqueue(task4)
task5 = Task("cardiac arrest", 0)
PQ.enqueue(task5)
task6 = Task("Appendix", 4)
PQ.enqueue(task6)
task7 = Task("HIV", 10)
PQ.enqueue(task7)
task8 = Task("Gonorhea", 7)
PQ.enqueue(task8)

print(PQ.dequeue())
print(PQ.dequeue())
print(PQ.dequeue())
print(PQ.dequeue())
print(PQ.dequeue())
print(PQ.dequeue())
print(PQ.dequeue())
print(PQ.dequeue())

