import json

with open('./base.json') as f:
    file_contents = f.read()

gantt_data = json.loads(file_contents)

print(gantt_data)