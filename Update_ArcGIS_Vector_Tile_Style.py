# Script by Misti Wudtke | misti@aldermaps.com | hub.aldermaps.com
# From the repo: https://github.com/AlderMaps/python-misc

# The purpose of this script is to provide a way to update ALL values of a given key
# in the JSON style object of an Esri basemap (as downloaded from Vector Tile Style Editor)
# This particular script updates the value for all instance of the key "minzoom"
# but could easily be modified to update other key-value pairs as needed.

# NOTE: To update the JSON in my style in AGOL, I open the "newstyle" file
# (the output file of this script), and copy / paste the whole thing
# directly into the JSON viewer in Vector Tile Style Editor, then save the style.
# I think I should be able to update it on the style Item page too...
# ...but this has produced...unexpected results. XD 
# I have not pinned down why. Works just fine in the Tile Style editor though!

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

            # If I'm at a small scale (i.e. zoomed far out),
            # I don't want to change the minzoom *quite as much*
            # as if I'm at a large scale (zoomed farther in).
            # So I check if the current minzoom value is less than 10:
            if v < 10:

                # If it is, subtract 2 from the current value
                # and set that as the new value for the current key:
                dict[k] = v - 2

                # Print statement to tell me what values were updated:
                print(f"Changed val from {v} to {v-2}")

            # Now I deal with any values of minzoom greater than or equal to 10:
            else:

                # In this case I want to decrease the minvalue by 3 instead of 2:
                dict[k] = v - 3

                # Again, print statement to keep track of changes:
                print(f"Changed val from {v} to {v-3}")

# That's all folks! My JSON has been updated;
# the only thing left to do is save it as a new file:
with open(newstyle, 'w') as ns:
    json.dump(data, ns)

# The NEW and updated JSON file has magically appeared with the name and directory
# I specified when I created the variable name.