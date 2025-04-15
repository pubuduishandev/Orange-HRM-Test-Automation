import json
import os

def load_users_from_json(json_path="TestData/test_users.json"):
    with open(json_path, "r") as file:
        return json.load(file)