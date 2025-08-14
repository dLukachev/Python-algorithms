import time
import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class BigO:
    @staticmethod
    def timeit(func):
        """Декоратор для проверки времени выполнения функции"""
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            logging.info(f'Время выполнения функции: {end - start:.8f}')
            return result
        return wrapper

    @staticmethod
    @timeit
    def find_max(data: list) -> int:
        """
        Это алгоритм поиска наибольшего числа в списке. У него сложность O(n), 
        потому что зависит от длинны листа, который передается в аргументы
        """
        if not data:
            return 0
        max_num = 0
        for i in data:
            if isinstance(i, int):
                if i > max_num:
                    max_num = i
        
        return max_num
    
    @staticmethod
    @timeit
    def unique_words(text: str) -> list:
        """
        Этот алгоритм возвращает список уникальных слов в строке. У него сложность O(n), 
        потому что зависит от длинны строки.
        """
        words = text.lower().split()
        unique = []
        for word in words:
            if word not in unique:
                unique.append(word)
        return unique
    

    @staticmethod
    @timeit
    def linear_search(items, target) -> int:
        """
        Этот алгоритм возвращает индекс искомого элемента. 
        У него сложность в худшем случае O(n). В лучшем O(1)
        """
        for index, item in enumerate(items):
            if item == target:
                return index
        return -1
    

    @staticmethod
    @timeit
    def bubble_sort(data: list) -> list:
        """
        Пузырьковая сортировка работает, многократно проходя по списку и "всплывая" (bubble up) 
        большие элементы к концу. На каждой итерации сравниваем соседние элементы и меняем их 
        местами, если они в неправильном порядке. Временная сложность: O(n²) в худшем и среднем случае.
        """
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

    @staticmethod
    def quick_sort(data: list):
        """
        Быстрая сортировка — более эффективный алгоритм, использующий принцип 
        "разделяй и властвуй". Выбирается опорный элемент (pivot), массив делится 
        на подмассивы (меньше и больше pivot), которые рекурсивно сортируются.
        Временная сложность: O(n log n) в среднем, O(n²) в худшем 
        случае (редко, если плохой pivot).
        """
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]  # Выбираем средний элемент как pivot
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return BigO.quick_sort(left) + middle + BigO.quick_sort(right)
    

class BinarySearch:
    @staticmethod
    @BigO.timeit
    def search(arr, target):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2  # Находим середину
            if arr[mid] == target:
                return mid  # Нашли, возвращаем индекс
            elif arr[mid] < target:
                left = mid + 1  # Ищем в правой половине
            else:
                right = mid - 1  # Ищем в левой половине
        return -1  # Элемент не найден
    
    @staticmethod
    @BigO.timeit
    def search_recursive(arr, target, left, right):
        if left > right:
            return -1  # Элемент не найден
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return BinarySearch.search_recursive(arr, target, mid + 1, right)
        else:
            return BinarySearch.search_recursive(arr, target, left, mid - 1)