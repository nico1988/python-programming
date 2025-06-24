import os

# create a directory named 'python_files_test'
directory_name = 'python_files_test'
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    print(f"Directory '{directory_name}' created.")
else:
    print(f"Directory '{directory_name}' already exists.")

# print current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# create a file named 'test_file.py' in the 'python_files_test' directory
file_path = os.path.join(directory_name, 'test_file.py')
with open(file_path, 'w') as file:
    file.write("# This is a test file.\n")
    file.write("print('Hello from test_file.py')\n")
    print(f"File '{file_path}' created with sample content.")