#!/usr/bin/python3
"""
This is the base model
it generates a unique id with uuid.uuid4()
created at date time 
can also update from json
this is all for now
"""

class BaseModel(object):
    """
    This is the base model
    """

    id = str(uuid.uuid4())

    def __init__(self)
