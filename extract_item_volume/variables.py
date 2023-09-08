import os
#class dependent_vars:
"""
variables used in driver_main.py
output filepath: current working directory
output filename: item_volume
"""
output_path='C:/users/shrsriv/Desktop/ITP rework/'
op_filename= 'op for all images.xlsx'


"""
variables used in ocr_text_extract.py
path: folder to read images
"""
path='C:\\Users\\shrsriv\\Desktop\\ITP rework\\images\\'


"""
variables used in pre_processing.py
del_chars: list of special characters
li_unit: combination of all the different ways in which paddle ocr is reading the unit of measurement
"""
del_chars = ['(', ')', '#', '&', ';', '%', '\"', "\'", '[', ']', '*', ',', '-', '_', '!', ':', '+', '\\', '/', '|']

###FL OZ, FL OZ, II OZ, FL.OZ . added in the list dated: 16th march

li_unit=['FL','F1','FI','FLOZ','FL.OZ.','FL. OZ.','FL.OZ','F.OZ','FL.O','FL.Z','F1OZ','FI0Z','FIOZ','F10Z','F.O','F1.OZ','F1.0Z.','F1.0Z','FOZ','FL O','FL 0','FL.Z','FL.OZ.','FLUID','ML','MILLILITRES','MLS','MILLILITRE','MILLI','LITRES','LITRE','LT.','LT','LTS','LTRS','PINT','PT','PINTS','QUARTS','QUART','QT','GALLON','GALLONS','GAL','L', 'FL OZ', 'FL OZ ','PTS','II OZ','FL.OZ .']


"""
variables used in post_processing.py
"""
## added 3 more units dated: 16th march 'FL OZ', 'FL OZ ','II OZ' in floz
fl_oz = [ 'FL OZ', 'FL.OZ','FL.OZ ', 'FOZ', 'FL OZ/', 'FL0Z', 'FL. OZ', 'FL.Z', 'FL.OZ.|', 'FL. OZ.', 'FL. OZ. ',
         'FL Z', 'FOZ', 'F/OZ', 'F OZ/', 'FL.','FLOZ','FLO','FI.OZ.','FL 02','F 02','FL OZ', 'FL OZ ','II OZ','FL.OZ .']
ml = ['ML', 'MILLI LITRES', 'M.L.', 'ML.', 'MILLILITRE','ML ']
litre = ['LTS', 'LITRE', 'LITRES', 'LT.', 'L', 'LT']
gallon = ['GALLON', 'GAL', 'GALS', 'GALLONS', 'GAL.']
pint = ['PINT', 'PINTS', 'PT.', 'PTS', 'PT']
quart = ['QUARTS', 'QT', 'QUART']
final_units = ['floz', 'fluid', 'ounce', 'ml', 'quart', 'pint', 'litre', 'gallon']

#### limit dictionary for PT: Pets&Pest control
limit_dict={
            'fl_oz': 80,
            'ml': 1300,
            'litre': 30,
            'quart':2,
            'pint':2,
            'gallon':2,

        }