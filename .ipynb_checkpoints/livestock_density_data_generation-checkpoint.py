# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:45:00 2026

@author: danyk
"""

import pandas as pd
import geopandas as gpd
from config import *
import rasterio
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

livestock_inv = pd.read_csv(INPUT_filepath+'00_additional_data/livestock_density/livestock_inventory.csv')

livestock_inv['AU'] = livestock_inv['Value'] / livestock_inv['ID'].map(au)
AU_density = livestock_inv.groupby(['YEAR', 'GEOID'])['AU'].sum().reset_index()

cnty_shapefile = gpd.read_file(INPUT_filepath+'00_additional_data/county_shp/US_CountyShapefile_2017.shp')
cnty_shapefile['GEOID'] = cnty_shapefile['GEOID'].astype(int)

wtsh_AU = []

for site in main_sites:
    site_shapfile_filepath = os.path.join(shapefile_filepath, f"{site}.shp")
    wtshd = gpd.read_file(site_shapfile_filepath)
        
    # Making sure the crs matches + and that it's in equal-area CRS
    wtshd = wtshd.to_crs(cnty_shapefile.crs)
    
    # watershed area
    wtshd_area = wtshd.area.sum()/1000000 # km2
    
    # Clipping county to watershed
    try:
        wtshd_county = gpd.clip(cnty_shapefile, wtshd)
    except Exception:
        wtshd_county = gpd.overlay(cnty_shapefile, wtshd, how='intersection')

    # Calculate the fraction of the county contained within the watershed
    wtshd_county['frac_area'] = wtshd_county.area / (wtshd_county['AREA_HA'] * 10000)

    AU_density['GEOID'].isin(wtshd_county['GEOID'])
    wtshd_county = wtshd_county[['GEOID', 'frac_area']].merge(AU_density, on='GEOID', how='inner')

    # Area-weighted AU, then sum by year
    wtshd_county['AU_weighted'] = wtshd_county['AU'] * wtshd_county['frac_area']
    wtshd_year = wtshd_county.groupby('YEAR')['AU_weighted'].sum().reset_index()
    wtshd_year['AU_density'] = wtshd_year['AU_weighted']/(wtshd_area)
    wtshd_year['Site'] = site
    
    wtsh_AU.append(wtshd_year)
    
combined_AU = pd.concat(wtsh_AU, ignore_index=True)

combined_AU.to_csv(INPUT_filepath+'00_additional_data/livestock_density/AU_density.csv')