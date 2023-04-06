import glob
import os
from skimage.io import imsave
str1 = 'female/'
str2 = 'male/'
str3 = 'train/'

img_list = glob.glob(str2 + '*.jpg.jpg')
print(img_list)
for i, img_path in enumerate(img_list):
    (filepath, tempfilename) = os.path.split(img_path)
    (Myfilename, extension) = os.path.splitext(tempfilename)

    a = open(str3 + Myfilename +'.txt', 'w')
    a.write("1 0.500000 0.500000 1.000000 1.000000")
    a.close()