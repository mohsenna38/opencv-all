import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

aks1 = Image.open('y0.5.png')
image1 = np.asarray(aks1)
plt.imshow(image1)
plt.show()
print(image1[0][0][0])
