#!/usr/bin/python3
"""This module is a magic method that initialializes the FileStorage instance for the application for models directory."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
