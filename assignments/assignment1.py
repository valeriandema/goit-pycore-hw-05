def caching_fibonacci():
    """
    Створює функцію fibonacci з кешуванням для оптимізації обчислень.
    Використовує замикання для збереження кешу між викликами.
    """
    cache = {}
    
    def fibonacci(n):
        """
        Обчислює n-те число Фібоначчі з використанням кешування.
        """
        # Базові випадки
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Перевіряємо кеш
        if n in cache:
            return cache[n]
        
        # Обчислюємо рекурсивно та зберігаємо в кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci
