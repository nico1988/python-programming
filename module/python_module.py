import os
import sys
import importlib.util
from typing import *

def load_module(module_name, module_path):
    """
    Load a Python module from a specified path.

    :param module_name: Name of the module to load.
    :param module_path: Path to the module file.
    :return: The loaded module.
    """
    if not os.path.exists(module_path):
        raise FileNotFoundError(f"Module path '{module_path}' does not exist.")
    
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None:
        raise ImportError(f"Could not load module '{module_name}' from '{module_path}'.")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    
    return module