from skimage import data, feature
from matplotlib import pyplot as plt


def show_image(img, name='', cmap='gray'):
    plt.imshow(img, cmap)
    plt.title(name)
    plt.axis('off')
    plt.show()


show_image(feature.canny(data.camera(), 2, 80, 90), 'canny')
