import numpy as np
from PIL import Image, ImageStat
import cv2
import glob
import scipy as sp
from scipy.misc import imread
from scipy.signal.signaltools import correlate2d as c2d
from operator import itemgetter
from k_mean_algorithm import k_mean_main
from otsu_method import otsu_main

def librabyfunction_notuse():
###
#from skimage import graph, data, io, segmentation, color
#from skimage import future
#def ncut(dir_mainfolder):
#    cv_img = []
#    num = 1
#    ################
#    ##Get all images from folder
#    for img2 in glob.glob(dir_mainfolder + "/*.png"):
#        n= cv2.imread(img2)
#        cv_img.append(n)
#    for img2 in glob.glob(dir_mainfolder + "/*.jpg"):
#        n= cv2.imread(img2)
#        cv_img.append(n)
#    print "Go"
#    for img in cv_img:
#        print "jump"

#        labels = segmentation.slic(img, compactness=30, n_segments=400)

#        print "001" 
#        rag = future.graph.rag_mean_color(img, labels,mode='similarity')
#        print "002"
#        new_labels = future.graph.cut_normalized(labels, rag)
#        print "003"
#        out2 = color.label2rgb(new_labels, img, kind='avg')
#        print "004"
#        cv2.imwrite(dir_mainfolder+"/img_ncut/"+str(num)+".jpg",out2)
#        num=num+1
#    print "done"
#    compare(cv_img,dir_mainfolder,2)


#def k_mean(dir_mainfolder, K):
#    num = 1
#    cv_img = []
#    ################
#    ##Get all images from folder
#    for img2 in glob.glob(dir_mainfolder + "/*.png"):
#        n= cv2.imread(img2)
#        cv_img.append(n)
#    for img2 in glob.glob(dir_mainfolder + "/*.jpg"):
#        n= cv2.imread(img2)
#        cv_img.append(n)
#    for img in cv_img:
#        Z = img.reshape((-1,3))
#        # convert to np.float32
#        Z = np.float32(Z)
#        # define criteria, number of clusters(K) and apply kmeans()
#        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    
#        ret,label,center=cv2.kmeans(Z,K,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

#        # Now convert back into uint8, and make original image
#        center = np.uint8(center)
#        res = center[label.flatten()]
#        res2 = res.reshape((img.shape))
#        cv2.imwrite(dir_mainfolder+"/img_kmean/"+str(num)+".jpg",res2)

#        num=num+1
#    compare(cv_img,dir_mainfolder,0)

#def otsu(dir_mainfolder):
#    mean_shift(dir_mainfolder)
#    ##Read all iamges from folder
#    num = 1
#    cv_img = []
#    for img2 in glob.glob(dir_mainfolder + "/img_meanshift/*.jpg"):
#        n= cv2.imread(img2)
#        cv_img.append(n)
#    for image in cv_img:
#        # convert the mean shift image to grayscale, then apply
#        # Otsu's thresholding
#        gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
#        thresh = cv2.threshold(gray, 0, 255,
#	        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#        cv2.imwrite(dir_mainfolder+"/otsu/"+str(num)+".jpg",thresh)
#        num=num+1
#        print ("done")
#    print "done"
#    compare(cv_img,dir_mainfolder,1)
###

##Get and calculate inner product image
    print "This is library function"

def get(i,dir_mainfolder, flag):
    if flag == 1:
        data = imread(dir_mainfolder+'/img_kmean_handwrite/%s.jpg' % i)
    elif flag == 0:
        data = imread(dir_mainfolder+'/img_meanshift/%s.jpg' % i)

    data = cv2.resize(data, (100, 100))
    data = sp.inner(data, [299, 587, 114]) / 1000.0
    return (data - data.mean()) / data.std()

##Compare user image to all images
def compare_kmean(dir_mainfolder):
    ##Compare_ls: Store score of comparation between images
    compare_ls = []
    ##Base_img: Image draw from user
    print "get base"
    base_img = cv2.imread(dir_mainfolder + '/img_result/0.jpg')
    img0 = cv2.cvtColor(base_img,cv2.COLOR_BGR2RGB)
    hist_base = cv2.calcHist([img0], [0, 1, 2], None, [8, 8, 8],
		[0, 256, 0, 256, 0, 256])
    hist_base = cv2.normalize(hist_base).flatten()
    base_img = cv2.resize(base_img, (100, 100))

    ##Get inner product user draw image
    base_img = sp.inner(base_img, [299, 587, 114]) / 1000.0
    base_img = (base_img - base_img.mean()) / base_img.std()
    base_img.shape
    num = 1
    ##Compare the user draw image to all images
    list_img =[]
    for img2 in glob.glob(dir_mainfolder + "/*.jpg"):
        n= cv2.imread(img2)
        list_img.append(n)
    for img2 in glob.glob(dir_mainfolder + "/*.png"):
        n= cv2.imread(img2)
        list_img.append(n)
    print "jump for"
    for img in list_img:
        img = get(num,dir_mainfolder,1)
        img.shape

        print "compare"
        ##Use correlation 2d to compare between image
        compare_img = c2d(base_img, img, mode='same')
        value_c2d_pixel = compare_img.max()*0.4/1000
        
        ##Read image and calculated image histogram
        data = imread(dir_mainfolder+'/img_kmean_handwrite/%s.jpg' % num)
        img_1= cv2.cvtColor(data,cv2.COLOR_BGR2RGB)
        hist_img = cv2.calcHist([img_1], [0, 1, 2], None, [8, 8, 8],
		[0, 256, 0, 256, 0, 256])
        hist_img = cv2.normalize(hist_img).flatten()

        ##Comare histograms
        compare = cv2.compareHist(hist_base,hist_img,cv2.cv.CV_COMP_CORREL)
        compare = compare*0.6
        avg_value = (compare + value_c2d_pixel)/2
        compare_ls.append((num,avg_value))
        
        print "compare done"
        num = num + 1

    ##Sorting the score of comparation DESC
    compare_ls = sorted(compare_ls,key = itemgetter(1), reverse = True)
    i = 1
    
    ##Write ranking image to folder
    for ls in compare_ls:
        cv2.imwrite(dir_mainfolder+"/img_rank/"+str(i)+".jpg",list_img[ls[0] - 1])
        i = i+1

