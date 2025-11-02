# File Read & Write Challenge + Error Handling Lab
# This program reads a file, modifies its contents,
# and writes the modified version to a new file.

try:
    # Ask the user for a filename to read
    filename = input("Enter the filename to read: ")

    # Try to open and read the file
    with open(filename, "r") as infile:
        content = infile.read()
        print("\n✅ File read successfully!\n")

        # Example modification — convert text to uppercase
        modified_content = content.upper()

    # Create a new file name for the modified version
    new_filename = "modified_" + filename

    # Write the modified content into the new file
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"✅ Modified file has been saved as '{new_filename}'")

except FileNotFoundError:
    print("❌ Error: The file does not exist. Please check the filename and try again.")
except PermissionError:
    print("❌ Error: You do not have permission to read or write this file.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
