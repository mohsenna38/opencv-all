import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import test3
#############################################################
aks1 = Image.open('y0.5.png')
image1 = np.asarray(aks1)
test3.arraymin(image1)
print(image1)
#plt.imshow(image1)
#plt.show()
