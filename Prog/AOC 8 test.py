# Open the input file for reading
with open("text.txt", "r") as input_file:
    # Read the entire contents of the file into a string
    input_string = input_file.read()

# Create a new string by joining the characters in the input string with a space
output_string = " ".join(input_string)

# Open the output file for writing
with open("text.txt", "w") as output_file:
    # Write the output string to the output file
    output_file.write(output_string)