#!/usr/bin/env python2
"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS
from PIL import Image

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'text/a_new_hope.txt')).read()

#make image black and white
image_file = Image.open('images/nga.png')
image_file = image_file.convert("L") # convert image to black and white
image_file.mode = "L"
image_file = image_file.point(lambda x: 0 if x>128 else 255)
image_file.save('images/grayscale.jpg')

# read the mask image
# taken from
mask = imread(path.join(d, "images/grayscale.jpg"))



wc = WordCloud(background_color="black", max_words=2000, mask=mask,
               stopwords=STOPWORDS)
# generate word cloud
wc.generate(text)

# store to file
#wc.to_file(path.join(d, "alice.png"))
wc.to_file(path.join(d, "images/output.jpg"))

# show
plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(mask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
