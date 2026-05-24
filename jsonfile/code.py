import json

# json_str = '{"name" : "Shivam","isTeacher" : true}'
# print(type(json_str))

# py_obj = json.loads(json_str)
# print(py_obj)
# print(type(py_obj))

py_obj = {
    "ky1" : "value1",
    "ky2" : 23
}

with open("D:\desktop\Data Science Learning\Data-Science-learning\jsonfile\data.json", "w") as file:
    json.dump(py_obj, file)