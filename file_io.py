import json
import os

FILENAME = "my_savings_data.json"

def read_my_file():
    if not os.path.exists(FILENAME):
        return {"user": {"student_name": "", "max_limit": 0.0}, "items_bought": []}
    
    try:
        f = open(FILENAME, "r")
        my_data = json.load(f)
        f.close()
        return my_data
    except:
        return {"user": {"student_name": "", "max_limit": 0.0}, "items_bought": []}

def write_to_file(info):
    f = open(FILENAME, "w")
    json.dump(info, f, indent=4)
    f.close()

