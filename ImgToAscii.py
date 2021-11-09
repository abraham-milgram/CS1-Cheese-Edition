"""
Author: abraham-milgram
Description: Image to Txt file converter
"""
from PIL import Image, ImageOps
import os
# Put the file of your image here (png or jpg supporteds)
file = r"C:\Users\user\Downloads\image.jpg"
imageOrigin1 = Image.open(file)
imageOrigin1.show()
width1, height1 = imageOrigin1.size
imageOrigin = imageOrigin1.resize((width1, (round(height1 * 2/3) + 1)))
width, height = imageOrigin.size
imageOrigin.show()

# Converting to grayscale
imListRaw = list(ImageOps.grayscale(imageOrigin).getdata())

# Grouping numbers into lists of 3 so they can be handled as rgb values
imList = []
ListDynamic = []
c = 0
for a in imListRaw:
    if c != 3:
        ListDynamic.append(a)
        c += 1
    else:
        imList.append(ListDynamic)
        ListDynamic = []
        c = 0

# Takes the average of the rgb values then scales them down to a value under 70 (amount of charecters in the b/w scale)
imListP = []
for a in imList:
    imListP.append(round((sum(a)/3)*70/255))

# Scale of ascii charecters based on amount of colored pixels "http://paulbourke.net/dataformats/asciiart/"
cscale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~i!lI;:,\\\"^`\". "

# Converting the greyscale single number values into ascii characters
imListFinal = []
for a in imListP:
    if a == 0:
        imListFinal.append(' ')
    else:
        imListFinal.append(cscale[a])

# Writing to a text file/seperating the list of charecters into lines
f = open("im.txt","w+")
for h in range(round(height/4)):

    line = []
    for w in range(round(width/4)):
        line.append(imListFinal[h*width+w])
    f.write(''.join(line) + "\n")
f.close()
# Opening the file
os.system('notepad.exe ' + 'im.txt')
quit