import cv2

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False

imcount = 0
def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


stop_exit = False
while True:
    # load the image, clone it, and up the mouse callback function
    impath = "image.jpg"
    image = cv2.imread(impath)
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            image = clone.copy()
        # if the 'e' key is pressed, break from the loop
        elif key == ord("e"):
            stop_exit = True
            break
        # if the 'c' key is pressed, continue extracting
        elif key == ord("c"):
            break
    if stop_exit:
        break
    # if there are two reference points, then crop the region of interest
    # from the image and display it
    if len(refPt) == 2:
        roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        coordinates = f"img: {imcount}  x,y : {refPt[0]}, x2,y2: {refPt[1]}, width: {refPt[1][1] - refPt[0][1]}, height: {refPt[1][0] - refPt[0][0]}"
        print(coordinates)
        cv2.imwrite(f"image_gathering/roi{imcount}.jpg", roi)
        with open(f"image_gathering/roi{imcount}.txt", "w") as coord:
            coord.write(coordinates)
        imcount += 1

    # close all open windows
    cv2.destroyAllWindows()
