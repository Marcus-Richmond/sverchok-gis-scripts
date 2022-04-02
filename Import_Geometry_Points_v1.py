"""
in gpkg_path FP
in gpkg_layer s
out Vertices v
"""

import geopandas as gpd
import pandas as pd
import fiona
import numpy as np

if gpkg_path and gpkg_layer:

    # read in gpkg layer as geopandas data frame
    gpd1 = gpd.read_file(gpkg_path[0][0], layer = gpkg_layer[0][0])

    # read in geometry of gpkg layer as geoseries
    gs = gpd.GeoSeries(gpd1["geometry"])

    # call geo interface method on geoseries
    gi = gs.__geo_interface__

    # create empty lists to add new vertices to
    Vertices_features_individual = []
    Vertices_features_all = []

    # for loop to create vertices
    for index in range(len(gi['features'])):
            
        new_x = gi['features'][index]['geometry']['coordinates'][0]
        new_y = gi['features'][index]['geometry']['coordinates'][1]
        new_z = 0
            
        new_vector = [new_x, new_y, new_z]

        Vertices_features_individual.append(new_vector)

    Vertices = [Vertices_features_individual]

else:
    print("not executed yet because no filepath and/or layer was given")