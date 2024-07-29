lst1 = {}

list_of_dicts = {"a" : 1, "b" : 2, "c" : 3}
for item in list_of_dicts:
    for key, value in item.iteritems():
        try:
            item[key] = int(value)
        except ValueError:
            item[key] = float(value)
print(list_of_dicts)