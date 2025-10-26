from decimal import Decimal
from assignments.assignment1 import caching_fibonacci
from assignments.assignment2 import generator_numbers, sum_profit
from assignments.assignment3 import (
    load_logs, 
    filter_logs_by_level, 
    count_logs_by_level, 
    display_log_counts,
    display_logs_for_level
)
from assignments.assignment4 import add_contact, show_phone

def main():
    test_assignment1()
    test_assignment2()
    test_assignment3()
    test_assignment4()


def test_assignment4():
    """Тестування завдання 4 - консольний бот з обробкою помилок"""

    contacts = {}
    
    # Тест 1: add без аргументів (IndexError)
    print("1. Тест: add без аргументів")
    result = add_contact([], contacts)
    print(f"Результат: {result}\n")
    
    # Тест 2: add з правильними аргументами
    print("2. Тест: add з правильними аргументами")
    result = add_contact(["Jime", "0501234356"], contacts)
    print(f"Результат: {result}\n")
    
    # Тест 3: phone з неіснуючим контактом (KeyError)
    print("3. Тест: phone з неіснуючим контактом")
    result = show_phone(["Bob"], contacts)
    print(f"Результат: {result}\n")


def test_assignment3():
    
    try:
        # Завантажуємо логи
        logs = load_logs('assets/logfile.log')
        print(f"Завантажено {len(logs)} записів логів\n")
        
        # 1. Загальна статистика за рівнями логування
        print("1. Загальна статистика за рівнями логування:")
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
        
        # 2. Детальний вивід для рівня ERROR
        print("\n2. Детальний вивід для рівня ERROR:")
        display_logs_for_level(logs, 'ERROR')
        
    except Exception as e:
        print(f"Помилка при тестуванні: {e}")



def test_assignment1():
    """Тестування завдання 1 - кешування fibonacci"""
    # Отримуємо функцію fibonacci з кешуванням
    fibonacci = caching_fibonacci()
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610


def test_assignment2():
    """Тестування завдання 2 - генератор чисел та підрахунок прибутку"""
    # Тестовий текст з прикладу
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
    assert total_income == Decimal('1351.46')

if __name__ == "__main__":
    main()