# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author: Samantha Chung
# Date: December 7 2020
# Description: Multiple piel manipulation functions that can be used to edit a photo
#               - This file is where all the functions are called and the use interface is created and shown

import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
system = [
            "Q: Quit",
            "O:Open Image",
            "S:Save Current Image",
            "R:Reload Original Image"
         ]

# list of basic operation options
basic = [
          "1:Invert",
           "2:Flip Horizontal",
           "3:Flip Vertical",
           "4:Switch to Intermediate Functions",
          "5:Switch to Advanced Functions"
         ]

# list of intermediate operation options
intermediate = [
                  "1:Remove Red Channel",
                  "2:Remove Green Channel",
                  "3:Remove Blue Channel",
                  "4:Convert to Grayscale",
                  "5:Apply Sepia Filter",
                  "6:Decrease Brightness",
                  "7:Increase Brightness",
                  "8: Switch to Basic Functions",
                  "9: Switch to Advanced Functions"
                 ]

# list of advanced operation options
advanced = [
                "1:Rotate Left",
                "2:Rotate Right",
                "3:Pixelate",
                "4:Binarize",
                "5: Switch to Basic Functions",
                "6: Switch to Intermediate Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice(Q/O/S/R or 1-5)...")
    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate
        menuString.append("")
        menuString.append("Enter your choice(Q/O/S/R or 1-9)...")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice(Q/O/S/R or 1-6)...")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
        Input:  state - a dictionary containing the state values of the application
                img - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """

    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")

            #My functions start here
        if userInput == "O":
            print ("Opening image...")

            #Opens window so you can choose whiever image is needed
            tkinter.Tk().withdraw()
            openFilename = tkinter.filedialog.askopenfilename()
            #Saves the image opened to a dictionary value that will be used later on
            appStateValues["lastOpenFilename"] = openFilename
            #Gets image and displays it in window with text instructions
            img = cmpt120imageProj.getImage(openFilename)
            cmpt120imageProj.showInterface(img,"Project Image",generateMenu(appStateValues))
        if userInput == "S":
            print ("Saving current image...")
            #Opens window to save the edited image
            tkinter.Tk().withdraw()
            saveFilename = tkinter.filedialog.asksaveasfilename()
            #After saved, the image is taken and showed again in output window
            cmpt120imageProj.saveImage(img, saveFilename)
            cmpt120imageProj.showInterface(img,"New Saved Image",generateMenu(appStateValues))
        if userInput == "R":
            print ("Loading original image...")
            #Finds the last opened image that was stored in dictionary in the "OPEN" function and shows it
            img = cmpt120imageProj.getImage(appStateValues["lastOpenFilename"])
            cmpt120imageProj.showInterface(img, "Project Image", generateMenu(appStateValues))

        # ***add the rest to handle other system functionalities***

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)

        #If the chosen mode is "basic," these are the available keys that can manipulate the image
        #Each modes interface is stored in the dictionary and is shown when selected
        if state['mode'] == "basic":
            if userInput == "1":
                print ("Image colours inverted")

                """
                #Each function uses a variable to ressaign the function call to
                #img is used since it is a global variable and was used when opening the image
                #So after the new pixels are returned from the function, showInterface will use those pixels and shwo them in output
                """

                img = cmpt120imageManip.invertImage(img)
                cmpt120imageProj.showInterface(img,"Project Image Inverted",generateMenu(appStateValues))
            elif userInput == "2":
                print ("Image flipped horizontally")
                img = cmpt120imageManip.flipHorizontal(img)
                cmpt120imageProj.showInterface(img,"Project Image Flipped Horizontal",generateMenu(appStateValues))
            elif userInput == "3":
                print ("Image flipped vertically")
                img = cmpt120imageManip.flipVertical(img)
                cmpt120imageProj.showInterface(img,"Project Image Flipped Vertical",generateMenu(appStateValues))
            elif userInput == "4":
                print ("Changed to Intermediate functions")
                state ["mode"] = "intermediate"
                cmpt120imageProj.showInterface(img,"Intermediate Functions",generateMenu(appStateValues))
            elif userInput == "5":
                print ("Changed to Advanced mode")
                state ["mode"] = "advanced"
                cmpt120imageProj.showInterface(img,"Advanced Functions",generateMenu(appStateValues))
            elif userInput == "6":
                print ("Practice")
                img = cmpt120imageManip.practice(img)
                cmpt120imageProj.showInterface(img,"Practice",generateMenu(appStateValues))

        #These keys are allowed if the mode is changed to intermediate
        elif state['mode'] == 'intermediate':
            if userInput == "1":
                cmpt120imageManip.redChannel(img)
                cmpt120imageProj.showInterface(img,"Project Image Red Removed",generateMenu(appStateValues))
            elif userInput == "2":
                img = cmpt120imageManip.greenChannel(img)
                cmpt120imageProj.showInterface(img,"Project Image Green Removed",generateMenu(appStateValues))
            elif userInput == "3":
                img = cmpt120imageManip.blueChannel(img)
                cmpt120imageProj.showInterface(img,"Project Image Blue Removed",generateMenu(appStateValues))
            elif userInput == "4":
                img = cmpt120imageManip.grayscale(img)
                cmpt120imageProj.showInterface(img,"Project Image Grayscaled",generateMenu(appStateValues))
            elif userInput == "5":
                img = cmpt120imageManip.sepia(img)
                cmpt120imageProj.showInterface(img,"Project Image Sepia Filter Applied",generateMenu(appStateValues))
            elif userInput == "6":
                img = cmpt120imageManip.decreaseBrightness(img)
                cmpt120imageProj.showInterface(img,"Project Image Decreased Brightness by 10",generateMenu(appStateValues))
            elif userInput == "7":
                img = cmpt120imageManip.increaseBrightness(img)
                cmpt120imageProj.showInterface(img,"Project Image Increased Brightness by 10",generateMenu(appStateValues))
            elif userInput == "8":
                state ["mode"] = "basic"
                cmpt120imageProj.showInterface(img,"Basic Functions",generateMenu(appStateValues))
            elif userInput == "9":
                state ["mode"] = "advanced"
                cmpt120imageProj.showInterface(img,"Advanced Functions",generateMenu(appStateValues))

        #These keys are allowed if the mode is changed to advanced
        elif state['mode'] == 'advanced':
            if userInput == "1":
                img = cmpt120imageManip.leftRotate(img)
                cmpt120imageProj.showInterface(img,"Project Image Rotated Left",generateMenu(appStateValues))
            elif userInput == "2":
                img = cmpt120imageManip.rightRotate(img)
                cmpt120imageProj.showInterface(img,"Project Image Rotated Right",generateMenu(appStateValues))
            elif userInput == "3":
                img = cmpt120imageManip.pixelate(img)
                cmpt120imageProj.showInterface(img,"Project Image Pixelated",generateMenu(appStateValues))
            elif userInput == "4":
                img = cmpt120imageManip.binarize(img)
                cmpt120imageProj.showInterface(img,"Project Image Binarized",generateMenu(appStateValues))
            elif userInput == "5":
                state ["mode"] = "basic"
                cmpt120imageProj.showInterface(img,"Basic Functions",generateMenu(appStateValues))
            elif userInput == "6":
                state ["mode"] = "intermediate"
                cmpt120imageProj.showInterface(img,"Intermediate Functions",generateMenu(appStateValues))

        # ***add the rest to handle other manipulation functionalities***

    else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput)

    return img

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")
