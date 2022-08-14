#!/usr/bin/python3
"""
This is the base model
it generates a unique id with uuid.uuid4()
created at date time 
can also update from json
this is all for now
"""
import uuid
from datetime import datetime


class BaseModel(object):
    """
    This is the base model
    """

    id = 0
    created_at = 0
    updated_at = 0

    def __init__(self):
        """
        This initializes the class with Id, Date and Time
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()