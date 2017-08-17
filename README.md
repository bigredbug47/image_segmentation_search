# SIMPLE IMAGE SEARCH BASED SEGMENTATION PROJECT
The project will search image based segmentation image, histogram image, and correlation 2D between 2 image.
Project has 2 type of segmentation: k-mean, meanshift which full source code (not use library segmentation).
# FLOW-CHART OF PROJECT
The flow-chart of project is in the picture in folder, first the program will segmentation your image and all images dataset.
Depend what type of segmentation you choose, the time for segmentation will from 1hr-2hr for 100 images.
After segmentation, all images will store in specific folder in where your dataset folder locate.
Next, the program does otsu's method to all segmentation images to get their histograms. After calculate the diff between your picture
and others pictures histogram, the program average the correlation 2D and histogram score to return the ranking result.
The image that seem familiar will has high-score and should be the first in folder.
# HOW IT WORK
2 files to run different 2 programs:
- image_segmentation_simple.py - simple segmentation application.
- paint.py - main project.

