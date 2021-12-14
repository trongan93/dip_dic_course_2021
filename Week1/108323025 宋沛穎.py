

from matplotlib import pyplot as pit
import numpy as np
rawdata = np.fromfile("C:\\Users\\AI-00\\Pictures\\Saved Pictures\\lena_gray.raw",dtype=np.uint8)
imgRaw = rawdata.reshape([512,512])

new_imapeRaw = np.zeros((1024, 1024))

for i_new in range(0, 1024, 2):
    for j_new in range(0, 1024, 2):

        i = int(i_new/2)
        j = int(j_new/2)        
        new_imapeRaw[i_new, j_new] = imgRaw[i, j]
        new_imapeRaw[i_new+1, j_new] = imgRaw[i, j]
        new_imapeRaw[i_new, j_new+1] = imgRaw[i, j]
        new_imapeRaw[i_new+1, j_new+1] = imgRaw[i, j]
  
pit.imshow(new_imapeRaw, cmap="gray")



