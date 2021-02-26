# usb-port-detect-alpha
I made this repo a while back to help me make and test CV models to detect USB-A ports from a given picture or video feed with the aim of being able to use that information to make a robot arm automatically plug an USB drive into an USB port.


## Current Progress
- two models trained (one based on haar and one on lbp) to check which will suit our needs the best once we do train the models to a decent level of accuracy.
  - why did I do that? Haar is more accurate, but lbp is faster to train

 The Python code written to test the code works perfectly and it contains the following features:
- choose from a single image or a video stream (such as the one from your webcam)
- overlay what both the haar and lbp cascade models think are USB ports on the screen
  - choose to display, one of the above, both of the above, or the intersection of the above

## Future plans?
Based on our testing, using a neural network through `TensorFlow` just seems to be a much better option for our needs, ergo that's it for this repo :/ 

## disclaimer
As I was building this repo as merely a proof of concept (for RoverCrest's robot arm team), I did not take the time to pick proper postive images to use to train the Cascade models created by OpenCV, so the lbp and haar cascade models in this repo are examples as to why you should manually pick postive images instead of relying on OpenCV's ability to automatically create multiple postives based on single image (`opencv_createsamples`) :-( 
