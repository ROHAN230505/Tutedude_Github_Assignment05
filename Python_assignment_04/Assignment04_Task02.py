# Step 1: Write user input to output.txt
text_to_write = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")

print("Data successfully written to output.txt.")

# Step 2: Append additional data
text_to_append = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")

print("Data successfully appended.")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.readlines()

# Print line by line with numbering
for i, line in enumerate(content, start=1):
    print(line.strip())
