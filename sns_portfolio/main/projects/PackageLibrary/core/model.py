# PackageLibrary.core.model

# Required Package Imports
import os

class Model:
    def __init__(self, name, prefabs=[]):
        self.location = os.path.abspath(__file__)
        self.attributes = ['name', 'base_directory', 'prefabs']
        self.name = name
        self.base_directory = os.getcwd()
        self.prefab_directory = os.path.join(self.base_directory, f"{self.name}s")
        # Check for a prefab directory
        if not os.path.exists(self.prefab_directory):
            print(f"{self.name} prefab directory does not exist")
            print(f"Attempting to create directory: {self.prefab_directory}")
            try:
                os.makedirs(self.prefab_directory)
                print(f"{self.name} prefab directory created: {self.prefab_directory}")
            except:
                print(f"{self.name} prefab directory could not be created")
        # Check that the prefab directory is a package
        if not os.path.exists(os.path.join(self.prefab_directory, '__init__.py')):
            try:
                prefab_init = open(os.path.join(self.prefab_directory, '__init__.py'), 'a')
                prefab_init.write(f"{self.name}.prefab __init__")
                prefab_init.close()
            except:
                print(f"Prefab directory is not a package")
        # Attempt to import the prefab
        try:
            pass
        except:
            pass
        self.prefabs = prefabs
        # Creat

    def __str__(self):
        return 'Model'

    def __repr__(self):
        return f'< PackageLibrary.core.Model Object >'

    def new_model(self, default_object, prefabs=[]):
        """
        Creates a new model package in the 'target_directory'
        with a name derived from 'default_object.__str__'.
        The attributes of 'default_object' will be used as
        default values for the model and attributes of objects in
        'prefabs' will be saved to the 'prefab' collection
        """
        model_name = default_object.__str__()
        # Check the target_directory is 

    def save_prefab(self, target_object):
        """
        Saves the object as a prefab.
        If a model for 'target_object' does not exist,
        one will be created
        """