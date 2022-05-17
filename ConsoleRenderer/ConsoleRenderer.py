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

def draw(game, assets):
    def drawRow(row):
        out = ""

        for i in range(len(assets[game[0][0]])):
            for x in game[row]:
                for j in assets[x][i]:
                    out += setTTYFgCol(j[0], j[1], j[2])
                    out += "██"
            out += "\n"

        return out

    for x in range(len(game)):
        stdout.write(f"{drawRow(x)}")
    
    resetColor()