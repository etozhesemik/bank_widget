from typing import Union


def filter_by_state(lists: Union[list], user_state="EXECUTED") -> list:
    new_list = []

    for list in lists:
        search_state = list.get("state")
        if search_state == user_state:
            new_list.append(list)
    return new_list


def sort_by_date(lists: Union[list], reverse: Union[bool]=False) -> list:
    return sorted(lists, key = lambda x: x["date"], reverse=reverse)