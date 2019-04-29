import png
from numpy import genfromtxt
import numpy as np
from PIL import Image
import os, sys
import csv


#  width and height
# 48894  = 281*174
# 48894*9 = 843*522
# 231401 = 641*361


# filename: the csv's filename
# width: png's width
# mode: RGB or L
# outputFilename: png's filename
def csv2pngColor(filename, width, outputFilename):
    all = []
    temp = []
    my_data = genfromtxt(filename, delimiter=',')
    i = 0
    for row in my_data:
        for ele in row:
            temp.append(ele)
            i += 1
            if i == width * 3:
                all.append(list(temp))
                i = 0
                temp = []
    png.from_array(all, 'RGB').save(outputFilename)


def data2pngColor(data, width, outputFilename):
    all = []
    temp = []
    i = 0
    for row in data:
        for ele in row:
            temp.append(ele)
            i += 1
            if i == width * 3:
                all.append(list(temp))
                i = 0
                temp = []
    png.from_array(all, 'RGB').save(outputFilename)



def csv2pngGrey(filename, width, outputFilename):
    all = []
    temp = []
    my_data = genfromtxt(filename, delimiter=',')
    i = 0
    for row in my_data:
        temp.append(row[4])
        i += 1
        if i == width:
            all.append(list(temp))
            i = 0
            temp = []
    png.from_array(all, 'L').save(outputFilename)

def data2pngGrey(data, width, outputFilename):
    all = []
    temp = []
    i = 0
    for row in data:
        temp.append(row[4])
        i += 1
        if i == width:
            all.append(list(temp))
            i = 0
            temp = []
    png.from_array(all, 'L').save(outputFilename)


def color2Grey(filename1, filename2):
    img = Image.open(filename1).convert('L')
    img.save(filename2)

def grey2CSV(filename1, filename2):
    im = Image.open(filename1)
    width, height = im.size
    pix = im.load()
    data = []
    for j in range(1, height, 3):
        for i in range(1, width, 3):
            temp = []
            dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
            for dir in dirs:
                temp.append(pix[i+dir[0],j+dir[1]])
            data.append(temp)
    with open(filename2, 'w', newline='\n') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        for row in data:
            w.writerow(row)

def color2CSV(filename1, filename2):
    im = Image.open(filename1)
    width, height = im.size
    pix = im.load()
    data = []
    for j in range(1, height, 3):
        for i in range(1, width, 3):
            data.append(list(pix[i,j]))
    with open(filename2, 'w', newline='\n') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        for row in data:
            w.writerow(row)


if __name__ == "__main__":
    color2Grey('palm.jpg','palmGrey.png')
    color2CSV('palm.jpg','palmColor.csv')
    grey2CSV('palmGrey.png','palmGrey.csv')


    # csv2pngColor('color.csv', 281, 'color.png')
    # csv2pngGrey('input.csv', 281, 'input.png')
    # csv2pngGrey('data.csv', 641, 'data.png')
