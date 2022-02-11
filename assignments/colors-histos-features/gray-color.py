import matplotlib.pyplot as plt

from skimage import data
from skimage import io
from skimage.color import rgb2hsv
from skimage.color import hsv2rgb

# rgb_img = io.imread('air-balloon.jpg')
rgb_img = io.imread('rainbow-sea.jpg')
hsv_img = rgb2hsv(rgb_img)
hue_img = hsv_img[:, :, 0]
sat_img = hsv_img[:, :, 1]
# val_img = hsv_img[:, :, 2]

# red only
# red = (hue_img > 0.9) | (hue_img < 0.1)
# sat_img[~red] = 0

# green only
# green = (hue_img > 0.3) & (hue_img < 0.5)
# sat_img[~green] = 0

# blue only
blue = (hue_img > 0.6) & (hue_img < 0.8)
sat_img[~blue] = 0

plt.imshow(hsv2rgb(hsv_img))
plt.axis('off')
plt.show()
