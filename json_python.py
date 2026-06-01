# import json
# from encodings import utf_8
# from math import fabs
#
# json_data = """
# {
#   "name": "Иван",
#   "age": 30,
#   "is_student": false,
#   "courses": ["python","Qa_automation"],
#   "address": {
#     "city": "moscow",
#     "zip": "101000"
#   }
# }
# """
# parsed_data = json.loads(json_data)
#
# print(parsed_data["name"])
# data = {
#     "name": "Иван",
#     "age": 30,
#     "is_student": True,}
#
# json_string = json.dumps(data,indent=4)
# print(json_string)
#
# with open("json_example.json","r",encoding='utf_8') as file:
#     read_data=json.load(file)
#     print(read_data)
#
# with open("json_user.json","w",encoding='utf_8') as file:
#     json.dump(data,file,indent=4,ensure_ascii=False)