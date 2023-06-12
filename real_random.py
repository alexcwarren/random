import random

def generate_random_numbers(max_num: int, num_samples: int) -> list[int]:
    """Return list of frequencies of numbers 1 to max_num after generating
    num_samples random integers.

    Indices of list represent each number, and the element at a given index
    is that number's frequency.
    """
    number_counter = [0 for _ in range(max_num)]

    for _ in range(num_samples):
        number_counter[random.randint(1, max_num) - 1] += 1

    for i,num in enumerate(number_counter):
        print(f"{(i + 1):3}: " + "*" * num)

if __name__ == "__main__":
    # Simulate a six-sided die (d6)
    d6_counts = generate_random_numbers(6, 100)
