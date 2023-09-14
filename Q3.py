def generate_even_numbers(n):
    even_numbers = [2 * i for i in range(1, n + 1)]
    return even_numbers

N = 10  # Change N to the desired number of even natural numbers
even_numbers_list = generate_even_numbers(N)
print(even_numbers_list)
