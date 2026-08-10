# Input and Output filepath
INPUT_filepath = "../INPUT/"
OUTPUT_filepath = "../OUTPUT/"
metadata_filepath = INPUT_filepath+"01_metadata/metadata.csv"
shapefile_filepath = INPUT_filepath+'03_shapefiles/'
anc_data_filepath = INPUT_filepath+"00_additional_data/"
load_filepath = INPUT_filepath+"02_water_quality_data/"
land_use_filepath = INPUT_filepath+"06_dynamic_lulc/"


# Data metadata
START_YEAR = 2015

# SITE IDs
MAIN_SITES = ['STREAM-gauge-2891', #ok
            'STREAM-gauge-2886',#ok
            'STREAM-gauge-2903',#ok
            'STREAM-gauge-2962',#ok
            'STREAM-gauge-2963',#ok
            'STREAM-gauge-3092',#ok
            'STREAM-gauge-3096',#ok
            'STREAM-gauge-3097',#ok
            'STREAM-gauge-3077',#ok
            'STREAM-gauge-3089',#ok
            'STREAM-gauge-3100', #ok
            'STREAM-gauge-3108',#ok
            'STREAM-gauge-3109',#ok
            'STREAM-gauge-308',#ok
            'STREAM-gauge-2203',#ok
            'STREAM-gauge-4472',#ok
            'STREAM-gauge-4431',#ok
            'STREAM-gauge-4440',#ok
            'STREAM-gauge-4442', #error
            'STREAM-gauge-4465', #ok
            'STREAM-gauge-2804',#ok
            'STREAM-gauge-2816', #ok
            'STREAM-gauge-3776',#ok
            'STREAM-gauge-3809',#ok
            'STREAM-gauge-4881', # shatto 'STREAM-gauge-NA1',
            'STREAM-gauge-4882', # kirkpatrick 'STREAM-gauge-NA2',
            'STREAM-gauge-695', #ok
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
    'STREAM-gauge-4881':  'IN-SD',
    'STREAM-gauge-4882':  'IN-KD',
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