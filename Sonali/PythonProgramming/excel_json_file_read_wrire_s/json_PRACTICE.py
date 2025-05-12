
import json_PRACTICE

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
# print(y)
print(y["age"])




# def read_json_data(filepath):
#     with open(filepath, "r") as file:
#         data = file.read()
#         json_data = json.loads(data)
#         return json_data


# data = read_json_data("users_data_sonali.json")
# print(data)
