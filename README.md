# Image-Corruptor

<br>Python program that tries to corrupt images, while still maintaining some original aspects of the image.</br>
Python 3.6x. Requires PIL and os modules.
<br>Works by applying a Kuwahara filter, over-enhancing edges, and then adding multiple posterize effects.</br>

![alt text](https://gcdn.pbrd.co/images/AR7mlvMAbM0Z.jpg?o=1)

## Kuwahara Filter
The Kuwahara filter is an edge-preserving smoothing filter that reduces noise in an image while preserving sharp edges. It works by dividing a window around each pixel into four overlapping sub-regions, calculating the mean and variance for each sub-region, and then replacing the pixel's value with the mean of the sub-region with the smallest variance.

### Installation
In addition to PIL and os, this project now requires `numpy` and `scipy`.
You can install them using pip:
`pip install numpy scipy`


