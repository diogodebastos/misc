import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# https://matplotlib.org/examples/pylab_examples/custom_cmap.html

cdict1 = {'red':   ((0.0, 0.97, 0.97),
                   (0.25, 0.0, 0.0),
                   (0.75, 0.0, 0.0),
                   (1.0, 1.0, 1.0)),

         'green': ((0.0, 0.25, 0.25),
                   (0.25, 0.15, 0.15),
                   (0.75, 0.39, 0.39),
                   (1.0, 0.78, 0.78)),

         'blue':  ((0.0, 1.0, 1.0),
                   (0.25, 0.65, 0.65),
                   (0.75, 0.02, 0.02),
                   (1.0, 0.0, 0.0))
        }

myColor = LinearSegmentedColormap('myColorMap', cdict1)

def grayscale_cmap(cmap):
    """Return a grayscale version of the given colormap"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    # convert RGBA to perceived grayscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]

    return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)


def view_colormap(cmap):
    """Plot a colormap with its grayscale equivalent"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    cmap = grayscale_cmap(cmap)
    grayscale = cmap(np.arange(cmap.N))

    fig, ax = plt.subplots(2, figsize=(6, 2),
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax[0].imshow([colors], extent=[0, 10, 0, 1])
    ax[1].imshow([grayscale], extent=[0, 10, 0, 1])

view_colormap(myColor)
plt.show()
