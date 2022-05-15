import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file)

def load_data(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
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
            print(f"{key} doesn't exist in data.")
    elif cmd == "list":
        print(data)
    elif cmd == "clear":
        data = {}
        save_data(SAVED_DATA, data)
        print("Data cleared.")
    elif cmd == "del":
        key = input("Enter a key: ")
        if key in data:
            print(f"Deleted '{data[key]}' at {key}.")
            del data[key]
            save_data(SAVED_DATA, data)
        else:
            print(f"{key} doesn't exist in data.")
    else:
        print("Unknown command.")

else:
    print("Please pass exactly one command.")