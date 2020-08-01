class Min_heap:
    def __init__(self,maxsize):
        self.size=0
        self.maxsize=maxsize
        self.arr=[0]*(maxsize+1)
        self.front=0
    def parent(self,pos):
        return pos-1//2
    def left_child(self,pos):
        return pos*2+1
    def right_child(self,pos):
        return pos*2+2
    def insert(self,ele):
        if self.size<self.maxsize:
            i=self.size
            self.arr[i]=ele
            self.size+=1
    def heapify(self,length,front):
        smallest=front
        left=self.left_child(smallest)
        right=self.right_child(smallest)
        if left<length and self.arr[left]<self.arr[smallest]:
            smallest=left
        if right<length and self.arr[right]<self.arr[smallest]:
            smallest=right
        if smallest!=front:
            (self.arr[smallest],self.arr[front])=(self.arr[front],self.arr[smallest])
            self.heapify(length,smallest)
    def heapsort(self,length):
        for i in range(self.size//2,-1,-1):
            self.heapify(length,i)
        for i in range(self.size-1,-1,-1):
            self.arr[self.front],self.arr[i]=self.arr[i],self.arr[self.front]
            self.heapify(i,self.front)
    def Print(self):
        for i in range(0, (self.size//2)):
            print(" PARENT : "+ str(self.arr[i])+" LEFT CHILD : "+
                                str(self.arr[2 * i + 1])+" RIGHT CHILD : "+
                                str(self.arr[2 * i + 2]))
    


if __name__ == "__main__":

    print('The minHeap is ')
    minHeap = Min_heap(6)
    minHeap.insert(9)
    minHeap.insert(5)
    minHeap.insert(13)
    minHeap.insert(12)
    minHeap.insert(45)
    minHeap.insert(16)
    minHeap.Print()
    minHeap.heapsort(6)
    print("heapsort")
    minHeap.Print()
