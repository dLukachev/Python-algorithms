from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):  # Добавление в конец
        self.items.append(item)
    
    def dequeue(self):  # Удаление из начала
        if not self.is_empty():
            return self.items.popleft()
        return None
    
    def is_empty(self):  # Проверка на пустоту
        return len(self.items) == 0
    
    def peek(self):  # Просмотр первого элемента
        if not self.is_empty():
            return self.items[0]
        return None
    

# Реальное применение: Обработка запросов в игре
game_queue = Queue()
game_queue.enqueue("Player1: Move")
game_queue.enqueue("Player2: Jump")
game_queue.enqueue("Player3: Shoot")

print("Очередь запросов:", list(game_queue.items))  # Вывод: ['Player1: Move', 'Player2: Jump', 'Player3: Shoot']
print("Обработан запрос:", game_queue.dequeue())  # Вывод: Player1: Move
print("Очередь после обработки:", list(game_queue.items))  # Вывод: ['Player2: Jump', 'Player3: Shoot']
print('------------------------------------------------------------------------')
# Очередь сообщений
chat_queue = Queue()
chat_queue.enqueue("User1: Hi!")
chat_queue.enqueue("User2: Hello!")
chat_queue.enqueue("User1: How are you?")

while not chat_queue.is_empty():
    print("Отправлено:", chat_queue.dequeue())  # Вывод: последовательная отправка сообщений