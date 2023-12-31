from priorityQueue import K, Entry, PQEntry, AbstractPriorityQueue
from typing import Generic, TypeVar, List, Comparator, Optional

K = TypeVar('K')
V = TypeVar('V')

class HeapPriorityQueue(AbstractPriorityQueue[K, V]):
    def __init__(self, comp: Optional[Comparator[K]] = None, keys: List[K] = None, values: List[V] = None):
        super().__init__(comp)
        self.heap = []

        if keys is not None and values is not None:
            for j in range(min(len(keys), len(values))):
                self.heap.append(PQEntry(keys[j], values[j]))

        self.heapify()

    def parent(self, j: int) -> int:
        return (j-1) // 2
    
    def left(self, j:int) -> int:
        return 2*j + 1
    
    def right(self, j:int) -> int:
        return 2*j + 2
    
    def hasLeft(self, j:int) -> bool:
        return self.left(j) < len(self.heap)
    
    def hasRight(self, j:int) -> bool:
        return self.right(j) < len(self.heap)
    
    def swap(self, i:int, j:int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def upheap(self, j:int):
        while j>0:
            p = self.parent(j)
            if self.compare(self.heap[j], self.heap[p]) >= 0:
                break
            self.swap(j, p)
            j = p

    def downheap(self, j:int):
        while self.hasLeft(j):
            leftIndex = self.left(j)
            smallChildIndex = leftIndex
            if self.hasRight(j):
                rightIndex = self.right(j)
                if self.compare(self.heap[leftIndex], self.heap[rightIndex]) > 0:
                    smallChildIndex = rightIndex
            if self.compare(self.heap[smallChildIndex], self.heap[j]) >= 0:
                break
            self.swap(j, smallChildIndex)
            j = smallChildIndex

    def heapify(self):
        start_index = self.parent(self.size() - 1)
        for j in range(start_index, -1, -1):
            self.downheap(j)

    def size(self):
        return len(self.heap) 
    
    def min(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    def insert(self, key: K, value: V):
        self.check_key(key)
        newest = PQEntry(key, value)
        self.heap.append(newest)
        self.upheap(len(self.heap) - 1)
        return newest
    
    def removeMin(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        answer = self.heap[0]
        self.swap(0, len(self.heap) - 1)
        self.heap.pop()
        self.downheap(0)
        return answer
    
    def PQSort(S, P):
        n = S.size()

        for j in range(n):
            element = S.remove(S.first())
            P.insert(element, None)

        for j in range(n):
            element = P.remove_min().getKey()
            S.add_last(element)
