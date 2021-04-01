# PackageLibrary.config
# Content:
    # Config File Data
    # Config Variables

# Python Imports
import os

__all__ = ['profile']

# Config Variables

    # Config File Data

location = os.path.abspath(__file__)
package_location = os.path.dirname(location)
default_model_directory = os.path.join(package_location, 'model_library')

    # Config Collections

        # Elements in the following collections should follow this syntax:
        # config_variable_name = {
        #     'collection_name':{
        #         'variable_name':variable_value,
        #     }
        # }

        # Package Library Profiles

# Collections of PackageLibrary attributes
profile = {
    'default':{
        'model_directory':default_model_directory,
        'models':{},
        },
}

# Collections of class objects for object creation
model = {

}

# Collections of premade object attributes
prefab = {

}