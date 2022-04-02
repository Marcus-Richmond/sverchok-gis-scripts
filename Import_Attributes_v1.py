"""
in gpkg_path FP
in gpkg_layer s
in layer_attribute s
out attribute_values s
"""

import geopandas as gpd
import pandas as pd
import fiona
import numpy as np

if gpkg_path and gpkg_layer and layer_attribute:
    
    # sanity check
    print(gpkg_path)
    
    # read in gpkg layer as geopandas data frame
    gpd1 = gpd.read_file(gpkg_path[0][0], layer = gpkg_layer[0][0])

    # call geo interface method on geodataframe
    gi = gpd1.__geo_interface__

    # variable to control which attribute is being extracted
    variableAttribute = layer_attribute[0][0]

    # create empty list to add attributes to
    listAttribute = []

    # loop through geointerface (gi) and extract values from the 'Integer' column, and add them to the list created above
    for features in range(len(gi['features'])):
        value = [gi['features'][features]['properties'][variableAttribute]]
        
        listAttribute.append(value)
        
    attribute_values = listAttribute
    
else:
    print("not executed yet because no filepath and/or layer was given")