def compare_meanshift(dir_mainfolder):
    ##Compare_ls: Store score of comparation between images
    compare_ls = []
    ##Base_img: Image draw from user
    print "get base"
    base_img = cv2.imread(dir_mainfolder + '/img_result/0.jpg')
    img0 = cv2.cvtColor(base_img,cv2.COLOR_BGR2RGB)
    hist_base = cv2.calcHist([img0], [0, 1, 2], None, [8, 8, 8],
		[0, 256, 0, 256, 0, 256])
    hist_base = cv2.normalize(hist_base).flatten()
    base_img = cv2.resize(base_img, (100, 100))

    ##Get inner product user draw image
    base_img = sp.inner(base_img, [299, 587, 114]) / 1000.0
    base_img = (base_img - base_img.mean()) / base_img.std()
    base_img.shape
    num = 1
    ##Compare the user draw image to all images
    list_img =[]
    for img2 in glob.glob(dir_mainfolder + "/*.jpg"):
        n= cv2.imread(img2)
        list_img.append(n)
    for img2 in glob.glob(dir_mainfolder + "/*.png"):
        n= cv2.imread(img2)
        list_img.append(n)
    print "jump for"
    for img in list_img:
        img = get(num,dir_mainfolder,0)
        img.shape

        print "compare: " + num
        ##Use correlation 2d to compare between image
        compare_img = c2d(base_img, img, mode='same')
        value_c2d_pixel = compare_img.max()*0.4/1000
        
        ##Read image and calculated image histogram
        data = imread(dir_mainfolder+'/img_meanshift/%s.jpg' % num)
        img_1= cv2.cvtColor(data,cv2.COLOR_BGR2RGB)
        hist_img = cv2.calcHist([img_1], [0, 1, 2], None, [8, 8, 8],
		[0, 256, 0, 256, 0, 256])
        hist_img = cv2.normalize(hist_img).flatten()

        ##Comare histograms
        compare = cv2.compareHist(hist_base,hist_img,cv2.cv.CV_COMP_CORREL)
        compare = compare*0.6
        avg_value = (compare + value_c2d_pixel)/2
        compare_ls.append((num,avg_value))
        
        print "compare done"
        num = num + 1

    ##Sorting the score of comparation DESC
    compare_ls = sorted(compare_ls,key = itemgetter(1), reverse = True)
    i = 1
    
    ##Write ranking image to folder
    for ls in compare_ls:
        cv2.imwrite(dir_mainfolder+"/img_rank/"+str(i)+".jpg",list_img[ls[0] - 1])
        i = i+1

def mean_shift(dir_mainfolder):
    ##Read all images from folder
    num = 1
    cv_img = []
    for img2 in glob.glob(dir_mainfolder + "/*.png"):
        n= cv2.imread(img2)
        cv_img.append(n)
    for img2 in glob.glob(dir_mainfolder + "/*.jpg"):
        n= cv2.imread(img2)
        cv_img.append(n)
    for image in cv_img:
        # Get the image and use meanshift
        shifted = cv2.pyrMeanShiftFiltering(image, 21, 51)
        cv2.imwrite(dir_mainfolder+"/img_meanshift/"+str(num)+".jpg",shifted)
        num=num+1

def main(dir_mainfolder, set_k, kmean_flag):
    if kmean_flag == 1:
        ##Run k_mean segmentation
        #k_mean(dir_mainfolder, set_k)
        ##k_mean_main(dir_mainfolder,set_k)
        ##otsu_main(dir_mainfolder,1)
        compare_kmean(dir_mainfolder)
    else:
        ##Run otsu thresholding with meanshift
        #otsu(dir_mainfolder)
        ##mean_shift(dir_mainfolder)
        ##otsu_main(dir_mainfolder,0)
        compare_meanshift(dir_mainfolder)
    print "Done"
    
    cv2.waitKey(0)

