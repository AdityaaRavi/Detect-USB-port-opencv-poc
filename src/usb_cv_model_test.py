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

# creating a video feed
feed = cv.VideoCapture(TESTING_INPUT)
if not feed.isOpened():
    print("There is a problem with the feed source you gave!")
    exit()

# going through each frame of the given source
while True:
    status, frame = feed.read()

    # quiting the loop once all frames have been processed.
    if not status:
        print("All available frames processed!")
        break

    # converting the frame to grayscale
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # processing the frame using the models
    lbp_ml_result = lbp.detectMultiScale(frame)
    haar_ml_result = haar.detectMultiScale(frame)

    # showing before application preview
    cv.namedWindow('before application:', cv.WINDOW_NORMAL)
    cv.imshow("before application:", frame)

    # showing to the user what objects were thought to be USB ports by the models
    # LBP
    lbp_final = np.array([])
    np.copy(lbp_final, frame)
    for x, y, w, h in lbp_ml_result:
        lbp_final = cv.rectangle(lbp_final, (x, y), (x + w, y + h), (255, 0, 0), 4)

    # Haar
    haar_final = np.array([])
    np.copy(haar_final, frame)
    for x, y, w, h in haar_ml_result:
        haar_final = cv.rectangle(haar_final, (x, y), (x + w, y + h), (0, 255, 0), 4)

    # ## showing the results of both the methods to the user.

    # # LBP
    cv.namedWindow('LBP preview:', cv.WINDOW_NORMAL)
    cv.imshow("LBP preview:", lbp_final)
    # # Haar
    cv.namedWindow('Haar preview:', cv.WINDOW_NORMAL)
    cv.imshow("Haar preview:", haar_final)

feed.release()

