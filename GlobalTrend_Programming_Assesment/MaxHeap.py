class MaxHeap:
    def __init__(self):
        self.heap = []
    def insert(self, value):
        self.heap.append(value)
        self._heap_up(len(self.heap) - 1)
    def delete(self):
        if len(self.heap) == 0:
            raise IndexError("delete from an empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heap_down(0)
        return max_value
    def get_max(self):
        if len(self.heap) == 0:
            raise IndexError("get from an empty heap")
        return self.heap[0]
    def _heap_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heap_up(parent_index)
    def _heap_down(self, index):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heap_down(largest)
    def __str__(self):
        return str(self.heap)
# Example 
heap = MaxHeap()
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(5)
print(heap)       
print(heap.get_max())  
heap.delete()      
print(heap)        