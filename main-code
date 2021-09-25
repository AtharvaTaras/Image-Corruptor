from PIL import Image, ImageFilter, ImageOps
import os

os.chdir('A:\Python Projects\cats\cute cat')
print(os.getcwd())

for f in os.listdir('.'):
    i = Image.open(f)

    fn, fext = os.path.splitext(f)

    i2 = i.filter(ImageFilter.EDGE_ENHANCE_MORE)
    i5 = i2.filter(ImageFilter.EDGE_ENHANCE_MORE)
    i6 = ImageOps.posterize(i5, 4)
    i7 = ImageOps.posterize(i6, 4)

    i7.save('output/{}.jpg'.format(fn))
