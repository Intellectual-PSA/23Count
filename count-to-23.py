import random

def count_to_23():
    total = 0
    steps = 0

    while total < 23:
        increment = random.choice([2, 3])
        total += increment
        steps += 1
        print(f"Step {steps}: Added {increment}, Total now {total}")

    print(f"\nReached {total} in {steps} steps.")

count_to_23()
