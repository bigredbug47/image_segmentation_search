import Tkinter
from Tkinter import *
import tkFileDialog
from k_mean_algorithm import k_mean_simple
from otsu_method import simple_otsu
import cv2

def kmean_fields():
   if(int(e1.get())>1):
       num_k = int(e1.get())
   else:
       num_k = 2
   k_mean_simple(file_path,num_k)

def meanshift_fields():
   image = cv2.imread(file_path)
   if (int(e2.get()>40)):
       bandwith = int(e2.get())
   else:
       bandwith = 51
   shifted = cv2.pyrMeanShiftFiltering(image, 21, bandwith)
   cv2.imshow("Meanshift Image",shifted)
   cv2.waitKey(0)

def otsu_fields():
    simple_otsu(file_path)

def open_fields():
   root = Tkinter.Tk()
   root.withdraw()
   global file_path
   file_path = tkFileDialog.askopenfilename()
   print file_path
   
   

master = Tk()
Label(master, text="K number").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)
Label(master, text="Meanshift bandwidth").grid(row=1)
e2 = Entry(master)
e2.grid(row=1, column=1)
Button(master, text='Open', command=open_fields).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='K-mean', command=kmean_fields).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text='Mean-shift', command=meanshift_fields).grid(row=3, column=3, sticky=W, pady=4)
Button(master, text='Otsu', command=otsu_fields).grid(row=3, column=4, sticky=W, pady=4)
mainloop( )