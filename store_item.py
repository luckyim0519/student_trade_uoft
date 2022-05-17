"""
File made by Lucky and Justin(Taehee) Cha

All copyrighted materials are owned by Lucky and Justin.
2022, May, 11th
"""
from django.contrib.auth.models import User


class StoreItem:
    """
    A class for items on the website

    === Private Attributes ===
    _name: name of the item
    _id: id of the item
    _og_user: the user that posted this Store_item

    ==== Representation Invariant ===
    _id is always unique to only this Store_item object.
    No other Store_item have the same _id as this Store_item
    """
    _name: str
    _id: int
    _og_user: User

    def __init__(self, n: str, i: int, u: User) -> None:
        self._name = n
        self._id = i
        self._og_user = u

    def __eq__(self, __o: object) -> bool:
        return self._id == __o
