#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')
import numpy as np
import itertools
import matplotlib.pyplot as plt
import os
import time


#Global Vars
print("Setting Global Vars...")
length = 10

def generate_colors_array():
    print("Creating Colors Array...")
    #colors = [[i, i, i] for i in range(0, 256, 255)]
    colors = list(itertools.product([i for i in range(0, 256)], repeat=3))
    print("Array has been created with lenght: {}".format(len(colors)))
    return colors

def new_image():
    colors_array = generate_colors_array()
    for item in itertools.product(colors_array, repeat=length**2):
        image(item)

def image(item):
    clear_image_dir()
    image_name = "ape_image.png"
    print("Will create new image")
    nparr = np.array([item[i:i + length] for i in range(0, len(item), length)])
    plt.imshow(nparr)
    plt.axis('off')
    plt.show()
    plt.savefig('/var/www/html/{}'.format(image_name))
    time.sleep(5)
        
def clear_image_dir():
    print("Clearing dir")
    try:
        os.remove("/var/www/html/ape_image.png")
    except:
        print("Error in removal of png")
        pass

def main():
    print("Starting main script...")
    new_image()
    print("Done!")

if __name__ == '__main__':
    main()
