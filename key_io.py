# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 19:23:34 2020
Project-Image_Authentication_Using_Water_Marking_Technique
Section-Key_I/0
@author: RAVI
"""

import sys
import math
import itertools
import random
from PIL import Image
    
def shuffle_order(size, shuffle_seed):
    order = []
    for i in range (size):
        order.append(i)
    if (shuffle_seed):
        random.seed(shuffle_seed)
        shuffled = random.shuffle(order)
        return order
    else:
        return order
    
def encrypt(plain, key):
    cipher = []
    k = 0
    len_key = len(key)
    len_plain = len(plain)
    for i in range(len_plain):
        cipher.append((plain[i] + ord(key[i % len_key])) % 256)
    return cipher

def decrypt(cipher, key):
    plain = []
    k = 0
    len_key = len(key)
    len_cipher = len(cipher)
    for i in range(len_cipher):
        plain.append((cipher[i] + 256 - ord(key[i % len_key])) % 256)
    return plain


def rms(image_a,image_b):
    px_a = image_a.load()
    px_b = image_b.load()
    sum=0;
    for i in range(image_a.width):
        for j in range(image_a.height):
            p_a = px_a[i,j]
            p_b = px_b[i,j]
            sum += math.pow((p_a[0] - p_b[0]), 2) + math.pow((p_a[1] - p_b[1]), 2) + math.pow((p_a[2] - p_b[2]), 2)

    return 5#math.sqrt(sum / (image_a.width * image_a.height) / 3)
