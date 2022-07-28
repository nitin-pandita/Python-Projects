#converting image to sketch 
from cv2 import blur
import numpy as np
import imageio
import scipy.ndimage
import cv2
import imageio.v2 as imageio
img = "demo.jpg"

def rgb2grey(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140]) #2-D array formula to convert image to gray scale

def dodge(front,back):
    final_sketch = front*255/(255-back)
    final_sketch[final_sketch > 255] = 255 # if size is greater than 255
    final_sketch[back== 255]=255
    #to convert any suitable existing col to categorical type as we will use aspect function
    return final_sketch.astype('uint8')
ss = imageio.imread(img) #used to read the image
gray = rgb2grey(ss)  #used to convert image to white and black

i = 255-gray #0,0,0 is for the darkest color and 255,255,255 is for brighest color which is probably white color 

 #to convert it into blur image
blur = scipy.ndimage.filters.gaussian_filter(i,sigma =15) #sigma is for intensity of blur of image
r = dodge(blur,gray) # this will convert image to sketch by taking two parameters as blur and gray

cv2.imwrite("myimage.png",r)