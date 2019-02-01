import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

aks1 = Image.open('dot.png')
image1 = np.asarray(aks1)
plt.imshow(image1)
plt.show()
