import json

foods_file = open(r'foods.txt')
highfiber_file = open(r'highfiber.txt')
lowfat_file = open(r'lowfat.txt')
low_glycemic_index_file = open(r'low-glycemic-index.txt')

foods_text = foods_file.read()
highfiber_text = highfiber_file.read()
lowfat_text = lowfat_file.read()
low_glycemic_index_text = low_glycemic_index_file.read()

foods_file.close()
highfiber_file.close()
lowfat_file.close()
low_glycemic_index_file.close()

foods_text = foods_text.splitlines()
highfiber_text = highfiber_text.splitlines()
lowfat_text = lowfat_text.splitlines()
low_glycemic_index_text = low_glycemic_index_text.splitlines()

for x in range(len(foods_text)):
    if foods_text[x] == "salmon2":
        foods_text[x] = "Salmon"
    elif foods_text[x] == "Sriacha":
        foods_text[x] = "Sriracha"

food_list = []

for x in range(len(foods_text)):
    if foods_text[x] != "" and foods_text[x] != "ja&ng":
       food_dict = {foods_text[0]:foods_text[x], highfiber_text[0]:highfiber_text[x], 
       low_glycemic_index_text[0]:low_glycemic_index_text[x], lowfat_text[0]:lowfat_text[x]}
       food_list.append(food_dict)


json_file = open("foods_output.json", "w")
json.dump(food_list, json_file)