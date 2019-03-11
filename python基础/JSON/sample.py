import json

# json_str = '{"name": "jeff", "age": 18, "married": false}'
json_str = '{"name": "jeff", "age": 18, "married": false, "lucky_number": [1,\
        2,3,4,5]}'
human = json.loads(json_str)
print(type(human))
print(human)

# json_obj = {'name': 'jeff', 'age': 18, 'married': False}
json_obj = {'name': 'jeff', 'age': 18, 'married': False, 'lucky_number': [1,
            2, 3, 4, 5]}
result = json.dumps(json_obj)
print(type(result))
print(result)
