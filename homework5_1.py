def caching_fibonacci():
    cache = {}  # Створення кешу для зберігання обчислених значень

    # Внутрішня функція для обчислення чисел Фібоначчі з використанням кешу
    def fibonacci(n):
        if n in cache:       # Перевірка, чи число вже є у кеші
            return cache[n]
        elif n <= 1:    # Випадки для 0 та 1
            return n
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)   # Рекурсивний виклик для обчислення числа Фібоначчі
            cache[n] = result  # Зберігання результату у кеші
            return result
        
    return fibonacci


fib = caching_fibonacci()

print(fib(10)) 
print(fib(15))  


