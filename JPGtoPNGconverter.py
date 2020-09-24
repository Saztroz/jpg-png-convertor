import sys
import os
from PIL import Image

#grab first and s econd argument from sys import #pokedex and #new folder
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if new\ exists and if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through pokedex, convert images to PNG
#save them to new folder

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done')

#pass arguments in terminal python JPGtoPNGconverter.py Pokedex\ new\