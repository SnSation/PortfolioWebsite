# PackageLibrary.core.library
# Content:
    # Class - PackageLibrary: Stores, creates, and manages models of objects

# Import Required Python Packages
import os, importlib

# Import Required PackageLibrary Components
class PackageLibrary:
    class_name = 'PackageLibrary'

    def __init__(self, model_library):
        self.location = os.path.abspath(__file__)
        self.attributes = ['base', 'models', 'collection']

        self.profile = None
        
        # 'model_directory works best with a relative path
        # from the location of a 'PackageLibrary' instance
        self.model_directory = None
        
        self.model_library = model_library

        self.models = {}

    def __str__(self):
        return f'Library'

    def __repr__(self):
        return f'< Library Object >'
                    

    # Getters and Setters 
        
    # Return the attributes of this object as a dictionary
    def to_dict(self):
        # The keys of the following dictionary are the names of this object's properties
        # The values of the following dictionary are the values of this object's properties
        attribute_dict = {
            "root" : self.root,
            "attributes" : self.attributes,
            "base" : self.base,
            "prefabs":self.prefabs,
            "models" : self.models,
        }

        return attribute_dict

    # Set the value of a single attribute of this object
    def set_attribute(self, attribute_name, attribute_value):
        """
        Searches tracked attributes for the given 'attribute_name'
        Sets this object's attribute value to the given 'attribute_'value'
        """
        for attribute in self.attributes:
            if attribute == attribute_name:
                setattr(self, attribute, attribute_value)
                break

    # Set the value of one or more attributes of this object
    def set_attributes(self, attribute_dict):
        """
        Searches tracked attributes for key matches
        in the given 'attribute_dict'.
        Sets matched attributes to the match's value
        """
        for attribute in self.attributes:
            if attribute in attribute_dict:
                setattr(self, attribute, attribute_dict[attribute])

    def clear_attribute(self, attribute_name):
        """
        Searches tracked attributes for the given 'attribute_name'
        Sets the matched attribute to 'None'
        """
        if attribute_name == "all":
            for attribute in self.attributes:
                setattr(self, attribute, None)
        else:
            self.set_attribute(attribute_name, None)

    # The following getters and setters may be redundant with 'set_attribute'
    # but are included for use with inheritance

    def set_base(self, directory_path):
        self.base = directory_path

    def get_base(self):
        return self.base

    def set_models(self, models_list):
        self.models = models_list

    def get_models(self):
        return self.models

    ##### Utility Methods #####



    ##### Set Up Methods #####

    def load_from_config(self, module_path):
        """
        Attemps to import the 'library' variable
        from the config file
        """
        try:
            config_file = importlib.machinery.SourceFileLoader('library', module_path).load_module()
        except:
            print("config file could not be imported")
            raise
            
        

    ##### Primary Methods #####

    