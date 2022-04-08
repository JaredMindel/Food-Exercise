foods_file = open(r'foods.txt')
highfiber_file = open(r'highfiber.txt')
lowfat_file = open(r'lowfat.txt')
low_glycemic_index_file = open(r'low-glycemic-index.txt')

foods_text = foods_file.readlines()
highfiber_text = highfiber_file.read()
lowfat_text = lowfat_file.read()
low_glycemic_index_text = low_glycemic_index_file.read()

foods_file.close()
highfiber_file.close()
lowfat_file.close()
low_glycemic_index_file.close()

print(foods_text)