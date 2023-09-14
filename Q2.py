def generate_odd_numbers(n):
    odd_numbers = [2 * i - 1 for i in range(1, n + 1)]
    return odd_numbers

N = 10  # Change N to the desired number of odd natural numbers
odd_numbers_list = generate_odd_numbers(N)
print(odd_numbers_list)
