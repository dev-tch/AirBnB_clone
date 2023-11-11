#!/usr/bin/python3
""" module with one class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """implement class"""
    # public attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""
