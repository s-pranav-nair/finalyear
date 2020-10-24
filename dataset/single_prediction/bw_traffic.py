# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 17:24:14 2020

@author: Pranav
"""
import os
from PIL import Image
from PIL import ImageOps  
import numpy as np
img_path = os.path.join('color')
img_list = []

hidden_files_removed = [fl for fl in os.listdir(img_path) if fl[0] != '.' ]
for one_img in hidden_files_removed:

    # Workaround to counter the 'too many open files' error in PIL
    temp_img = Image.open(os.path.join(img_path, one_img))
    img_list.append(temp_img.copy())
    temp_img.close()
    



img_bw = [img.convert('L') for img in img_list]
consonants_proc = [ImageOps.invert(img) for img in img_bw]

for i in range(0,200):
    newImg1 = consonants_proc[i]
    label = hidden_files_removed[i]
    newImg1.save(label,"PNG")


def vectorize_one_img(img):
        # Represent the image as a matrix of pixel weights, and flatten it
        flattened_img = np.asmatrix(img).flatten()
        # Rescaling by dividing by the maximum possible value of a pixel
        flattened_img = np.divide(flattened_img,255.0)
        return np.asarray(flattened_img)[0] 

def to_vectors(img_list):
    return [vectorize_one_img(img) for img in img_list]

consonants_inputs = to_vectors(consonants_proc)