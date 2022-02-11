import matplotlib.pyplot as plt

from skimage import data
from skimage import io
from skimage.color import rgb2hsv
from skimage.color import hsv2rgb

# img = io.imread('air-balloon.jpg')
rgb_img = io.imread('rainbow-sea.jpg')
hsv_img = rgb2hsv(rgb_img)
hue_img = hsv_img[:, :, 0]
sat_img = hsv_img[:, :, 1]
# val_img = hsv_img[:, :, 2]

fig, (axo, axa) = plt.subplots(ncols=2, figsize=(8, 2))

axo.hist(hue_img.ravel(), bins=256)
axo.set_title('original')

# blue only
blue = (hue_img > 0.6) & (hue_img < 0.8)
sat_img[~blue] = 0

# alter image
rgb_img = hsv2rgb(hsv_img)
hsv_img = rgb2hsv(rgb_img)
hue_img = hsv_img[:, :, 0]

axa.hist(hue_img.ravel(), bins=256)
axa.set_title('altered')

fig.supxlabel('hue')
fig.supylabel('count')
fig.tight_layout()
plt.show()
