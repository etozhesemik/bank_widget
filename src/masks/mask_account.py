from typing import Union


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Функция принимает на вход номер счета
    и возвращает последние 4 цифры номера, а перед ними — две звездочки.

    Пример ввода:
    73654108430135874305

    Пример вывода:
    **4305
    """

    str_account_number = str(account_number)

    return f"**{str_account_number[-4:]}"
