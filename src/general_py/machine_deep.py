from sklearn.datasets import fetch_olivetti_faces
import numpy as np
import matplotlib.pyplot as plt


faces = fetch_olivetti_faces()

# setup the figure

fig = plt.figure(figsize=(6,6))#figure size in inches
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# plot the digits: each image is 8x8 pixels
for i in range(64):
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    ax.imshow(faces.images[i], cmap=plt.cm.bone, interpolation='nearest')

    # label the image with the target value
    #print(ax.text(0, 7, str(faces.target[i])))


if __name__=='__main__':
    #print(faces.keys())
    #print(np.all(faces.images.reshape((400, 4096)) == faces.data))
    print (u'\u10dc',u'\u0923', u'\u2721') #https://home.unicode.org/

