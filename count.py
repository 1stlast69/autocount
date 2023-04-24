# Open the file for reading
with open("numbers.txt", "r") as f:
    # Read the number from the file
    number = int(f.read().strip())

# Add a number to the read number
number += 5

# Open the file for writing
with open("numbers.txt", "w") as f:
    # Write the new number to the file
    f.write(str(number))
