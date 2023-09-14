from collections import Counter

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency_counter = Counter(my_list)

for element, frequency in frequency_counter.items():
    print(f"Element: {element}, Frequency: {frequency}")
