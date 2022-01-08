from os.path import isfile
from Image_set_gen import *
import noise
from PIL import Image
import numpy as np

Nx, Ny = 200, 200
shape = (Nx, Ny)
scale = 10.0
octaves = 6
persistence = 0.5
lacunarity = 2.0
world = np.zeros(shape)
for count in range(100):  # number of images
    if isfile("Noise_Img" + str(count) + ".png") is not True:  # check for existing files
        seed = random.randint(0, 100)
        for i in range(shape[0]):
            for j in range(shape[1]):
                world[i][j] = noise.pnoise2(i / scale,
                                            j / scale,
                                            octaves=octaves,
                                            persistence=persistence,
                                            lacunarity=lacunarity,
                                            repeatx=Nx,
                                            repeaty=Ny,
                                            base=seed)
        im = Image.fromarray((world * 255).astype('uint8'), mode="L")
        im.save("Noise_Img" + str(count) + ".png")  # file path
