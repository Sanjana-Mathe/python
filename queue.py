class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.q:
            print("Queue is empty")
            return None
        item = self.q.pop(0)
        print(f"Dequeued: {item}")
        return item

    def display(self):
        print("Queue:", self.q)

# Sample operations
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
