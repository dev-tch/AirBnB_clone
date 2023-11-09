#!/usr/bin/python3
"""module for package initialization"""


from models.engine.file_storage import FileStorage
# unique storage instance for application
storage = FileStorage()
# load data
storage.reload()
