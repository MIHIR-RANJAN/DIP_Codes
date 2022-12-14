#LAB 1 - 

#Read and Display the Image

import cv2
img=cv2.imread("LAB1.jpeg")
cv2.imshow('Read and Display Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Resize the Image

import cv2
import numpy as np

img=cv2.imread('LAB1.jpeg')
h,w,c=img.shape
new_img=cv2.resize(img,(500,500))
cv2.imshow('Resized Image',new_img)

cv2.waitKey(0)

cv2.destroyAllWindows()


#Image into gray-scale

import cv2 
img=cv2.imread('LAB1.jpeg')
new_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray-Scaled Image",new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Image into black and white

import cv2 
img=cv2.imread('LAB1.jpeg')
# cv2.imshow('Original',img)
# cv2.waitKey(0)
new_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("changed",new_img)
# cv2.waitKey(0)
(thresh, blackAndWhiteImage) = cv2.threshold(new_img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Black white image', blackAndWhiteImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Image Profile

import cv2 
import numpy as np

img=cv2.imread("LAB1.jpeg")

size=img.shape
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 
address="/Users/apple/Desktop/code/Digital_Image_processing/wp3013104.jpeg"
print('Image Dimension    : ',size)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)
print("Resolution of image is :"+str(width) + "x" + str(height))
print("Image is located at-: "+address)

number_of_white_pix = np.sum(img == 255)
number_of_black_pix = np.sum(img == 0)
  
print('Number of white pixels:', number_of_white_pix)
print('Number of black pixels:', number_of_black_pix)




#RGB seperation

import cv2
img=cv2.imread('LAB1.jpeg')

red=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("Red Focused",red)
cv2.waitKey(0)  

red=cv2.cvtColor(img,cv2.COLOR_BGR2LUV)
cv2.imshow("Blue focused",red)
cv2.waitKey(0) 

red=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
cv2.imshow("Green focused",red)
cv2.waitKey(0) 

cv2.destroyAllWindows()


#Flow Control and loop


import cv2
num=int(input("please enter your number"))

img_0=cv2.imread("butterfly.jpeg")
img_1=cv2.imread("LAB1.jpeg")

if num==0:
    cv2.imshow("IMAGE-0",img_0)
    cv2.waitKey(0)
else:
    cv2.imshow("IMAGE_1",img_1)
    cv2.waitKey(0)

cv2.destroyAllWindows()

for i in range(num):
    print("iam in loop and this is the ",i)



#2-D image

import cv2 
import numpy as np 

arr = np.random.randint(0, 256, (400,400), dtype=np.uint8)
_,bw_image = cv2.threshold(arr, 128,255,cv2.THRESH_BINARY)

cv2.imshow("2D array image",bw_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



#LAB 2

#obtaining a negative image

import cv2
import numpy as np
img = cv2.imread('LAB2.jpg')
print(img.dtype)
img_neg = 255 - img
cv2.imshow('negative',img_neg)
cv2.waitKey(0)




#optaining a flip image

import cv2
path = r'LAB2.jpg'
src = cv2.imread(path)
window_name = 'Flip Image'
image = cv2.flip(src, 0)
cv2.imshow(window_name, image)
cv2.waitKey(0)




#contrast stretching of an image

import cv2
import numpy as np
img = cv2.imread('LAB2.jpg')
original = img.copy()
xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]
x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')
img = cv2.LUT(img, table)
cv2.imshow("original", original)
cv2.imshow("Contrast Stretcked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows() 




#thresholding of the image


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('LAB2.jpg',0)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()




#LAB 3

#Q1. Plot histogram 
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('/Users/snigdhaasthana/Desktop/my_image.jpeg',0) ??? plt.hist(img.ravel(),256,[0,256]);
plt.show()

#Q1. Histogram plot line 
import numpy as np 
import cv2 as cv 
from matplotlib import pyplot as plt 
img = cv.imread('/Users/snigdhaasthana/Desktop/my_image.jpeg') 
color = ('b','g','r') 
for i,col in enumerate(color): 
histr = cv.calcHist([img],[i],None,[256],[0,256]) plt.plot(histr,color = col)plt.xlim([0,256]) ??? plt.show() 


#Q1. Histogram with or without mask 

import cv2 as cv		import numpy as np		from matplotlib import pyplot as plt		img = cv.imread('/Users/snigdhaasthana/Desktop/my_image.jpeg',0) 
mask = np.zeros(img.shape[:2], np.uint8)                mask[100:300, 100:400] = 255                masked_img = cv.bitwise_and(img,img,mask = mask) 
hist_full = cv.calcHist([img],[0],None,[256],[0,256]) hist_mask = cv.calcHist([img],[0],mask,[256],[0,256]) 
plt.subplot(221),
plt.imshow(img, 'gray')
plt.subplot(222), 
plt.imshow(mask,'gray') 
plt.subplot(223), 
plt.imshow(masked_img, 'gray') 
plt.subplot(224), 
plt.plot(hist_full),
plt.plot(hist_mask) 
plt.xlim([0,256]) 
plt.show() 


#histogram equalization 

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('/Users/snigdhaasthana/Desktop/my_image.jpeg',0) hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max() 
plt.plot(cdf_normalized, color = 'b') 
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

##Q2 b. histogram equalization of low contrast image 

import cv2 
import numpy as npimg = cv2.imread('/Users/snigdhaasthana/Desktop/low_contr', 0) 
equ = cv2.equalizeHist(img) 
res = np.hstack((img, equ)) 
cv2.imshow('image',res) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

#Q3 Arithmetic operations Add
 
import cv2 
import numpy as np 
image1 = cv2.imread('/Users/snigdhaasthana/Desktop/img1.jpeg') 
image2 = cv2.imread('/Users/snigdhaasthana/Desktop/img2.jpeg') 
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0) 
cv2.imshow('Weighted Image', weightedSum) 
if cv2.waitKey(0) & 0xff == 27: 
cv2.destroyAllWindows() 

#Q3 subtraction 

import cv2 
import numpy as np 
img1 = cv2.imread('/Users/snigdhaasthana/Desktop/img1.jpeg') 
img2 = cv2.imread('/Users/snigdhaasthana/Desktop/img2.jpeg') 
sub = cv2.subtract(img1, img2) 
cv2.imshow('substract',sub) 
if cv2.waitKey(0) & 0xff == 27: 
cv2.destroyAllWindows() 



#Q3 Multiple
 
#multiply 
import cv2 
import numpy as np 
img1 = cv2.imread('/Users/snigdhaasthana/Desktop/img1.jpeg') 
img2 = cv2.imread('/Users/snigdhaasthana/Desktop/img2.jpeg') 
mul = cv2.multiply(img1, img2) 
cv2.imshow('multiply',mul) 
if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
	
#Q3 division 
#division 
import cv2 
import numpy as np 
img1 = cv2.imread('/Users/snigdhaasthana/Desktop/img1.jpeg') 
img2 = cv2.imread('/Users/snigdhaasthana/Desktop/img2.jpeg') 
div = cv2.divide(img1, img2) 
cv2.imshow('division',div) 
if cv2.waitKey(0) & 0xff == 27: 
cv2.destroyAllWindows() 


#LAB 4

#Write and execute programs for image logical operator. 

#1.1 AND operation between two image. 
import cv2
import numpy as np
img1 = cv2.imread('LAB_1.1.png') 
img2 = cv2.imread('LAB_1.2.jpeg')
dest_and = cv2.bitwise_and(img2, img1, mask = None)
cv2.imshow('LOGICAL AND', dest_and)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()


#1.2 OR operation between two image. 
import cv2
import numpy as np 
img1 = cv2.imread('LAB_1.1.png') 
img2 = cv2.imread('LAB_1.2.jpeg')
dest_or = cv2.bitwise_or(img2, img1, mask = None)
cv2.imshow('LOGICAL OR', dest_or)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()



#1.3 Water marking using EX-OR operation 
#1.3
import cv2
logo = cv2.imread("LAB_1.1.png")
img = cv2.imread("LAB_1.2.jpeg")
h_logo, w_logo, _ = logo.shape
h_img, w_img, _ = img.shape
center_y = int(h_img/2)
center_x = int(w_img/2)
top_y = center_y - int(h_logo/2)
left_x = center_x - int(w_logo/2)
bottom_y = top_y + h_logo
right_x = left_x + w_logo
destination = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(destination, 1, logo, 0.5, 0)
img[top_y:bottom_y, left_x:right_x] = result
cv2.imwrite("watermarked.jpg", img)
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#1.4 NOT operation (Negative image) 
#1.4
import cv2
import numpy as np
img1 = cv2.imread('LAB_1.1.png')
img2 = cv2.imread('LAB_1.2.jpeg')
dest_not1 = cv2.bitwise_not(img1, mask = None)
dest_not2 = cv2.bitwise_not(img2, mask = None)
cv2.imshow('LOGICAL NOT on image 1', dest_not1)
cv2.imshow('LOGICAL NOT on image 2', dest_not2)
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()


#1.5 Calculate intersection of two images 
#1.5
import cv2
img1 = cv2.imread('LAB_1.1.png',0)
img2 = cv2.imread('LAB_1.2.jpeg',0)
img_bwa = cv2.bitwise_and(img1,img2)
img_bwo = cv2.bitwise_or(img1,img2)
img_bwx = cv2.bitwise_xor(img1,img2)
cv2.imshow("LOGICAL AND of Image 1 and 2", img_bwa)
cv2.imshow("LOGICAL OR of Image 1 and 2", img_bwo)
cv2.imshow("LOGICAL XOR of Image 1 and 2", img_bwx)
cv2.waitKey(0)
cv2.destroyAllWindows()


#2. Write and execute programs for image frequency domain filtering. 

#2.1 Apply Fast Fourie Transformation(FFT) on any colour image. 
#2.1
import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

img_c1 = cv2.imread("LAB_2.jpeg", 0)
img_c2 = np.fft.fft2(img_c1)
img_c3 = np.fft.fftshift(img_c2)
img_c4 = np.fft.ifftshift(img_c3)
img_c5 = np.fft.ifft2(img_c4)

plt.subplot(151), plt.imshow(img_c1, "gray"), plt.title("Original Image")
plt.subplot(152), plt.imshow(np.log(1+np.abs(img_c2)), "gray"), plt.title("Spectrum")
plt.subplot(153), plt.imshow(np.log(1+np.abs(img_c3)), "gray"), plt.title("Centered Spectrum")
plt.subplot(154), plt.imshow(np.log(1+np.abs(img_c4)), "gray"), plt.title("Decentralized")
plt.subplot(155), plt.imshow(np.abs(img_c5), "gray"), plt.title("Processed Image")
plt.show()


#LAB 5

#Low pass filter - Mean filtering

import numpy as np
import pandas as pd
import cv2
img_root="Images/"
img = cv2.imread("LAB_5.jpeg",cv2.IMREAD_UNCHANGED)
kernel = np.ones((10,10),np.float32)/25
meanFilter = cv2.filter2D(img,-1,kernel)
cv2.imshow("Mean Filtered Image",np.hstack((img, meanFilter)))
cv2.waitKey(0)
cv2.destroyAllWindows()

#Low pass filter - Median filtering

import numpy as np
import pandas as pd
import cv2
img = cv2.imread("LAB_5.jpeg",cv2.IMREAD_UNCHANGED)
medianFilter = cv2.medianBlur(img,5)
cv2.imshow("Median Filter",np.hstack((img, medianFilter)))
cv2.waitKey(0)
cv2.destroyAllWindows()


#Low pass filter - Gaussian filter

import numpy as np
import pandas as pd
import cv2
img = cv2.imread("LAB_5.jpeg",cv2.IMREAD_UNCHANGED)
gaussBlur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("Gaussian Smoothing",np.hstack((img,gaussBlur)))
cv2.waitKey(0)
cv2.destroyAllWindows()



#High pass filter - Gaussian filter

import cv2
img = cv2.imread("LAB_5.jpeg")
img = cv2.resize(img, (680, 520),
interpolation=cv2.INTER_CUBIC)
hpf = img - cv2.GaussianBlur(img, (21, 21), 3)+127
cv2.imshow("Original", img)
cv2.imshow("High Passed Filter", hpf)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Homomorphic filter

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("LAB_5.jpeg")
img = np.float32(img)
img = img/255
rows,cols,dim=img.shape
rh, rl, cutoff = 2.5,0.5,32
imgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
y,cr,cb = cv2.split(imgYCrCb)
y_log = np.log(y+0.01)
y_fft = np.fft.fft2(y_log)
y_fft_shift = np.fft.fftshift(y_fft)
DX = cols/cutoff
G = np.ones((rows,cols))
for i in range(rows):
for j in range(cols):
G[i][j]=((rh-rl)*(1-np.exp(-((i-rows/2)**2+(j-cols/2)**2)/(2*DX**2))))+rl
result_filter = G * y_fft_shift
result_interm = np.real(np.fft.ifft2(np.fft.ifftshift(result_filter)))
result = np.exp(result_interm)
cv2.imshow("Homomorphic filtering",result)
cv2.waitKey(0)
cv2.destroyAllWindows()

#LAB 6

#Translation 

import cv2
import numpy as np
img = cv2.imread('img.png',cv2.IMREAD_COLOR)
rows,cols,channels = img.shape
M = np.float32([[1,0,50],[0,1,25]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Scaling 

import cv2
import numpy as np
img = cv2.imread('img.png')
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('img',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Upscale and Downscale 

import numpy as np
import cv2
img = cv2.imread('img.png', 1)
cv2.imshow('Original', img)
img_half = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('Half Image', img_half)
img = cv2.imread('img.png', 1)
cv2.imshow('Original', img)
img_scale_up = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)
cv2.imshow('Upscaled Image', img_scale_up)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Rotation 

import cv2
import numpy as np
img = cv2.imread('img.png',cv2.IMREAD_COLOR)
rows,cols,channels = img.shape
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Shrinking 

import cv2
import numpy as np
img = cv2.imread('img.png')
scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dsize = (width, height)
output = cv2.resize(img, dsize)
cv2.imshow('img',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Zooming 

import cv2
import numpy as np
img = cv2.imread('img.png')
scale_percent = 128
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dsize = (width, height)
output = cv2.resize(img, dsize)
cv2.imshow('Original',img)
cv2.imshow('Zoomed',output)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3x3 mask for low and high pass filters  

import cv2
import numpy as np
image = cv2.imread('img.png')
# Print error message if image is null
if image is None:
    print('Could not read image')
# Apply identity kernel
kernel1 = np.array([[0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
# Apply blurring kernel
kernel2 = np.ones((3, 3), np.float32) / 25
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
cv2.imshow('Original', image)
cv2.imshow('identity.jpg', identity)
cv2.imshow('Kernel Blur', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#LAB 7

#LAPLACE EDGE 

import sys
import cv2 as cv
def main(argv):
 ddepth = cv.CV_16S
 kernel_size = 3
 window_name = "Laplace Demo"
imageName = argv[0] if len(argv) > 0 else (r"C:\Users\kotip\OneDrive\Documents\SEM 3-1\DIP\Screenshot 2022-10-21 105428.jpg") 
    src = cv.imread(cv.samples.findFile(imageName), cv.IMREAD_COLOR) # Load an image
if src is None: 
        print ('Error opening image')
        print ('Program Arguments: [image_name -- default lena.jpg]')
        return -1 src = cv.GaussianBlur(src, (3, 3), 0)
   src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
  cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
   dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)
    abs_dst = cv.convertScaleAbs(dst)
     cv.imshow(window_name, abs_dst)
    cv.waitKey(0)
     return 0
if __name__ == "__main__":
    main(sys.argv[1:])



#PREWITT FILTER 

import cv2 
import numpy as npimg = cv2.imread(r"C:\Users\kotip\OneDrive\Documents\SEM 3-1\DIP\Screenshot 2022-10-21 105428.jpg")gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
cv2.imshow("Original Image", img)
cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Prewitt", img_prewittx + img_prewitty)
cv2.waitKey(0)
cv2.destroyAllWindows()



#SOBEL(HORIZONTAL AND VERTICAL)
 
import cv2
import numpy as np
img = cv2.imread(r"C:\Users\kotip\OneDrive\Documents\SEM 3-1\DIP\Screenshot 2022-10-21
105428.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely
cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", img_sobelx)
cv2.imshow("Sobel Y", img_sobely)
cv2.imshow("Sobel", img_sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()


#CANNY FILTER 

import cv2
import numpy as np
img = cv2.imread(r"C:\Users\kotip\OneDrive\Documents\SEM
3-1\DIP\Screenshot 2022-10-21 105428.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)
img_canny = cv2.Canny(img,100,200)
cv2.imshow("Original Image", img)
cv2.imshow("Canny", img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()


#ROBERTS FILTER 

import cv2
import numpy as np
from scipy import ndimage
from google.colab.patches import cv2_imshow
roberts_cross_v = np.array( [[1, 0 ],[0,-1 ]] )
roberts_cross_h = np.array( [[ 0, 1 ],[ -1, 0 ]] )
img = cv2.imread("/content/Screenshot 2022-10-21 105428.jpg",0).astype('float64')
img/=255.0
vertical = ndimage.convolve( img, roberts_cross_v )
horizontal = ndimage.convolve( img, roberts_cross_h )
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
edged_img*=255
cv2_imshow(edged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




#HOUGH TRANSFORM ( LINE) 

import cv2
import numpy as np
from google.colab.patches import cv2_imshow
img = cv2.imread('/content/react-table-tutorial-8378-01.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
for r_theta in lines:
    arr = np.array(r_theta[0], dtype=np.float64)
    r, theta = arr
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*r
    y0 = b*r
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
x2 = int(x0 - 1000*(-b))
y2 = int(y0 - 1000*(a))
cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv2_imshow( img)




#HOUGH TRANSFORM( CIRCLE) 

import numpy as np
import cv2 as cv
img = cv.imread(r"C:\Users\kotip\OneDrive\Documents\SEM 3-1\DIP\different-sized-circle-templates.jpg",0)
img = cv.medianBlur(img,5)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()