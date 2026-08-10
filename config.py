# Input and Output filepath
INPUT_filepath = "../INPUT/"
OUTPUT_filepath = "../OUTPUT/"
metadata_filepath = INPUT_filepath+"01_metadata/metadata.csv"
shapefile_filepath = INPUT_filepath+'03_shapefiles/'
anc_data_filepath = INPUT_filepath+"00_additional_data/"
load_filepath = INPUT_filepath+"02_water_quality_data/"
land_use_filepath = INPUT_filepath+"06_dynamic_lulc/"
anthropogenic_filepath = INPUT_filepath+"07_dynamic_anthropogenic"

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

CROP_ID = {
    'crop_0': 'Background',
    'crop_1': 'Corn',
    'crop_2': 'Cotton',
    'crop_3': 'Rice',
    'crop_4': 'Sorghum',
    'crop_5': 'Soybeans',
    'crop_6': 'Sunflower',
    'crop_10': 'Peanuts',
    'crop_11': 'Tobacco',
    'crop_12': 'Sweet_Corn',
    'crop_13': 'Popcorn',
    'crop_14': 'Mint',
    'crop_21': 'Barley',
    'crop_22': 'Durum_Wheat',
    'crop_23': 'Spring_Wheat',
    'crop_24': 'Winter_Wheat',
    'crop_25': 'Other_Small_Grains',
    'crop_26': 'Dbl_Crop_WinWht_Soybeans',
    'crop_27': 'Rye',
    'crop_28': 'Oats',
    'crop_29': 'Millet',
    'crop_30': 'Speltz',
    'crop_31': 'Canola',
    'crop_32': 'Flaxseed',
    'crop_33': 'Safflower',
    'crop_34': 'Rape_Seed',
    'crop_35': 'Mustard',
    'crop_36': 'Alfalfa',
    'crop_37': 'Other_Hay_Non_Alfalfa',
    'crop_38': 'Camelina',
    'crop_39': 'Buckwheat',
    'crop_41': 'Sugarbeets',
    'crop_42': 'Dry_Beans',
    'crop_43': 'Potatoes',
    'crop_44': 'Other_Crops',
    'crop_45': 'Sugarcane',
    'crop_46': 'Sweet_Potatoes',
    'crop_47': 'Misc_Vegs_and_Fruits',
    'crop_48': 'Watermelons',
    'crop_49': 'Onions',
    'crop_50': 'Cucumbers',
    'crop_51': 'Chick_Peas',
    'crop_52': 'Lentils',
    'crop_53': 'Peas',
    'crop_54': 'Tomatoes',
    'crop_55': 'Caneberries',
    'crop_56': 'Hops',
    'crop_57': 'Herbs',
    'crop_58': 'Clover_Wildflowers',
    'crop_59': 'Sod_Grass_Seed',
    'crop_60': 'Switchgrass',
    'crop_61': 'Fallow_Idle_Cropland',
    'crop_62': 'Pasture_Grass',
    'crop_63': 'Forest',
    'crop_64': 'Shrubland',
    'crop_65': 'Barren',
    'crop_66': 'Cherries',
    'crop_67': 'Peaches',
    'crop_68': 'Apples',
    'crop_69': 'Grapes',
    'crop_70': 'Christmas_Trees',
    'crop_71': 'Other_Tree_Crops',
    'crop_72': 'Citrus',
    'crop_74': 'Pecans',
    'crop_75': 'Almonds',
    'crop_76': 'Walnuts',
    'crop_77': 'Pears',
    'crop_81': 'Clouds_No_Data',
    'crop_82': 'Developed',
    'crop_83': 'Water',
    'crop_87': 'Wetlands',
    'crop_88': 'Nonag_Undefined',
    'crop_92': 'Aquaculture',
    'crop_111': 'Open_Water',
    'crop_112': 'Perennial_Ice_Snow',
    'crop_121': 'Developed_Open_Space',
    'crop_122': 'Developed_Low_Intensity',
    'crop_123': 'Developed_Med_Intensity',
    'crop_124': 'Developed_High_Intensity',
    'crop_131': 'Barren_131',
    'crop_141': 'Deciduous_Forest',
    'crop_142': 'Evergreen_Forest',
    'crop_143': 'Mixed_Forest',
    'crop_152': 'Shrubland_152',
    'crop_176': 'Grassland_Pasture',
    'crop_190': 'Woody_Wetlands',
    'crop_195': 'Herbaceous_Wetlands',
    'crop_204': 'Pistachios',
    'crop_205': 'Triticale',
    'crop_206': 'Carrots',
    'crop_207': 'Asparagus',
    'crop_208': 'Garlic',
    'crop_209': 'Cantaloupes',
    'crop_210': 'Prunes',
    'crop_211': 'Olives',
    'crop_212': 'Oranges',
    'crop_213': 'Honeydew_Melons',
    'crop_214': 'Broccoli',
    'crop_215': 'Avocados',
    'crop_216': 'Peppers',
    'crop_217': 'Pomegranates',
    'crop_218': 'Nectarines',
    'crop_219': 'Greens',
    'crop_220': 'Plums',
    'crop_221': 'Strawberries',
    'crop_222': 'Squash',
    'crop_223': 'Apricots',
    'crop_224': 'Vetch',
    'crop_225': 'Dbl_Crop_WinWht_Corn',
    'crop_226': 'Dbl_Crop_Oats_Corn',
    'crop_227': 'Lettuce',
    'crop_228': 'Dbl_Crop_Triticale_Corn',
    'crop_229': 'Pumpkins',
    'crop_230': 'Dbl_Crop_Lettuce_Durum_Wht',
    'crop_231': 'Dbl_Crop_Lettuce_Cantaloupe',
    'crop_232': 'Dbl_Crop_Lettuce_Cotton',
    'crop_233': 'Dbl_Crop_Lettuce_Barley',
    'crop_234': 'Dbl_Crop_Durum_Wht_Sorghum',
    'crop_235': 'Dbl_Crop_Barley_Sorghum',
    'crop_236': 'Dbl_Crop_WinWht_Sorghum',
    'crop_237': 'Dbl_Crop_Barley_Corn',
    'crop_238': 'Dbl_Crop_WinWht_Cotton',
    'crop_239': 'Dbl_Crop_Soybeans_Cotton',
    'crop_240': 'Dbl_Crop_Soybeans_Oats',
    'crop_241': 'Dbl_Crop_Corn_Soybeans',
    'crop_242': 'Blueberries',
    'crop_243': 'Cabbage',
    'crop_244': 'Cauliflower',
    'crop_245': 'Celery',
    'crop_246': 'Radishes',
    'crop_247': 'Turnips',
    'crop_248': 'Eggplants',
    'crop_249': 'Gourds',
    'crop_250': 'Cranberries',
    'crop_254': 'Dbl_Crop_Barley_Soybeans',
}