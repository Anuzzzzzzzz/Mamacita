import json

python_user_data = {
    "id": 99,
    "name": "Anuj Paudel",
    "email": "anuj.paudel061.com",
    "is_active": True,
    "courses": ["Biology", "Chemistry"]
}


json_string = json.dumps(python_user_data, indent=4)

print(python_user_data)
print("-"*20)
print(json_string)


