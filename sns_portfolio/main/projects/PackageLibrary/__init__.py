# PackageLibrary __init__
# Import PackageLibrary modules/packages
from . import config, core

__all__ = ['config', 'core']

# Set Up
import os

current_directory = os.getcwd()
default_base_directory = os.path.join(current_directory, 'models_library')

# Check for a 'model_library'
if not os.path.isdir(default_base_directory):
    try:
        os.makedirs(default_base_directory)
        print(f"Base Directory Created: {default_base_directory}")
    except:
        print("Could not create Base Directory")
        raise
else:
    print("Base Directory Found")

# Make sure 'model_library' is a package
base_init = os.path.join(default_base_directory, '__init__.py')
if not os.path.exists(base_init):
    print("Base Directory is not a package")
    print("Attempting to create a package")
    try:
        new_init = open(base_init, "w")
        new_init.write("# model_library __init__")
        new_init.append("__all__ = []")
        new_init.close()
        print("Base Directory '__init__.py' Created")
    except:
        print("Could not convert Base Directory to package")
else:
    print("Base Directory '__init__.py' found")


# Package Methods
def new(profile_name='clean'):
    new_package_library = core.PackageLibrary()
    return new_package_library