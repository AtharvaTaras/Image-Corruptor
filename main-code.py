from PIL import Image, ImageFilter, ImageOps
import os
from kuwahara_filter import kuwahara_filter

os.chdir('A:\Python Projects\cats\cute cat')
print(os.getcwd())

for f in os.listdir('.'):
    i = Image.open(f)

    # Apply Kuwahara filter
    i_kuwahara = kuwahara_filter(i)

    fn, fext = os.path.splitext(f)


    # Apply existing filters to the Kuwahara filtered image
    i2 = i_kuwahara.filter(ImageFilter.EDGE_ENHANCE_MORE)
    i5 = i2.filter(ImageFilter.EDGE_ENHANCE_MORE)
    i6 = ImageOps.posterize(i5, 4)
    i7 = ImageOps.posterize(i6, 4)

    i7.save('output/{}.jpg'.format(fn))

