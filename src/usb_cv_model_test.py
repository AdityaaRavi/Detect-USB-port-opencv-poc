# This code is meant to test how accurate the previously created models were.

# importing required external libraries
import cv2 as cv
import numpy as np
import os
# finding and storing the path of the project's root directory
PROJECT_PATH = os.path.dirname(os.getcwd())

# creating constants for cv models' paths
HAAR_MODEL_PATH = PROJECT_PATH + "/resources/final_model/haar_low_cascade.xml"
LBP_MODEL_PATH = PROJECT_PATH + "/resources/final_model/lbp_low_cascade.xml"

# creating cascade classifier variables
haar = cv.CascadeClassifier
lbp = cv.CascadeClassifier

# loading the models onto the classifier variables
if not haar.load(cv.samples.findFile(HAAR_MODEL_PATH)):
    print("Error loading Haar model!")
    exit()
if not lbp.load(cv.samples.findFile(LBP_MODEL_PATH)):
    print("Error loading lbp model!")
    exit()

# Creating a constant to store the source of testing feed
TESTING_INPUT = 0


