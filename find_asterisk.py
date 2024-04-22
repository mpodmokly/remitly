import json

def find_asterisk(filename):
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        raise FileNotFoundError
    
    data = json.load(file)

    try:
        if data["PolicyDocument"]["Statement"][0]["Resource"] == "*":
            return True
        return False
    except Exception:
        return False
