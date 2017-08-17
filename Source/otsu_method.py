from PIL import Image
import numpy as np
import os, sys
import cv2
import glob

def total_pix(image):
  size = image.size[0] * image.size[1]
  return size
##Calculated intensity of each pixel 
##and get a histogram from intensity pixels
def histogramify(image):
  grayscale_array = []
  for w in range(0,image.size[0]):
    for h in range(0,image.size[1]):
      intensity = image.getpixel((w,h))
      grayscale_array.append(intensity)

  total_pixels = image.size[0] * image.size[1]
  bins = range(0,257)
  img_histogram = np.histogram(grayscale_array, bins)
  return img_histogram

##Get the image has been seperated two class by threshold t
##Image will be divided into 2 color black and white (Backgorund and Forground)
def threshold(dir_mainfolder, t, image, num):
  intensity_array = []
  for w in range(0,image.size[1]):
    for h in range(0,image.size[0]):
      intensity = image.getpixel((h,w))
      ##If the intensity of pixel smaller than threshold the pixel will be black
      if (intensity <= t):
        x = 0
      else:
        x = 255
      intensity_array.append(x)
  image.putdata(intensity_array)
  #image.show()  
  if (dir_mainfolder == "simple"):
      image.show()
  else:
      image.save(dir_mainfolder+"/img_otsu_handwrite/"+str(num)+".jpg")

def otsu(dir_mainfolder, image, num):
##Calculate histogram intensity from image
  hist = histogramify(image)
##Get total pixels in image
  total = total_pix(image)
  current_max, threshold_value = 0, 0
  sumT, sumF, sumB = 0, 0, 0
##Calculated the sum of weight intensity of image
  for i in range(0,256):
    sumT += i * hist[0][i]

  weightB, weightF = 0, 0
  varBetween, meanB, meanF = 0, 0, 0
  for i in range(0,256):
    ##Weight Background probability
    weightB += hist[0][i]
    ##Foreground probability
    weightF = total - weightB
    if weightF == 0:
      break

##Sum of weight intensity background and foreground
    sumB += i*hist[0][i]
    sumF = sumT - sumB
##Calculated the mean of Background and Foreground
    meanB = sumB/weightB
    meanF = sumF/weightF
##Calculate the variance with the threshold i
    varBetween = weightB * weightF
    varBetween *= (meanB-meanF)*(meanB-meanF)

##Get the max variance to have the best threshold value
    if varBetween > current_max:
      current_max = varBetween
      threshold_value = i 
      
  print "threshold value is:", threshold_value
  threshold(dir_mainfolder, threshold_value, image, num) 
  
def otsu_main(dir_mainfolder,k):
    num = 1
    cv_img = []
    ################
    ##Get all images from folder
    if k==0:
        for img2 in glob.glob(dir_mainfolder + "/img_meanshift/*.jpg"):
            im = Image.open(img2)
            cv_img.append(im)
    else:
        for img2 in glob.glob(dir_mainfolder + "/img_kmean_handwrite/*.jpg"):
            im = Image.open(img2)
            cv_img.append(im)
    for image in cv_img:
        bw = image.convert('L')
        otsu(dir_mainfolder, bw, num)
        num = num + 1

def simple_otsu(file_path):
    image = Image.open(file_path)
    bw = image.convert('L')
    otsu("simple", bw, 0)

