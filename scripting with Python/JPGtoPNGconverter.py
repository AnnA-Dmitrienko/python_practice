import sys
import os  # or pathlib module
from pathlib import Path

from PIL import Image

# grab the first and second arguments - sys module
arg1 = sys.argv[1]
arg2 = sys.argv[2]
# check if new exists, if not - create it
if not os.path.exists(arg2):
    os.makedirs(arg2)

# loop through pokedex - convert images to png
for filename in os.listdir(arg1):
    img = Image.open(f'{arg1}{filename}')
    # splits the text between the name and the extension
    clean_name = os.path.splitext(filename)[0]
    # print(clean_name)
    img.save(f'{arg2}{clean_name}.png', 'png')

print('all done!')
# # save them to a new folder
