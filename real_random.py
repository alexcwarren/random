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

def generate_weighted_random_numbers(possibilities: dict[str, int], num_samples: int) -> list[int]:
    print(possibilities, num_samples)
    possibility_counter = dict.fromkeys(possibilities, 0)
    total = sum(possibilities.values())
    weights = [count / total for count in possibilities.values()]
    for _ in range(num_samples):
        possibility_counter[random.choices([p for p in possibility_counter.keys()], weights)[0]] += 1

    max_width: int = len(max(possibility_counter.keys(), key=len))
    for i, p in enumerate(possibility_counter):
        print(f"{p} ({weights[i] * 100 // 1}): " + str(possibility_counter[p] / num_samples * 100))

if __name__ == "__main__":
    # Simulate a six-sided die (d6)
    # d6_counts = generate_random_numbers(6, 100)

    # Simulate weighted possibilities
    chaos_token_counts = generate_weighted_random_numbers(
        {
            "+1": 1,
            "0": 2,
            "-1": 3,
            "-2": 2,
            "Skull": 2,
            "Cultist": 1,
            "Tablet": 1,
            "Auto Fail": 1,
            "Elder Sign": 1
        },
        10000
    )
