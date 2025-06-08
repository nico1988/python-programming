# list python build-in functions in python
print("Python built-in functions")
import builtins
for func in dir(builtins):
    if callable(getattr(builtins, func)):
        print(func)