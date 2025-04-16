import json
import os

def load_titles_from_json(json_path="TestData/test_titles.json"):
    with open(json_path, "r") as file:
        return json.load(file)

def load_users_from_json(json_path="TestData/test_users.json"):
    with open(json_path, "r") as file:
        return json.load(file)

def load_side_nav_menu_from_json(json_path="TestData/test_side_nav_menu.json"):
    with open(json_path, "r") as file:
        return json.load(file)

def load_profile_menu_from_json(json_path="TestData/test_profile_menu.json"):
    with open(json_path, "r") as file:
        return json.load(file)