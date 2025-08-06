from PIL import Image, ImageFilter, ImageOps
import os
from kuwahara_filter import kuwahara_filter

input_image_path = 'images/cat.jpg'
output_directory = 'examples'
output_image_name = 'cat_example.jpg'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

i = Image.open(input_image_path)

    # Apply Kuwahara filter
i_kuwahara = kuwahara_filter(i)


    # Apply existing filters to the Kuwahara filtered image
i2 = i_kuwahara.filter(ImageFilter.EDGE_ENHANCE_MORE)
i5 = i2.filter(ImageFilter.EDGE_ENHANCE_MORE)
i6 = ImageOps.posterize(i5, 4)
i7 = ImageOps.posterize(i6, 4)

i7.save(os.path.join(output_directory, output_image_name))


