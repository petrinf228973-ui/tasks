print("МАССИВ  ")
numbers = [5, 2, 8, 1, 3]
print("Исходный массив:", numbers)
numbers.append(10)
print("После добавления:", numbers)
numbers.remove(2)
print("После удаления:", numbers)
numbers.sort()
print("Отсортированный массив:", numbers)
print("Элемент по индексу 2:", numbers[2])
print()

print(" СТЕК  ")
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Стек:", stack)
top = stack.pop()
print("Сняли элемент:", top)
print("Стек после удаления:", stack)
print()

print("  ОЧЕРЕДЬ")
from collections import deque
queue = deque()
queue.append("Петя")
queue.append("Вася")
queue.append("Маша")
print("Очередь:", queue)
first = queue.popleft()
print("Обслужили:", first)
print("Теперь очередь:", queue)
print()

print("ДЕК  ")
d = deque()
d.append(1)
d.append(2)
d.appendleft(0)
print("Дек после добавления:", d)
d.pop()
d.popleft()
print("Дек после удаления:", d)
print()

print(" ПРИОРИТЕТНАЯ ОЧЕРЕДЬ  ")
import heapq
priority_queue = []
heapq.heappush(priority_queue, (2, "Вася"))
heapq.heappush(priority_queue, (1, "Петя"))
heapq.heappush(priority_queue, (3, "Маша"))
while priority_queue:
    print("Следующий:", heapq.heappop(priority_queue))
print()

print(" СВЯЗНЫЙ СПИСОК  ")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
linked = LinkedList()
linked.add("Петя")
linked.add("Вася")
linked.add("Маша")
print("Список:")
linked.display()
print()

print(" МУЛЬТИСПИСОК  ")
multi = [
    ["Петя", [5, 4, 3]],
    ["Маша", [4, 5, 5]],
    ["Вася", [3, 3, 4]]
]
for student in multi:
    name = student[0]
    marks = student[1]
    avg = sum(marks) / len(marks)
    print(f"{name}: оценки {marks}, средний балл {avg:.2f}")
print()
print("  КОНЕЦ ПРОГРАММЫ  ")
