import sys
from typing import List, Dict
from collections import Counter


def load_logs(path: str) -> List[Dict[str, str]]:
    """
    Завантажує логи з файлу і повертає список словників з ключами
    datetime, level, message.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return [parse_log_line(line.strip()) for line in file
                    if line.strip()]
    except FileNotFoundError:
        print(f"Помилка: Файл {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []


def parse_log_line(line: str) -> Dict[str, str]:
    """
    Парсить рядок логу і повертає словник з ключами
    datetime, level, message.
    """
    splitted_line = line.split(" ")

    if len(splitted_line) < 4:
        print(f"Неправильний формат логу: {line}")
        return {}

    return {
        'datetime': f"{splitted_line[0]} {splitted_line[1]}",
        'level': splitted_line[2],
        'message': " ".join(splitted_line[3:])
    }


def filter_logs_by_level(
    logs: List[Dict[str, str]],
    level: str
) -> List[Dict[str, str]]:
    """
    Фільтрує логи за рівнем логування з використанням
    функціонального програмування.
    """
    return list(filter(
        lambda log: log['level'].lower() == level.lower(),
        logs))


def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Підраховує кількість записів для кожного рівня логування.
    Використовує Counter для більш ефективного підрахунку.
    """
    return dict(Counter(log['level'] for log in logs))


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Форматує та виводить результати підрахунку в читабельній формі.
    """
    if not counts:
        print("Логи не знайдено.")
        return

    # Сортуємо за кількістю (спадаючий порядок)
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    # Виводимо заголовок таблиці
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    # Виводимо дані
    for level, count in sorted_counts:
        print(f"{level:<15} | {count}")


def display_logs_for_level(logs: List[Dict[str, str]], level: str) -> None:
    """
    Виводить детальну інформацію для всіх записів певного
    рівня логування.
    """
    filtered_logs = filter_logs_by_level(logs, level)

    if not filtered_logs:
        print(f"Записи з рівнем '{level.upper()}' не знайдено.")
        return

    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in filtered_logs:
        print(f"{log['datetime']} - {log['message']}")


def main():
    """
    Головна функція для обробки аргументів командного рядка та
    виконання аналізу логів.
    """
    if len(sys.argv) < 2:
        print("Використання: python assignment3.py <шлях_до_файлу_логів> "
              "[рівень_логування]")
        print("Приклад: python assignment3.py assets/logfile.log")
        print("Приклад: python assignment3.py assets/logfile.log error")
        return

    log_file_path = sys.argv[1]
    filter_level = sys.argv[2].lower() if len(sys.argv) > 2 else None

    # Завантажуємо логи
    logs = load_logs(log_file_path)

    if not logs:
        print("Не вдалося завантажити логи або файл порожній.")
        return

    # Підраховуємо статистику
    counts = count_logs_by_level(logs)

    # Виводимо загальну статистику
    display_log_counts(counts)

    # Якщо вказано рівень логування, виводимо деталі
    if filter_level:
        display_logs_for_level(logs, filter_level)


if __name__ == "__main__":
    main()
