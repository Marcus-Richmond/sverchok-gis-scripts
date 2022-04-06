"""
in gpkg_path FP
in gpkg_layer s
out Vertices v
out Edges s
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
        for index2 in range(len(gi['features'][index]['geometry']['coordinates'][0])-1):
            
            new_x = gi['features'][index]['geometry']['coordinates'][0][index2][0]
            new_y = gi['features'][index]['geometry']['coordinates'][0][index2][1]
            new_z = 0
            
            new_vector = [new_x, new_y, new_z]

            Vertices_features_individual.append(new_vector)
        
        Vertices_features_all.append(Vertices_features_individual)
        
        Vertices_features_individual = []

    Vertices = Vertices_features_all

    # create empty lists to add new edges and polygons to
    Edges_features_individual = []
    Edges_features_all = []

    # for loop to create edges and polygons
    for index_edge in range(len(gi['features'])):
        for index_edge2 in range(len(gi['features'][index_edge]['geometry']['coordinates'][0])-1):
            
            v1 = index_edge2
            v2 = index_edge2 + 1

            # if statement to reset v2 once it reaches the last vertex
            if v2==len(gi['features'][index_edge]['geometry']['coordinates'][0])-1:
                v2=0
            
            # create edge
            e = (v1, v2)
            
            # append edge to edge list
            Edges_features_individual.append(e)
            
        
        
        Edges_features_all.append(Edges_features_individual)
        
        Edges_features_individual = []

    Edges = Edges_features_all
    
else:
    print("not executed yet because no filepath and/or layer was given")