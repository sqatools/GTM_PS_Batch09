import json

def read_json_data(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        json_data = json.loads(data)
        return json_data

data = read_json_data("users_data.json")

print(data)
print(data['FirstName'])
print(data['LastName'])

def write_json_content(filepath, data):
    with open(filepath, "w") as file:
        json_data = json.dumps(data)
        file.write(json_data)


data['phone'] = 79879878798
write_json_content("users_data.json", data)

