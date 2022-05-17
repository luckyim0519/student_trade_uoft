"""
File made by Lucky and Justin(Taehee) Cha

This file contains all converter functions for this website

All copyrighted materials are owned by Lucky and Justin.
2022, May, 11th
"""
from typing import List
from store_item import StoreItem
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def get_users() -> List[User]:
    """
    Return a list of all the Users that are currently saved on the database.
    """
    curr_user = get_user_model()

    all_users = list(curr_user.objects.all())
    return all_users


def get_posted_items(u: User) -> List[StoreItem]:
    """
    return a copied list of the _posted_store_items list of the User in u

    the id of the two list must be different
    """
    #link with database and find all the items linked with this user
    #TODO
