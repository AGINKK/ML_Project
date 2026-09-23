import random

# 1. Random numbers
print(random.randint(1, 100))  # Random whole integer between 1 and 100
print(random.random())  # Random float between 0.0 and 1.0

# 2. Picking from a list (e.g., choosing a fruit or prize)
fruits = ["apple", "banana", "cherry", "date"]
print(random.choice(fruits))  # Picks one random fruit

# 3. Picking multiple unique items (e.g., picking 2 raffle winners)
winners = random.sample(fruits, 2)
print("Raffle winners:", winners)