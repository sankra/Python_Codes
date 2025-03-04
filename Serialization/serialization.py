import json

# Python object (dictionary)
data = {"name": "Alice", "age": 25, "city": "New York"}

# Serialize: Convert Python object → JSON string
json_str = json.dumps(data)
print(json_str) 
print(type(json_str))

# Deserialize: Convert JSON string → Python object
python_obj = json.loads(json_str)
print(python_obj)
print(type(python_obj))
