# Input and Output filepath
INPUT_filepath = "../INPUT/"
OUTPUT_filepath = "../OUTPUT/"
metadata_filepath = INPUT_filepath+"01_metadata/metadata.csv"
shapefile_filepath = INPUT_filepath+'03_shapefiles/'
anc_data_filepath = INPUT_filepath+"00_additional_data/"
load_filepath = INPUT_filepath+"02_water_quality_data/"
land_use_filepath = INPUT_filepath+"07_dynamic_lulc/"

# Data metadata
START_YEAR = 2015

# SITE IDs
MAIN_SITES = ['STREAM-gauge-2891',
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
            #'STREAM-gauge-692', Platte River which has an outlier
            'STREAM-gauge-695'
]

# Names for stations
SHORTHAND_NAMES = {
    'STREAM-gauge-2891': 'IL-EM',
    'STREAM-gauge-2886': 'IL-SP',
    'STREAM-gauge-2903': 'IL-DP',
    'STREAM-gauge-2962': 'IL-KA',
    'STREAM-gauge-2963': 'IL-BM',
    'STREAM-gauge-3092': 'IA-IA',
    'STREAM-gauge-3096': 'IA-DM',
    'STREAM-gauge-3097': 'IA-NR',
    'STREAM-gauge-3077': 'IA-TR',
    'STREAM-gauge-3089': 'IA-CR',
    'STREAM-gauge-3100': 'IA-SR',
    'STREAM-gauge-3108': 'IA-NI',
    'STREAM-gauge-3109': 'IA-NO',
    'STREAM-gauge-308':  'LA-MS',
    'STREAM-gauge-2203': 'MO-MO',
    'STREAM-gauge-4472': 'IN-IR',
    'STREAM-gauge-4431': 'IN-WW',
    'STREAM-gauge-4440': 'IN-EC',
    'STREAM-gauge-4442': 'IN-SB',
    'STREAM-gauge-4465': 'IN-KA',
    'STREAM-gauge-2804': 'KS-KS',
    'STREAM-gauge-2816': 'KS-LA',
    'STREAM-gauge-3776': 'KY-GR',
    'STREAM-gauge-3809': 'OH-OH',
    'STREAM-gauge-NA1':  'IN-SD',
    'STREAM-gauge-NA2':  'IN-KD',
    'STREAM-gauge-695':  'NE-ER',
    'STREAM-gauge-692':  'NE-PR',
}

# Animal units. Workbook is found i Inputs > 00_additional_data > livestock_density > AU_animal_workbook.xlsx
AU = {1047:0.83, # Beef cow
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