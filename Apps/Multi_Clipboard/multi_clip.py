import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return(data)
    except:
        return {}

if len(sys.argv) == 2:
    cmd = sys.argv[1]
    data = load_data(SAVED_DATA)

    if cmd == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print(f"Saved '{clipboard.paste()}' at {key}.")
    elif cmd == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print(f"Copied '{data[key]}' to clipboard.")
        else:
            print("Key doesn't exist.")
    elif cmd == "list":
        print(data)
    elif cmd == "clear":
        data = {}
        save_data(SAVED_DATA, data)
        print("Data cleared.")
    else:
        print("Unknown command.")
else:
    print("Please pass exactly one command.")