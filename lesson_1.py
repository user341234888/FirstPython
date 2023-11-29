import json

sample_array = ["1", "2", "3", "4"]
json_str = json.dumps(sample_array, ensure_ascii=False)
print(json_str)
file_descriptor = open(r'dz.json', 'w', encoding='utf-16')
file_descriptor.write(json_str)
file_descriptor.close()
file_descriptor = open(r'dz.json', 'r', encoding='utf-16')
json_str=file_descriptor.read()
main_dic=json.loads(json_str)
print(main_dic)
