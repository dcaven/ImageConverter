#pip install PIL
from PIL import Image
from os.path import exists
import os

def webpToPNG(oldBaseFilePath, oldFileName, oldFileExtension, newBaseFilePath, newFileName, newFileExtension) :
    try :
        if exists(newBaseFilePath + newFileName + newFileExtension) == True :
            response = input("File already exists and will be overwritten. Continue? (y/n)  ")
            if(response != "y" and response != "Y"):
                print("File not overwritten.")
                return

        print("Starting Conversion")
        file = Image.open(oldBaseFilePath + oldFileName + oldFileExtension).convert("RGB")
        file.save(newBaseFilePath + newFileName + newFileExtension, newFileExtension[1:])
        print("Success. File output to: " + newBaseFilePath + newFileName + newFileExtension)
    except Exception as e:
        print("Conversion failed: ", e)

def main():
    # oldBaseFilePath = ""C:\\my\\file\\path\\here\\"
    # oldFileName = "myFileNameHere"
    # oldFileExtension = ".webp"
    # newBaseFilePath = ""C:\\my\\file\\path\\here\\"
    # newFileName = "myFileNameHere"
    # newFileExtension = ".png"
    # webpToPNG(oldBaseFilePath, oldFileName, oldFileExtension, newBaseFilePath, newFileName, newFileExtension)
    convertAllPicturesInDirectory("C:\\my\\file\\path\\here\\", ".webp")

def convertAllWebpPicturesInDirectoryToPNG(directory, oldExtension):
    oldExtension = ".webp"
    newFileExtension = ".png"

    files = os.listdir(directory)
    for file in files:
        if file.endswith(oldExtension):
            fileWithoutExtension = file.replace(oldExtension, "")
            webpToPNG(directory, fileWithoutExtension, oldExtension, directory, fileWithoutExtension, newFileExtension)

if(__name__ == "__main__"):
    main()