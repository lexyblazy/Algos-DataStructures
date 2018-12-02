class MaxHeap:
    def __init__(self):
        self.values = []

    def add(self, data):
        self.values.append(data)
        self.bubbleUp(data)

    def bubbleUp(self, data):

        parentIndex = int((len(self.values) - 1) / 2)
        dataIndex = len(self.values) - 1
        while True:
            if data > self.values[parentIndex]:
                # swap them
                self.values[dataIndex] = self.values[parentIndex]
                self.values[parentIndex] = data
                dataIndex = parentIndex
            else:
                break
            parentIndex = int((parentIndex - 1)/2)

    def extractMax(self):
        max = self.values[0]
        last = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = last
            self.sinkDown()
        return max

    def sinkDown(self):
        rootIndex = 0
        lastIndex = len(self.values) - 1
        while rootIndex <= lastIndex:
            root = self.values[rootIndex]
            leftChildIndex = (2*rootIndex) + 1
            rightChildIndex = (2*rootIndex) + 2
            left = None
            right = None

            if leftChildIndex > lastIndex:
                break
            else:
                if leftChildIndex < lastIndex:
                    left = self.values[leftChildIndex]

                if rightChildIndex < lastIndex:
                    right = self.values[rightChildIndex]

                if right:
                    childIndex = rightChildIndex if right > left else leftChildIndex
                else:
                    childIndex = leftChildIndex
                if root < self.values[childIndex]:
                    temp = self.values[childIndex]
                    self.values[childIndex] = root
                    self.values[rootIndex] = temp
                    rootIndex = childIndex
                else:
                    break

    def __repr__(self):
        return "{}".format(self.values)


heap = MaxHeap()
heap.add(16)
heap.add(10)
heap.add(7)
heap.add(11)

print(heap)
print(heap.extractMax())
print(heap)
print(heap.extractMax())
print(heap)
print(heap.extractMax())
print(heap)
