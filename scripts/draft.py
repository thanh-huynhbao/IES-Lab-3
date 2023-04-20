import numpy as np

kernel = np.zeros((5,5),np.float32)
kernel[2][2] = -1
print(kernel)
