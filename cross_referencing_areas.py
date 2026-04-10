# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:27:02 2026

@author: dkbyrnes
"""

import pandas as pd
import geopandas as gpd
from config import *

md = pd.read_csv(metadata_filepath)

compare_areas = []
missing_watersheds = []

for idx, row in md.iterrows():
    site_id = row['STREAM_ID']
    md_area = row['drainagearea_sqkm']
    
    
    try:
        watrshed = gpd.read_file(shapefile_filepath+site_id+'.shp')
        
        
        calc_area = watrshed.to_crs("EPSG:5070").area.iloc[0] / 1e6
        prpt = md_area/calc_area
        
        compare_areas.append({
            'STREAM_ID': site_id,
            'md_Area_km2': md_area,
            'calc_Area_km2': calc_area,
            'md_to_calc_prop': prpt})
        
    except Exception:
        missing_watersheds.append(site_id)

result = pd.DataFrame(compare_areas)
result.to_csv('../OUTPUT/area_errors.csv')
