class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Класс бинарного дерева поиска
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def _find_min(self, node):
        if node is None:
            return None, None
        if node.left is None:
            return node.value, node
        return self._find_min(node.left)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Случай 1: Лист или узел без потомков
            if node.left is None and node.right is None:
                return None
            # Случай 2: Один потомок
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_value, min_node = self._find_min(node.right)
                node.value = min_value
                node.right = self._delete_recursive(node.right, min_value)
        return node

# Реальное применение: Хранение рейтингов игроков
bst = BinarySearchTree()
ratings = [10, 15, 11, 20, 30 ,90, 88, 45, 12, 23, 34, 43]
for rating in ratings:
    bst.insert(rating)

# Поиск значения
result = bst.search(14)
print("Не найден узел со значением 14:", result.value if result else "Не найдено")
result = bst.search(20)
print("Найден узел со значением 20:", result.value if result else "Не найдено")