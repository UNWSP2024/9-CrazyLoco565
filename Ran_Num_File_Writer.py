# Program #2: Random Number File Writer
# Writes random numbers (1–500) to "random_numbers.txt".

import random

def main():
    try:
        # Ask the user for how many random numbers to generate
        count = int(input("How many random numbers should the file hold (1–1000)? "))

        # Validate input
        if count < 1 or count > 1000:
            print("Please enter a number between 1 and 1000.")
            return

        # Open the file in write mode
        with open("random_numbers.txt", "w") as file:
            for _ in range(count):
                number = random.randint(1, 500)
                file.write(f"{number}\n")

        print(f"{count} random numbers have been written to 'random_numbers.txt'.")

    except ValueError:
        print("Invalid input. Please enter an integer.")
    except IOError:
        print("An error occurred while writing to the file.")

# Run the program
if __name__ == "__main__":
    main()
