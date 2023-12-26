
import random

    main()
if __name__ == "__main__":
    data = generate_random_data()
def generate_random_data():
    data = [random.randint(1, 100) for _ in range(10)]

    for item in data:
        print(f"Random Number: {item}")
    return data
def main():
