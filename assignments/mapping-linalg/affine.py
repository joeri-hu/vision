from skimage import data, transform
from matplotlib import pyplot as plt
import numpy as np

img = data.coffee()
rot = transform.AffineTransform(rotation=np.pi/5)
tlan = transform.AffineTransform(translation=(55,77))
scl = transform.AffineTransform(scale=1/3)
img_rot = transform.warp(img, rot)
img_tlan = transform.warp(img, tlan)
img_scl = transform.warp(img, scl)

fig, ax = plt.subplots(nrows=4)
ax[0].imshow(img)
ax[0].set_title('original')
ax[0].set_axis_off()
ax[1].imshow(img_rot)
ax[1].set_title('rotated')
ax[1].set_axis_off()
ax[2].imshow(img_tlan)
ax[2].set_title('translated')
ax[2].set_axis_off()
ax[3].imshow(img_scl)
ax[3].set_title('stretched')
ax[3].set_axis_off()
plt.show()
