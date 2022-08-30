#!/usr/bin/python3
"""
This is a place module
"""


from .base_model import BaseModel


class Place(BaseModel):
	"""
	This is the place class
	very good
	"""

	city_id = ""
	user_id = ""
	name = ""
	description = ""
	number_rooms = 0
	number_bathrooms = 0
	max_guest = 0
	price_by_night = 0
	latitude = 0.0
	longitude = 0.0
	amenity_ids = []

	def __init__(self, *args, **kwargs):
		"""
		This initializes the class
		"""
		super().__init__(*args, **kwargs)
