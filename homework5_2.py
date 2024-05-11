import re 
from typing import Callable


# Функція яка аналізує текст та ідентифіковує всі дійсні числа, і повертати їх як генератор.
def generator_numbers(text_to_scan: str):
    pattern = re.compile(r" \d+[.]?\d+ " )  # Відокремлення всіх букв та зайвих знаків.
    numbers_iter = pattern.finditer(text_to_scan)  
    for number in numbers_iter:
        yield float(number.group())   


def sum_profit(text_to_scan: str, func: Callable)-> float:
    total_revenue = 0
    for income in func(text_to_scan):   # Використання переданої функції
        total_revenue += income  # Обчислення загальної суми чисел
    return total_revenue 


text = "A worker's total income is made up of a few parts: 1000.01 as a basic income, plus additional income of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)


print(f"Total income: {total_income}")


