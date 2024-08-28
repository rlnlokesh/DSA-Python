class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def extract_min(self):
        if not self.heap:
            return None

        min_value = self.heap[0]
        last_index = len(self.heap) - 1

        self.heap[0] = self.heap[last_index]
        self.heap.pop()

        self.heapify_down(0)

        return min_value

    def delete_node(self, value):
        index = self.heap.index(value)
        last_index = len(self.heap) - 1

        self.heap[index], self.heap[last_index] = self.heap[last_index], self.heap[index]
        self.heap.pop()

        self.heapify_down(index)

    def display(self):
        print("Min Heap:", self.heap)

# Example usage:
if __name__ == '__main__':
    min_heap = MinHeap()

    min_heap.insert(3)
    min_heap.insert(4)
    min_heap.insert(9)
    min_heap.insert(5)
    min_heap.insert(2)

    min_heap.display()  # Output: Min Heap: [2, 4, 3, 5, 9]

    min_value = min_heap.extract_min()
    print("Extracted min value:", min_value)  # Output: Extracted min value: 2

    min_heap.display()  # Output: Min Heap: [3, 4, 9, 5]

    min_heap.delete_node(4)
    min_heap.display()  # Output: Min Heap: [3, 5, 9]
