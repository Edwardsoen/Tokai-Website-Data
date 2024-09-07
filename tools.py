import os 
from PIL import Image
import cv2
import numpy as np



path = "product-data"
for i in os.listdir("product-data"): 
    for ii in os.listdir("product-data/"+ i): 
        if "thumbnail.jpg" in ii: 
            file_name = ii
            try: 
                with Image.open(os.path.join(path, i, ii)) as img:
                    img.thumbnail((500, 500), Image.ANTIALIAS)
                    img.save(os.path.join(path, i, ii), "JPEG")
                    print("done :" + ii)
            except IOError: 
                print("test")
            

# for i in os.listdir("product-data\\Snail Horn"): 
#     img = cv2.imread(os.path.join("product-data\\Snail Horn", i))

