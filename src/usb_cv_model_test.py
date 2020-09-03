# This code is meant to test how accurate the previously created models were.

# importing required external libraries
from __future__ import print_function
import cv2 as cv
import numpy as np
import os
# finding and storing the path of the project's root directory
PROJECT_PATH = os.path.dirname(os.getcwd())

# creating constants for cv models' paths
HAAR_MODEL_PATH = PROJECT_PATH + "/resources/final_model/haar_low_cascade.xml"
LBP_MODEL_PATH = PROJECT_PATH + "/resources/final_model/lbp_low_cascade.xml"

# creating cascade classifier variables
haar = cv.CascadeClassifier()
lbp = cv.CascadeClassifier()

# loading the models onto the classifier variables
if not haar.load(cv.samples.findFile(HAAR_MODEL_PATH)):
    print("Error loading Haar model!")
    exit()
if not lbp.load(cv.samples.findFile(LBP_MODEL_PATH)):
    print("Error loading lbp model!")
    exit()


# Calculate results and showing it to the user
def findAndshowUser(frame, **kwargs):
    # showing before application preview
    cv.namedWindow('before application:', cv.WINDOW_NORMAL)
    cv.imshow("before application:", frame)

    # converting the frame to grayscale
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # processing the frame using the models
    lbp_ml_result = lbp.detectMultiScale(frame_gray)
    haar_ml_result = haar.detectMultiScale(frame_gray)

    # showing to the user what objects were thought to be USB ports by the models
    if "lbp" in kwargs and kwargs["lbp"]:
        # LBP
        for x, y, w, h in lbp_ml_result:
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 4)

    if "haar" in kwargs and kwargs["haar"]:
        # Haar
        for x, y, w, h in haar_ml_result:
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)

    if "combined" in kwargs and kwargs["combined"]:
        for x, y, w, h in haar_ml_result:
            if (x, y, w, h) in lbp_ml_result:
                # displaying the common between haar and lbp
                frame = cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 4)

    print("kwargs printed:", kwargs)
    wait = 0
    if "waitkey" in kwargs:
        wait = kwargs["waitkey"]
        print("This is a video!, wait key is: " + str(wait))

    # ## showing the results of both the methods to the user.
    cv.namedWindow('Processed preview:', cv.WINDOW_NORMAL)
    cv.imshow("Processed preview:", frame)

    if cv.waitKey(wait) == ord("q"):
        print("Need to close!")
        return True

    return False


# Code for testing the model using a video
def testWithVideo():
    source = input("What is the path of the video feed (relative to the project root folder) you want to test with? "
                   "Type '0' to use the webcam: ")

    # Creating a constant to store the source of testing feed
    testing_input = 0
    if not source == '0':
        testing_input = PROJECT_PATH + source

    # creating a video feed
    feed = cv.VideoCapture(testing_input)
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

        # processing the image and showing the results
        if findAndshowUser(frame, haar=True, waitkey=1):
            print("wait key returned true!")
            break

    feed.release()


# Code for testing the model using an image
def testWithImg():
    while True:
        # Getting the path of the image from the user
        source = input("What is the path of the image you want to test with? (relative to the project root folder): ")
        testing_input = PROJECT_PATH + source

        # creating an image handler for the image
        img_handler = cv.imread(testing_input, cv.IMREAD_COLOR)

        # Showing the image to the user as a preview
        cv.namedWindow("Is this the image you want to use? Press 'y' to confirm and anything else to repick.",
                       cv.WINDOW_NORMAL)

        cv.imshow("Is this the image you want to use? Press 'y' to confirm and anything else to repick.", img_handler)
        if cv.waitKey(0) == ord("y"):
            break

    findAndshowUser(img_handler, haar=True)


# Asking the user if they want to test the models with an image or a video
if input("What do you want to use to test? Type 'image' or 'video': ").lower() == "image":
    testWithImg()
else:
    testWithVideo()

