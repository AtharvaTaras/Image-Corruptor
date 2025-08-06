import numpy as np
from scipy.ndimage import uniform_filter
from PIL import Image

def kuwahara_filter(image: Image.Image, radius: int = 3) -> Image.Image:
    """
    Applies the Kuwahara filter to a PIL Image.

    Args:
        image: The input PIL Image.
        radius: The radius of the filter window. The window size will be (2*radius + 1)x(2*radius + 1).

    Returns:
        A new PIL Image with the Kuwahara filter applied.
    """
    img_array = np.array(image).astype(float)
    output_array = np.zeros_like(img_array)

    # Handle grayscale and color images
    if img_array.ndim == 2:
        img_array = img_array[:, :, np.newaxis] # Add a channel dimension for consistency

    height, width, channels = img_array.shape

    for c in range(channels):
        channel_data = img_array[:, :, c]
        
        # Calculate squared values for variance calculation
        squared_channel_data = channel_data ** 2

        # Iterate over each pixel
        for i in range(height):
            for j in range(width):
                min_variance = float('inf')
                best_mean = 0

                # Define the four overlapping sub-regions
                regions = [
                    channel_data[max(0, i - radius):min(height, i + 1), max(0, j - radius):min(width, j + 1)], # Top-left
