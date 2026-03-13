# -*- coding: utf-8 -*-
"""
Septic Tank Density Calculator
Created for STREAM project

@author: dkbyrnes
"""

import os
import pandas as pd
import geopandas as gpd
import numpy as np
from tqdm import tqdm
from config import *

#%% Configuration - UPDATE THESE PATHS
INPUT_filepath = '../INPUT/'
shapefile_filepath = '../INPUT/03_shapefiles/'  # Update to your shapefile directory
OUTPUT_filepath = '../OUTPUT/'

#%% Load site list
# Read in shapefiles
# Get all shapefile names (without extension)
shapefile_names = [
    os.path.splitext(f)[0] 
    for f in os.listdir(shapefile_filepath) 
    if f.endswith('.shp')
]

# Check matches
ag_sites = [name for name in shapefile_names if name in main_sites]


print("\nResults:")
print(septic_df)

# Save to CSV
output_file = OUTPUT_filepath + 'septic_tank_density.csv'
septic_df.to_csv(output_file, index=False)
print(f"\nSaved to {output_file}")
