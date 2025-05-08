
import json

def read_json_data(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        json_data = json.loads(data)
        return json_data

data = read_json_data("user_data.json")

print(data)
print(data['Firstname'])
print(data['Lastname'])
print(data['phone_no'])
def write_json_content(filepath, data):
    with open(filepath, "w") as file:
        json_data = json.dumps(data)
        file.write(json_data)


data['emp_id'] = "IT_01"
write_json_content("user_data.json", data)
