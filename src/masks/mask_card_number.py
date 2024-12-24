def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.

    Пример ввода:
    7000792289606361

    Пример вывода:
    7000 79** **** 6361
    """

    str_card_number = str(card_number)
    if len(str_card_number) == 16:
        return f"{str_card_number[0:4]} {str_card_number[4:6]} ** **** {str_card_number[-4:]}"
    else:
        return "Номер карты должен содержать 16 символов"
