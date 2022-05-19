from PIL import Image
from os import path
from nilslib import setTTYFgCol, resetColor
from sys import stdout
from numba import jit

@jit(nopython=False, cache=True, nogil=True, fastmath=True, parallel=True)
def loadAsset(filename):
    list = []
    imagePath = "assets"

    im = Image.open(path.join(imagePath, filename))
    rgb_im = im.convert('RGB')
    
    for i in range(im.size[1]):
        list.append([])
        for j in range(im.size[0]):
            r, g, b = rgb_im.getpixel((j, i))
            list[i].append([r,g,b])

    return list
    
@jit(nopython=False, cache=True, nogil=True, fastmath=True, parallel=True)
def generateRow(row, assets, game):
    out = []

    for i in range(len(assets[game[0][0]])):
        out.append("")
        for x in game[row]:
            a = assets[x][i]
            for j in range(len(a)):
                if not (j > 0 and j < len(a) and a[j] == a[j - 1]):
                    out[i] += setTTYFgCol(a[j][0], a[j][1], a[j][2])

                out[i] += "███"

    return out

@jit(nopython=False, cache=True, nogil=True, fastmath=True, parallel=True)
def draw(game, assets):
    out = []
    for x in range(len(game)):
        out.append(generateRow(x, assets, game))

    str = ""
    count = 0
    for i in out:
        for j in i:
            str += f"{j}\n"
            count += 1
            if not count < 14:
                stdout.write(str)
                str = ""
                count = 0
            elif i[len(i) - 1] == j:
                stdout.write(str)
                str = ""
                count = 0

    resetColor()