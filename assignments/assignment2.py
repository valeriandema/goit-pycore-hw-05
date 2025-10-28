from decimal import Decimal
import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[Decimal]:
    """
    Генератор, який приймає текст і шукає дійсні числа в тексті з
    допомогою регулярних виразів.
    Дійсні числа у тексті вважаються записаними без помилок і чітко
    відокремлені пробілами з обох боків.
    """
    # Регулярний вираз для пошуку дійсних чисел, відокремлених
    # пробілами з обох боків
    pattern = r'(?<=\s)\d+\.\d+(?=\s)'
    for match in re.finditer(pattern, text):
        yield Decimal(match.group())


def sum_profit(
    text: str,
    func: Callable[[str], Generator[Decimal]]
) -> Decimal:
    """
    Сумує дійсні числа, які знаходяться в тексті і повертаються
    генератором. Приймає функцію-генератор як параметр.
    """
    return sum(number for number in func(text))
