# PackageLibrary.model_library __init__

# Required Package Imports
from .model import Model

def new_model(target_directory, default_object, prefabs=[]):
    """
    Creates a new model package in the 'target_directory'
    with a name derived from 'default_object.__str__'.
    The attributes of 'default_object' will be used as
    default values for the model and attributes of objects in
    'prefabs' will be saved to the 'prefab' collection
    """
    model_name = default_object.__str__()
    # Check the target_directory is 

def save_prefab(target_object):
    """
    Saves the object as a prefab.
    If a model for 'target_object' does not exist,
    one will be created
    """