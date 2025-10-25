from queue import PriorityQueue
q = PriorityQueue()
q.put((2, 'B'))
q.put((1, 'A'))
q.put((3, 'C'))
while not q.empty():
    print(q.get())
