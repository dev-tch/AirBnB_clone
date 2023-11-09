#!/usr/bin/python3
""" module with one class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """implement class"""
    place_id = ""
    user_id = ""
    text = ""
