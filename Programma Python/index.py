import json

with open('./base.json', mode='r', encoding='utf-8') as f:
    file_contents = f.read()

gantt_data = json.loads(file_contents)

print(gantt_data)