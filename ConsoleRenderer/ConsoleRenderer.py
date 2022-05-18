from time import perf_counter
from PIL import Image
from os import path
from nilslib import setTTYFgCol, resetColor
from sys import stdout

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

def generateRow(row, assets, game):
    out = []

    for i in range(len(assets[game[0][0]])):
        out.append("")
        for x in game[row]:
            for j in assets[x][i]:
                out[i] += setTTYFgCol(j[0], j[1], j[2])
                out[i] += "██"

    return out

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
            if not count < 15:
                stdout.write(str)
                str = ""
                count = 0
            elif i[len(i) - 1] == j:
                stdout.write(str)
                str = ""
                count = 0

    resetColor()