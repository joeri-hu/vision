from skimage import data, filters
from matplotlib import pyplot as plt


def show_image(img, name='', cmap='gray'):
    plt.imshow(img, cmap)
    plt.title(name)
    plt.axis('off')
    plt.show()


show_image(filters.sobel(data.camera()), 'sobel')
show_image(filters.prewitt(data.camera()), 'prewitt')
show_image(filters.roberts(data.camera()), 'roberts')

# Wat valt je op als je de resultaten van de eerste opdracht
# met de tweede opdracht vergelijkt?
# De edges van de eerste opdracht zijn een stuk feller.
