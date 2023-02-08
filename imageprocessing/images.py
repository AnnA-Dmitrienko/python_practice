from PIL import Image, ImageFilter

img = Image.open('pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SHARPEN)
# print(dir(img))
#png supports the image filters 
filtered_img= img.convert('L') #grayscale
filtered_img.save("gray.png", 'png')
