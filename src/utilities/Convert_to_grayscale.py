# The purpose of this utility program is to convert the given multi-channel image into a gray scale image

# importing required libraries
import cv2 as cv

while True:
    # Asking the user the path to access the image to be converted to gray scale
    path = input("What is the path to your image? :")
    img_handler = None
    try:
        img_handler = cv.imread(path, cv.IMREAD_UNCHANGED)
    except FileNotFoundError:
        print(path + " Not found. Please check the path and try again!")
        exit()

    print("Please press 'y' to confirm this is the image you want to convert to Gray Scale: ")
    cv.imshow(path, img_handler)
    pressed_key = cv.waitKey(0) & 0xFF

    if pressed_key == ord("y"):
        cv.destroyAllWindows()
        break

print("Image confirmed! starting process...")
img_gray = cv.cvtColor(img_handler, cv.COLOR_BGR2GRAY)
cv.imwrite(str.join("", path.split("/")[:-1]) + "/converted_" + str.join("", path.split("/")[1:]), img_gray)

print("Convertion DONE!")
