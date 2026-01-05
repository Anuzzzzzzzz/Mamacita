import json

user_profile = {
    "name": "Anuj Paudel",
    "email": "anuj@example.com",
    "hobbies": ["sleeping", "eating", "gaming"],
    "address": {
        "city": "Kathmandu",
        "zip_code":"33700"    
    }
}

user_profile_json = json.dumps(user_profile, indent=4)

print(user_profile_json)
print(user_profile)