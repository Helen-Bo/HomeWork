import json

file_obj = open('DPPBVV1U (1).json', 'r')
my_json = json.loads(file_obj.read())

my_list = []
runtime = 0
for i in my_json["_embedded"]["episodes"]:
    runtime += i["runtime"]
    my_list.append('Start of description ')
    my_list .append(i["season"])
    my_list .append(i["number"])
    my_list .append(i["name"])
    my_list .append(i["summary"])
    my_list .append(i["url"])
    my_list .append('End of description')

print(f'Общая длительность серий = {runtime} минут')
print('\n'.join(str(value) for value in my_list))


