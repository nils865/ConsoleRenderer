from PIL import Image
from os import path

def loadAsset(filename):
    list = []
    imagePath = "assets"

    im = Image.open(path.join(imagePath, filename))
    rgb_im = im.convert('RGB')
    
    for i in range(im.size[0]):
        list.append([])
        for j in range(im.size[1]):
            r, g, b = rgb_im.getpixel((i, j))
            list[i].append([r,g,b])

    return list