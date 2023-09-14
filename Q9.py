my_list = [1, 2, 3, 2, 4, 2, 5]
element_to_find = 2
indices = [index for index, value in enumerate(my_list) if value == element_to_find]
print(f"Indices of {element_to_find}: {indices}")
