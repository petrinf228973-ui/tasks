class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        self.root = self._insert(self.root, key)
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
    def search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)
    def delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.minValue(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)
        return node
    def minValue(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

t = Tree()
for x in [8,3,10,1,6,14,4,7,13]:
    t.insert(x)
print("Обход дерева:")
t.inorder(t.root)
print()
print("Удалим 3:")
t.root = t.delete(t.root,3)
t.inorder(t.root)
print()
f = 7
print("Поиск", f, "->", "найден" if t.search(t.root,f) else "нет")
