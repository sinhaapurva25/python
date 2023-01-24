import cv2
from matplotlib import pyplot as plt

plt.ion()
while(1):
    image = cv2.imread(r'Images/38.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_8)
    cv2.imshow("",image)
    ax = plt.hist(image.flatten(), 256, [0, 256])
    plt.draw()
    plt.savefig(r'Images/graph')
    plt.pause(0.001)
    plt.clf()
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()