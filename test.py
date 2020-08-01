import sys
print(sys.maxsize)
arr=[0]*3
print(arr)
def min_heapify(self,front):
    current=front
    while(front<self.size//2):
        if (self.heap[current]>self.heap[self.leftc(current)]) or (self.heap[current]>self.heap[self.leftc(current)]):
            if self.heap[self.leftc(current)]<self.heap[self.leftc(current)]:
                self.swap(self.leftc(current),current)
            else:
                self.swap(self.leftc(current),current)
    current+=1
    def minHeapify(self, pos):

        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.heap[pos] > self.heap[self.leftc(pos)] or self.heap[pos] > self.heap[self.rightc(pos)]):

                # Swap with the left child and heapify
                # the left child
                if self.heap[self.leftc(pos)] < self.heap[self.rightc(pos)]:
                    self.swap(pos, self.leftc(pos))
                    self.minHeapify(self.leftc(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightc(pos))
                    self.minHeapify(self.rightc(pos))
