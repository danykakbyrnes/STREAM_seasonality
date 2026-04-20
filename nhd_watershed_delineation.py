# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:33:19 2026

@author: dkbyrnes
"""

# This script is not used to produce any watersheds, since they were
# already all available. 

from pynhd import NLDI
from config import *

watershed_is_names = {'05484000':'STREAM-gauge-3100.shp'}

nldi = NLDI()
for gage_id, name in watershed_is_names.items():
    

    # Get basin boundary for a USGS gage
    basin = nldi.get_basins(gage_id, split_catchment=True, simplified=False)
    
    # add source as metadata
    basin["source"] = "NLDI_NHDPlusv2.1"
    
    gage = nldi.getfeature_byid("nwissite", 'USGS-'+gage_id)

    print(f"Station ID {gage_id}: {gage.geometry.y.iloc[0]},{gage.geometry.x.iloc[0]}")
    # Reproject to equal-area projection and calculate area in km²
    area_km2 = basin.to_crs("EPSG:5070").area.iloc[0] / 1e6
    print(f"Station ID {gage_id} area: {area_km2:.1f} km^2")
    
    flowlines = nldi.navigate_byid(
        fsource="nwissite",
        fid="USGS-06800500",
        navigation="upstreamTributaries",
        source="flowlines",
        distance=9999
    )
    
    # Save file
    basin.to_file(shapefile_filepath+name)
    #flowlines.to_file("elkhorn_rv_flowlines.shp")