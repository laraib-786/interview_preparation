
import sys
class MinHeap:
    def __init__(self,maxsize):
        self.size=0
        self.maxsize=maxsize
        self.heap=[0]*(self.maxsize+1)
        self.heap[0]=-1*sys.maxsize
        self.Front=1
    def parent(self,pos):
        return pos//2
    def leftc(self,pos):
        return 2*pos
    def rightc(self,pos):
        return 2*pos+1
    def isLeaf(self,pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    def insert(self,ele):
        if self.size==self.maxsize:
            return
        self.size+=1
        self.heap[self.size]=ele
        current=self.size
        while self.heap[self.parent(current)]>self.heap[current]:
                self.swap(self.parent(current),current)
                current=self.parent(current)
    # Function to print the contents of the heap
    def swap(self,fpos,spos):
        self.heap[fpos],self.heap[spos]=self.heap[spos],self.heap[fpos]
    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : "+ str(self.heap[i])+" LEFT CHILD : "+
                                str(self.heap[2 * i])+" RIGHT CHILD : "+
                                str(self.heap[2 * i + 1]))
    def remove(self):
        popped=self.heap[self.Front]
        self.heap[self.Front]=self.heap[self.size]
        self.size=self.size-1
        self.min_heapify(self.Front)
        return popped
    def min_heapify(self,front):
        current=front
        print(self.size)
        while(current<=self.size//2):
            print(current)
            if (self.heap[current]>self.heap[self.leftc(current)]) or (self.heap[current]>self.heap[self.leftc(current)]):
                if self.heap[self.leftc(current)]<self.heap[self.rightc(current)]:
                    self.swap(self.leftc(current),current)
                else:
                    self.swap(self.rightc(current),current)
            current+=1
if __name__ == "__main__":

    print('The minHeap is ')
    minHeap = MinHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
    print("The Min val is " + str(minHeap.remove()))
    minHeap.Print()
