
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


rawdata=np.fromfile('C:\\Users\\AI-00\\Desktop\\Lena512.raw',dtype=np.uint8)
print("Raw data:",rawdata.shape)
imgRaw=rawdata.reshape([512,512])
print("Image raw data: ",imgRaw.shape)


# In[5]:


import matplotlib.pyplot as plt
plt.imshow(imgRaw,cmap="gray")
plt.show()


# In[8]:


imgHeight=512
imgWidth=512
newImgHeight=1024
newImgWidth=1024
imgScale=int(newImgHeight/imgHeight)
newImgRaw=np.zeros((1024,1024))


# In[9]:


for i_new in range(0,newImgHeight,2):
    for j_new in range(0,newImgWidth,2):
        i=int(i_new/imgScale)
        j=int(j_new/imgScale)
        newImgRaw[i_new,j_new]=imgRaw[i,j]
        newImgRaw[i_new,j_new+1]=imgRaw[i,j]
        newImgRaw[i_new+1,j_new]=imgRaw[i,j]
        newImgRaw[i_new+1,j_new+1]=imgRaw[i,j]


# In[10]:


newImgRaw

