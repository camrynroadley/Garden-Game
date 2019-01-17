"""
A Singleton that controls the image and sound files. Uses python csv.
"""


import csv

# The FileManager's job is to handle all file input
class FileManager():
    # Inner class - This is where the implementation goes!
    class __FileManager:
        def __init__(self):

            # Two separate dictionaries for the images
            # tracks file paths and file values
            self._image_paths = {}
            self._image_values = {}
            with open('images/images.csv', newline = '') as input:
                reader = csv.reader(input)
                for row in reader:
                    k = row[0]
                    path = row[1]
                    value = row[2]

                    self._image_paths[k] = path
                    self._image_values[k] = value

            #Another dictionary for the sounds
            self._sound_paths = {}
            with open('sounds/sounds.csv', newline = '') as input:
                sound_reader = csv.reader(input)
                for row in sound_reader:
                    s_k = row[0]
                    s_path = row[1]

                    self._sound_paths[s_k] = s_path

        def get_path(self, key):
            return self._image_paths[key]

        def get_value(self, key):
            return self._image_values[key]

        def get_sound_path(self, key):
            return self._sound_paths[key]


    # Instance variable!
    instance = None
    def __init__(self):
        # Create an object if one does not exist
        # Note that if two constructors are called, only one object is created!
        if not FileManager.instance:
            FileManager.instance = FileManager.__FileManager()

    # Pass attribute retrieval to the instance
    def __getattr__(self, name):
        return getattr(self.instance, name)

