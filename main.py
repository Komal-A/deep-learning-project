import pandas as pd
import numpy as np
import PIL
from matplotlib.image import  imread
import os
import glob
import PIL 
from matplotlib.pyplot import imread, imshow
import matplotlib.image  as imr
import numpy as np



import xtarfile as tarfile
with open("C:\\University\\Year 3\\2nd Semester\\CSY3025- Artificial Intelligence\\2nd Term\\as-2\Dataset\\pairsDevTrain.txt","r") as f:
    pairs_train = f.read()

with open("C:\\University\\Year 3\\2nd Semester\\CSY3025- Artificial Intelligence\\2nd Term\\as-2\\Dataset\\pairsDevTrain.txt", "r") as f:
    pairs_test = f.read()

# with tarfile.open("C:\\University\\Year 3\\2nd Semester\\CSY3025- Artificial Intelligence\\2nd Term\\as-2\\Dataset\\lfw-funneled.tar", "r") as tar:
#     for member in tar.getmembers():
#       tar.extract(member, "C:\\University\\Year 3\\2nd Semester\\CSY3025- Artificial Intelligence\\2nd Term\\as-2\\Dataset\\data")


path = glob.glob(r"C:\University\Year 3\2nd Semester\CSY3025- Artificial Intelligence\2nd Term\as-2\Dataset\data\lfw_funneled/*/")
for i in path:
  if len(os.listdir(i)) >= 40:
    print(i) 
    print(len(os.listdir(i)))

for i in path:
  if len(os.listdir(i)) >= 40:
    image_list = os.listdir(i)
    for imag in image_list:
      img = imr.imread(i+imag)
      print(img.dtype)
      print(img.shape)


image_array = []
labels = []

for i in path:
  if len(os.listdir(i)) > 50:
    image_list = os.listdir(i)
    for imag in image_list:
      img = imr.imread(i+imag)
      label = i.split("\\")[-2]
      image_array.append(img)
      labels.append(label)

print(image_array)

print(labels)