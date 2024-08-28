class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, priority, item):
        element = (priority, item)
        self.queue.append(element)
        self.queue.sort(key=lambda x: x[0])  # Sort based on priority

    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)[1]

    def is_empty(self):
        return len(self.queue) == 0

# Example usage:
if __name__ == '__main__':
    priority_queue = PriorityQueue()

    priority_queue.push(3, "Task 1")
    priority_queue.push(1, "Task 2")
    priority_queue.push(2, "Task 3")

    while not priority_queue.is_empty():
        task = priority_queue.pop()
        print("Processing:", task)
