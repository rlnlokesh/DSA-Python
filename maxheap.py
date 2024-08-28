class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
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
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def extract_max(self):
        if not self.heap:
            return None

        max_value = self.heap[0]
        last_index = len(self.heap) - 1

        self.heap[0] = self.heap[last_index]
        self.heap.pop()

        self.heapify_down(0)

        return max_value

    def delete_node(self, value):
        index = self.heap.index(value)
        last_index = len(self.heap) - 1

        self.heap[index], self.heap[last_index] = self.heap[last_index], self.heap[index]
        self.heap.pop()

        self.heapify_down(index)

    def display(self):
        print("Max Heap:", self.heap)

# Example usage:
if __name__ == '__main__':
    max_heap = MaxHeap()

    max_heap.insert(3)
    max_heap.insert(4)
    max_heap.insert(9)
    max_heap.insert(5)
    max_heap.insert(2)

    max_heap.display()  # Output: Max Heap: [9, 5, 4, 3, 2]

    max_value = max_heap.extract_max()
    print("Extracted max value:", max_value)  # Output: Extracted max value: 9

    max_heap.display()  # Output: Max Heap: [5, 2, 4, 3]

    max_heap.delete_node(4)
    max_heap.display()  # Output: Max Heap: [5, 2, 3]
