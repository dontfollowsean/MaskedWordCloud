#!/usr/bin/env python2
"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from wordcloud import WordCloud, STOPWORDS
from PIL import Image

from scipy import ndimage
from scipy.misc import toimage
from skimage import filter
import numpy as np



	
d = path.dirname(__file__)

# Read the whole text.
print("Reading Text")
text = open(path.join(d, 'text/a_new_hope.txt')).read()

#make image black and white
print("Creating BW Image")
image_file = Image.open('images/nga.png')
image_file = image_file.convert("L") # convert image to black and white
image_file.mode = "L"
image_file = image_file.point(lambda x: 0 if x>128 else 255)
print("Saving BW Image")
image_file.save('images/output/grayscale.png')

#find edges
print("Creating Outline of BW Image")
edges = filter.canny(imread(path.join(d,'images/output/grayscale.png')), sigma=3)
edimage = toimage(edges).convert("RGB")


# read the mask image
print("Reading BW Image")
mask = imread(path.join(d, "images/output/grayscale.png"))


print("Creating WordCloud")
wc = WordCloud(background_color="black", max_words=2000, mask=mask,
	stopwords=STOPWORDS)
# generate word cloud
wc.generate(text)


# store to file
#wc.to_file(path.join(d, "alice.png"))
wc.to_file(path.join(d, "images/output/wordcloud.png"))
wcimg = toimage(imread(path.join(d,"images/output/wordcloud.png")))


#print(edimage.mode)
#print(wcimg.mode)

#print(type(edimage))
#print(type(imread(path.join(d,"images/output/output.jpg"))))
out = Image.blend(wcimg,edimage,0.15)
out.save('images/output/maskedwc.png')


# show
plt.imshow(out)
plt.axis("off")
plt.figure()
plt.imshow(edimage)
plt.axis("off")
plt.figure()
plt.imshow(wcimg)
plt.axis("off")
plt.figure()
plt.imshow(mask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()