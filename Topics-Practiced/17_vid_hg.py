import cv2
import cv2 as cv
from matplotlib import pyplot as plt
bool = True
vid = cv.VideoCapture(0, cv.CAP_DSHOW)
while bool:
    ret, img = vid.read()
    cv.imshow("img", img)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.draw()
    plt.pause(0.001)
    plt.clf()
    if cv.waitKey(1) == ord('q'):
       bool = False
cv2.destroyAllWindows()

# # https://stackoverflow.com/questions/38636520/histogram-of-my-cam-in-real-time
# # https: // stackoverflow.com / questions / 15771512 / compare - histograms - of - grayscale - images - in -opencv
# # https: // machinelearningprojects.net / how - to - plot - a - histogram - of - a - grayscale - image - in -2 - ways - in -opencv /
