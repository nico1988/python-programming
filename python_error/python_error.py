# python error
import os

try:
  fh = open('test_file.py', 'w')
  fh.write("# This is a test file.\n")
  fh.write("print('Hello from test_file.py')\n")
  fh.close()
except IOError as e:
  print(f"An IOError occurred: {e}")
else:
  print("File 'test_file.py' created successfully with sample content.")