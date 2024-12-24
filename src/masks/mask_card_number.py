from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.

    Пример ввода:
    7000792289606361

    Пример вывода:
    7000 79** **** 6361
    """

    str_card_number = str(card_number)

    return f"{str_card_number[0:4]} {str_card_number[4:6]} ** **** {str_card_number[-4:]}"
