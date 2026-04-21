# Input and Output filepath
INPUT_filepath = "../INPUT/"
OUTPUT_filepath = "../OUTPUT/"
metadata_filepath = INPUT_filepath+"01_metadata/metadata.csv"
shapefile_filepath = INPUT_filepath+'03_shapefiles/'
anc_data_filepath = INPUT_filepath+"00_additional_data/"
load_filepath = INPUT_filepath+"02_water_quality_data/load_flex_filled/"
land_use_filepath = INPUT_filepath+"07_dynamic_lulc/"

# Data metadata
start_year = 2008

# SITE IDs
main_sites=['STREAM-gauge-2891',
            'STREAM-gauge-2886',
            'STREAM-gauge-2903',
            'STREAM-gauge-2962',
            'STREAM-gauge-2963',
            'STREAM-gauge-3092',
            'STREAM-gauge-3096',
            'STREAM-gauge-3097',
            'STREAM-gauge-3077',
            'STREAM-gauge-3089',
            'STREAM-gauge-3100', #error
            'STREAM-gauge-3108',
            'STREAM-gauge-3109',
            'STREAM-gauge-308',
            'STREAM-gauge-2203',
            'STREAM-gauge-4472',
            'STREAM-gauge-4431',
            'STREAM-gauge-4440',
            'STREAM-gauge-4442', #error
            'STREAM-gauge-4465',
            'STREAM-gauge-2804',
            'STREAM-gauge-2816',
            'STREAM-gauge-3776',
            'STREAM-gauge-3809',
            'STREAM-gauge-NA1',
            'STREAM-gauge-NA2',
            'STREAM-gauge-692',
            'STREAM-gauge-695'
]

site_name_dict = []

# Animal units. Workbook is found i Inputs > 00_additional_data > livestock_density > AU_animal_workbook.xlsx
au = {1047:0.83, # Beef cow
      2047:0.74, # Milk cow
      5047:1.26, # Other cattle
      1051:8.57, # Hogs + pigs
      1048:455, # Broilers
      2048:250, # Layers and pullets
      1050:10, # Goats
      1053:10, # Sheeps and lambs
      1055:0.91, # Horses and ponies
      1054:67, # Turkeys
      }