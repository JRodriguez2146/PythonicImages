from PIL import Image, ImageEnhance, ImageFilter 
import os

path = './Scripts/imgs'
pathOut = './PythonicImages/Scripts/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    #Sharpen image
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

    #Contrast image
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')























