import json
if __name__ == "__main__":
    with open("test/secerts.json", "r") as f:
        secrets = json.load(f)
    print(secrets["password"])
    print(secrets["api_key"])