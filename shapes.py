#!/usr/bin/env python3
'''
This is a plahyground review of openCV image and pixel manipulation
Selecting individual pixels, or drawing and cutting shapes from images,
displaying, and saving them in different format.


'''
import argparse
import cv2

# Handling arguments and help message for arguments
ap = argparse.ArgumentParser(description="use -image arg to pass an image to analyze")
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image from the argument and load it with cv2
# The function cv2.imread will return a numpy array that represents the image

image = cv2.imread(args["image"])