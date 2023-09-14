my_list = [12, 'abc', 45, 'def', 78, 34.5, 56, 'xyz', 89]
integer_list = [x for x in my_list if isinstance(x, int)]
print("List with non-integer values removed:", integer_list)
