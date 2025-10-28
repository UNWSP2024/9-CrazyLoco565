# Program #3: Average Numbers
# Reads numbers from "numbers.txt" and calculates total and average.

def main():
    try:
        with open("numbers.txt", "r") as file:
            total = 0
            count = 0

            for line in file:
                try:
                    num = int(line.strip())
                    total += num
                    count += 1
                except ValueError:
                    print(f"Skipping invalid entry: {line.strip()}")

        if count > 0:
            average = total / count
            print(f"Total of numbers: {total}")
            print(f"Average of numbers: {average:.2f}")
        else:
            print("No valid numbers found in the file.")

    except FileNotFoundError:
        print("Error: The file 'numbers.txt' was not found.")
    except IOError:
        print("An I/O error occurred while reading the file.")

# Run the program
if __name__ == "__main__":
    main()
