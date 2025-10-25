import json
from pprint import pprint

json_string = """{
  "name": "Игорь",
  "age": 30,
  "is_student": false,
  "car": null,
  "hobbies": ["ping-pong", "swimming"]
}"""


json_from_string = json.loads(json_string)
# pprint(json_from_string)
json_to_string = json.dumps(json_from_string, indent=4, ensure_ascii=False)
print(json_to_string)

with open('json_example_2.json', 'w', encoding='utf-8') as file:
    json.dump(json_from_string, file, indent=4, ensure_ascii=False)

with open('json_example.json', 'r', encoding='utf-8') as file:
    json_from_file = json.load(file)
    # print(json_from_file)

# pprint(json_from_file)