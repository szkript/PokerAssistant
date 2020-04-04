import cv2
import pickle
from utils import Utils

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
coordinates_from_image = []
while True:
    # load the image, clone it, and up the mouse callback function
    impath = "image_gathering/current_table.jpg"
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
        player_data_pos = dict(
            x=refPt[0][0],
            y=refPt[0][1],
            width=refPt[1][1]-refPt[0][1],
            height=refPt[1][0]-refPt[0][0]
        )
        coordinates_from_image.append(player_data_pos)
        imcount += 1

    # close all open windows
    cv2.destroyAllWindows()

fname = input("filename: ")
with open(f'game_components/positions/{fname}.pickle', 'wb') as handle:
    pickle.dump(coordinates_from_image, handle, protocol=pickle.HIGHEST_PROTOCOL)

# cv2.imwrite("image_gathering/"+fname, Utils.crop_at_pos())
# with open('game_components/player9_coordinates.pickle', 'rb') as handle:
#     b = pickle.load(handle)
# print(b)