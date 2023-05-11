import convertapi
import os

convertapi.api_secret = "97H6ER6YCoJnqSjx"

file_path = "C:\\Users\\jacqu\\OneDrive\\Documents\\certificat_de_scolarité_22-23.pdf"

new_file_path = "C:\\Users\\jacqu\\OneDrive\\Documents\\temp"

result = convertapi.convert(
    'txt', # the format you want to convert to
    { 'File': file_path}
).save_files(new_file_path)

# Open the file in 'read' mode ('r')
with open(new_file_path, 'r') as file:
    # Read the entire contents of the file
    content = file.read()

# Print the contents of the file
print(content)

try:
    os.remove(new_file_path)
    print(f"The file '{new_file_path}' has been deleted.")
except FileNotFoundError:
    print(f"The file '{new_file_path}' does not exist.")
except PermissionError:
    print(f"You do not have permission to delete the file '{new_file_path}'.")
except Exception as e:
    print(f"An error occurred while deleting the file: {str(e)}")
