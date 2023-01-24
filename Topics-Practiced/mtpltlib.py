from matplotlib import pyplot as plt
path = r'Images\38.jpg'
img = plt.imread(path,-1)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.ion()
plt.show()
plt.waitforbuttonpress(5)
print('heyyy')