# Program #1: Item Counter
# Counts how many names are stored in the file "names.txt".

def main():
    try:
        # Open the file in read mode
        with open("names.txt", "r") as file:
            # Read all lines and count them
            names = file.readlines()
            count = len(names)

        print(f"There are {count} names stored in the file.")

    except FileNotFoundError:
        print("Error: The file 'names.txt' was not found.")
    except IOError:
        print("An I/O error occurred while reading the file.")

# Run the program
if __name__ == "__main__":
    main()
