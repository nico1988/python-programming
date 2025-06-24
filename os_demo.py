import os

print("This is a demo script for os module operations.")
# Create a directory named 'os_demo_test'
directory_name = 'os_demo_test'
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    print(f"Directory '{directory_name}' created.")
else:
    print(f"Directory '{directory_name}' already exists.")

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# Create a file named 'demo_file.py' in the 'os_demo_test' directory
file_path = os.path.join(directory_name, 'demo_file.py')
try:
    with open(file_path, 'w') as file:
        file.write("# This is a demo file.\n")
        file.write("print('Hello from demo_file.py')\n")
        print(f"File '{file_path}' created with sample content.")
except IOError as e:
    print(f"An IOError occurred: {e}")
else:
    print(f"File '{file_path}' created successfully with sample content.")

# List all files in the current directory
print("Listing all files in the current directory:")
for filename in os.listdir(current_directory):
    if os.path.isfile(os.path.join(current_directory, filename)):
        print(f"- {filename}")  

# Clean up by removing the created directory and file
try:
    os.remove(file_path)
    os.rmdir(directory_name)
    print(f"Cleaned up by removing '{file_path}' and directory '{directory_name}'.")
except OSError as e:
    print(f"An error occurred during cleanup: {e}")
else:
    print("Cleanup successful.")