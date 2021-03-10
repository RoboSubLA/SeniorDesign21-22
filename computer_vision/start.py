#!/usr/bin/env python
import os
"""
    Modifier: RICARDO MEDINA ()
    Path Bullshit solved by Ricardo godly 
"""
path = os.path.dirname(os.path.abspath(__file__))

weights = path + "/yolov4_files/yolov-tiny-letterA_final.weights"

cfg = path + "/yolov4_files/yolov-tiny-letterA.cfg"

data = path + "/yolov4_files/letterA.data"

so = path + "/yolov4_files/"
os.environ["DARKNET_PATH"] = so

from cv_scripts.cv_main import main

if __name__ == '__main__':
    main(weights, cfg, data)
    
