import json

def load_urls_from_json(json_path="TestData/test_urls.json"):
    with open(json_path, "r") as file:
        return json.load(file)

def load_users_from_json(json_path="TestData/test_users.json"):
    with open(json_path, "r") as file:
        return json.load(file)

def load_quick_launch_items_from_json(json_path="TestData/test_quick_launch_items.json"):
    with open(json_path, "r") as file:
        return json.load(file)

def load_profile_menu_items_from_json(json_path="TestData/test_profile_menu_items.json"):
    with open(json_path, "r") as file:
        return json.load(file)