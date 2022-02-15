import numpy as np
from skimage import data
from scipy import ndimage
from matplotlib import pyplot as plt


def apply_filter(kx, ky, img=data.camera()):
    img = np.asarray(img, dtype="int32")
    gx  = ndimage.convolve(img, kx)
    gy  = ndimage.convolve(img, ky)
    img = np.sqrt(np.square(gx) + np.square(gy))
    return np.asarray(np.clip(img, 0, 255), dtype="uint8")


def show_image(img, name='', cmap='gray'):
    plt.imshow(img, cmap)
    plt.title(name)
    plt.axis('off')
    plt.show()


sobel_mask = (
    np.array([
        [-1, 0,+1],
        [-2, 0,+2],
        [-1, 0,+1]]),
    np.array([
        [-1,-2,-1],
        [ 0, 0, 0],
        [+1,+2,+1]]))
show_image(apply_filter(*sobel_mask), 'sobel')

prewitt_mask = (
    np.array([
        [+1, 0,-1],
        [+1, 0,-1],
        [+1, 0,-1]]),
    np.array([
        [+1,+1,+1],
        [ 0, 0, 0],
        [-1,-1,-1]]))
show_image(apply_filter(*prewitt_mask), 'prewitt')

roberts_mask = (
    np.array([
        [0, 0, 0],
        [0,+1, 0],
        [0, 0,-1]]),
    np.array([
        [0, 0, 0],
        [0, 0,+1],
        [0,-1, 0]]))
show_image(apply_filter(*roberts_mask), 'roberts')

