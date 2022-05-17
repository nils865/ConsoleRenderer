from PIL import Image
from os import path
from nilslib import setTTYFgCol
from sys import stdout

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

def draw(game, assets):
    def drawRow(row):
        out = ""

        for x in range(len(game[row])):
            for i in assets[game[row][x]]:
                for j in i:
                    out += setTTYFgCol(j[0], j[1], j[2])
                    out += "██"
                out += "\n"
        return out

    for x in range(len(game)):
        stdout.write(drawRow(x))