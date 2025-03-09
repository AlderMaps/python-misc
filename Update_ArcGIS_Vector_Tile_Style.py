# Script by Misti Wudtke | misti@aldermaps.com | hub.aldermaps.com
# From the repo: https://github.com/AlderMaps/python-misc

# The purpose of this script is to provide a way to update ALL values of a given key
# in the JSON style object of an Esri basemap (as downloaded from Vector Tile Style Editor)
# This particular script updates the value for all instance of the key "minzoom"
# but could easily be modified to update other key-value pairs as needed.

# NOTE: To update the JSON in AGOL, go to the Item page of your copy
# of the style, select the "Update" button,and drag your NEW .json file
# (output of the script) into the dialoge box--boom, that's it!

import json

# The full path to the JSON style file you downloaded from within Vector Tile Style Editor
# ...update to the path of YOUR file! 
style = r"C:\your-dir-goes-here\your-style-file-name.json"

# A NEW file where the updated JSON will be written...update to YOUR path and file name!
newstyle = r"C:\your-dir-goes-here\your-style-file-name_NEW.json"

# Open the json file for processing:
with open(style) as s:
    data = json.load(s)

# The json data is loaded as a Python dictionary.
# I'm interested in the value at the key "layers";
# this value itself is a list of dictionaries.
# I start off by looping through the list:
for dict in data["layers"]:

    # Next, I loop through the key-value pairs in each dictionary:
    for k, v in dict.items():

        # I only stop to have a closer look
        # if the key is equal to what we want to change, "minzoom":
        if k == "minzoom":

            # Subtract 2 from the current value--
            # in other words, lower the minimum zoom value by two,
            # and set that as the new value for the current key:
            dict[k] = v - 2

            # Print statement to tell me what values were updated:
            print(f"Changed val from {v} to {v-2}")

# That's all folks! My JSON has been updated;
# the only thing left to do is save it as a new file:
with open(newstyle, 'w') as ns:
    json.dump(data, ns)

# The NEW and updated JSON file has magically appeared with the name and directory
# I specified when I created the variable name.