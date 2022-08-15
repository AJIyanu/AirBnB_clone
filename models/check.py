#!/usr/bin/python3

from base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
#my_model.save()
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
print("___________________________________________________________________________")
updater = {'updated_at': '2017-09-28T21:05:54.119572', 'id': 'user', 'created_at': '2017-09-28T21:05:54.119427', 'name': 'new_name', 'my_number': 99}
bm = BaseModel(**updater)
print(bm.id)
print(bm)