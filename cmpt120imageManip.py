# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author: Samantha Chung
# Date: December 7 2020
# Description: Multiple piel manipulation functions that can be used to edit a photo
#               - This file is where all the functions were written that can be called in the main.py

import cmpt120imageProj
import numpy
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

def practice(pixels):
    width = len(pixels)
    height = len(pixels[0])

    for x in range(width):
        for y in range(height):

            pix = pixels[x][y]

            r = pix[0]
            g =pix[1]
            b = pix [2]

            pixels[x][y] = [r,g,r]

    return pixels



def invertImage(pixels):

    #Gets the amount of pixels height wise and width wise
    width = len(pixels)
    height = len(pixels[0])

  # for loop that will go through each pixel of the image
  # starting with the width, called x for x axis
  # Then height with the variable name y for y axis
    for x in range (width):
        for y in range (height):

      # pix is the variable name that will read each of pixels in the image
            pix = pixels[x][y]

      # r,g,b are variable names that will look in to each pixels colour code and subtract that value from 255
            r = 255 - pix[0]
            g = 255 - pix[1]
            b = 255 - pix[2]

      # assigns the new colour code to each pixel in the image
            pixels[x][y] = [r,g,b]

    #Returns new pixels to be applied to the photo
    return pixels

def flipHorizontal(pixels):
    width = len(pixels)
    height = len(pixels[0])

    #Loop that will go through all the pixels but only half od its width
    #This is so that the image does not over write itself
    for x in range (width//2):
        for y in range (height):

            #pix is assigned the images pixels of the other side of the image
            pix = pixels [width - 1 - x][y]

            #The pix on the other side of the image is reassigned to the all the pixels in the image
            #In order to have the original image again and copy the left sides pixel on to the right
            pixels [width - 1 - x][y] = pixels[x][y]

            #All the pixels in the image is reassigned to pix to apply the same to the other side
            pixels[x][y] = pix

    return pixels

def flipVertical(pixels):
    width = len(pixels)
    height = len(pixels[0])

    #this is the same code as flipHorizontal
    #Except the height is halved to flip it vertically and instead of looking at the x (width) pixels
    #You look and copy the y (height) pixels
    for x in range (width):
        for y in range (height//2):

            pix = pixels [x][height - 1 - y]
            pixels [x][height - 1 - y] = pixels[x][y]
            pixels[x][y] = pix

    return pixels

def redChannel(pixels):
    print ("Removing red...")
    width = len(pixels)
    height = len(pixels[0])

    for x in range (width):
        for y in range (height):

            pix = pixels[x][y]

            #After getting each of the pixels, each of the colour values are assigned to a variable
            #Only the r value is subtracted by itself to remove all red shades in the image
            r = pix[0] - pix [0]
            g = pix[1]
            b = pix [2]

            #Assigned each pixel to the new set of pixels colours
            pixels[x][y] = [r,g,b]

    return pixels

def greenChannel(pixels):
    print ("Removing green...")
    width = len(pixels)
    height = len(pixels[0])

    for x in range (width):
        for y in range (height):

            pix = pixels[x][y]

            #Same as the above code except now green is subtracted to set the amount to 0
            r = pix[0]
            g = pix[1] - pix [1]
            b = pix [2]

            pixels[x][y] = [r,g,b]

    return pixels

def blueChannel(pixels):
    print ("Removing blue...")
    width = len(pixels)
    height = len(pixels[0])

    for x in range (width):
        for y in range (height):

            pix = pixels[x][y]

            #Same as the above code except now blue is subtracted to set the amount to 0
            r = pix[0]
            g = pix[1]
            b = pix [2] - pix [2]

            pixels[x][y] = [r,g,b]

    return pixels

def grayscale(pixels):
    print ("Changing to grayscale...")
    width = len(pixels)
    height = len(pixels[0])

    for x in range (width):
        for y in range (height):

            pix = pixels[x][y]

            #All colour values in each pixel is added together and divided by 3 to find its average
            colour = (pix[0] + pix [1] + pix [2])/3

            #Each pixel is now assigned the new average value in each of its r g b indexes
            pixels[x][y] = [colour,colour,colour]


    return pixels

#9

def sepia(pixels):
    print ("Applying sepia filter...")
    width = len(pixels)
    height = len(pixels[0])

    for x in range (width):
        for y in range (height):

            pix = pixels[x][y]

            #Each r g b value in each pixel is multiplied by the formula number
            #Each r g b value is then added together and assigned to a variable
            r = int((pix[0] * 0.393) + (pix[1] * 0.769) + (pix[2] * 0.189))
            g = int((pix[0] * 0.349) + (pix[1] * 0.686) + (pix[2] * 0.168))
            b = int((pix[0] * 0.272) + (pix[1] * 0.534) + (pix[2] * 0.131))

            #These if statements check each variable to see it it is too high or too lower
            #In order to not have variables that are negative or over 255
            #If they exeed, they are round up or down to an acceptable variable
            #If they were originally not too low or high, they stay the same
            if r > 255:
                r = 255
            elif r < 0:
                r = 0
            if g > 255:
                g = 255
            elif g < 0:
                g = 0
            if b > 255:
                b = 255
            elif b < 0:
                b = 0

            #After checking and making sure they are at the right value,
            #Each pixel in the image is assigned the new r g b values
            pixels[x][y] = [r,g,b]

    return pixels


def decreaseBrightness(pixels):
    print ("Decreased brightness by 10")
    width = len(pixels)
    height = len(pixels[0])

    for x in range (width):
        for y in range (height):

            pix = pixels[x][y]

            #Each r g b value subtracts 10 to itself in order to make the image darker each press
            r = pix[0] - 10
            g = pix[1] - 10
            b = pix[2] - 10

            #If the subtracted amount reaches 0, it stays at 0
            if r <= 0:
                r = 0
            if g <= 0:
                g = 0
            if b <= 0:
                b = 0

            pixels[x][y] = [r,g,b]

    return pixels

def increaseBrightness(pixels):
    print ("Increased brightness by 10")
    width = len(pixels)
    height = len(pixels[0])

    for x in range (width):
        for y in range (height):

            pix = pixels[x][y]

            #Each r g b value adds 10 to itself in order to make the image brighter each press
            r = pix[0] + 10
            g = pix[1] + 10
            b = pix[2] + 10

            #If the added amount reaches 255, it stays at 255
            if r >= 255:
                r = 255
            if g >= 255:
                g = 255
            if b >= 255:
                b = 255

            pixels[x][y] = [r,g,b]

    return pixels

def leftRotate(pixels):
    print ("Image rotated left once")
    width = len(pixels)
    height = len(pixels[0])

    #Creates a black image for the new pixels to be copied on to
    #The parameter is height then width because the image needs to be rotated
    #So the size of the width must become its height
    black = cmpt120imageProj.createBlackImage(height,width)

    for x in range (width):
        for y in range (height):

            #pix is assigned the image pixel values on the negative (other) side of the image (width wise (the right side of the image))
            pix = pixels[-x][y]

            #Each r g b value is assigned a variable
            #The r g b value is the colour values of the images starting from the right (opposite side)
            r = pix[0]
            g = pix[1]
            b = pix[2]

            #The r g b values are pasted on to the black image but height (y) first
            #In order to rotate the image
            black[y][x] = [r,g,b]



    return black

def rightRotate(pixels):
    print ("Image rotated left once")
    width = len(pixels)
    height = len(pixels[0])

    black = cmpt120imageProj.createBlackImage(height,width)
    for x in range (width):
        for y in range (height):

            #pix is assigned the image pixel values on the negative (other) side of the image (height wise (the bottom of the image))
            pix = pixels[x][-y]

            #Each r g b value is assigned a variable
            #The r g b value is the colour values of the images starting from the bottom (opposite side)
            r = pix[0]
            g = pix[1]
            b = pix[2]

            #The r g b values are pasted on to the black image but height (y) first
            #In order to rotate the image
            black[y][x] = [r,g,b]

    return black

def pixelate(pixels):
    print("4x4 Pixels averaged")

    #Gets the pixel amount of the width of the image and divides it by 4
    #Any remainders are subtracted from the width
    #Same for height
    width = len(pixels)
    width = width - width%4
    height = len(pixels[0])
    height = height - height%4

    #For loop selects only pixels in groups of 4's
    for x in range (0, width, 4):
        for y in range (0, height, 4):

            r=0
            g=0
            b=0

            #A new for loop that loop at the last x value and the next 4 x values
            #Same for n
            for i in range(x,x+4):
                for n in range(y,y+4):

                    #Add the pixel value to the r g b counter above
                    #The counter is the pixel and colour value
                    r += pixels[i][n][0]
                    g += pixels[i][n][1]
                    b += pixels[i][n][2]

            #Outside of the loop is the averaging of the r g b counters to pixelize the image
            #This loops its as many time as there are groups
            newR = r / 16
            newG = g / 16
            newB = b / 16

            #Same as before, loop applies from the previous x to next 4 x values
            for a in range (x,x+4):
                for b in range (y,y+4):

                    #The pixel the loop is on is assigned the averaged colour values
                    pixels[a][b][0] = newR
                    pixels[a][b][1] = newG
                    pixels[a][b][2] = newB

    return pixels


def binarize(pixels):
    print ("Image binarized")
    width = len(pixels)
    height = len(pixels[0])
    imageLoop = True
    amount = 0

    #turns image to greyscale and averages pixel values
    for x in range (width):
        for y in range (height):

            pix = pixels[x][y]

            colour = (pix[0] + pix [1] + pix [2])/3

            pixels[x][y] = [colour,colour,colour]

            #adds the r pixels value to the amount counter that adds them all together
            amount += pixels[x][y][0]

    #Calculates the first threshold with the amount value and divides by the total number of pixels in the image
    threshold_1 = int((amount)/(width*height))
    print (threshold_1)

    while imageLoop:

        #Creates a foreground and background black image
        #counters are made for average calculations later on
        foreground = cmpt120imageProj.createBlackImage(width, height)
        fg = 0
        background = cmpt120imageProj.createBlackImage(width,height)
        bg = 0

        for x in range (width):
            for y in range (height):

                #only looks at the r value of each pixel
                #That pixel value is added to the bg counter
                #Each run through the counter goes up to know how many pixels went through the loop
                #same for foreground except if it is higher, it is added to a different image
                pix = pixels[x][y][0]
                if pix <= threshold_1:
                    bg += pix
                elif pix > threshold_1:
                    fg += pix

        #using the counters, the averages are calculated
        fgAverage = int((bg)/(width*height))
        bgAverage = int((fg)/(width*height))

        #the second threshold is made
        threshold_2 = int((fgAverage+bgAverage)/2)
        print (threshold_2)

        #the difference of the thresholds are calculated
        final_threshold = threshold_2 - threshold_1
        print (final_threshold)

        #If the final threschold is lower than 10, the while loop ends
        #If it is above, a new for loop sorts the o and 255 pixels
        if final_threshold <= 10:
            for x in range (width):
                for y in range (height):
                    pix = pixels[x][y][0]
                    #If the r value is lower than the threshold, the pixels is turned to black
                    #If the r value is above, it is turned white
                    if pix <= threshold_1:
                        pixels[x][y] = [0,0,0]
                    elif pix > threshold_1:
                        pixels[x][y] = [255,255,255]

            break
        else:
            threshold_1 = threshold_2

    return pixels


