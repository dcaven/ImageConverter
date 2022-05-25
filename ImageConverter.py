from urllib import response
from PIL import Image
from os.path import exists

def webpToPNG(oldBaseFilePath, oldFileName, oldFileExtension, newBaseFilePath, newFileName, newFileExtension) :
    try :
        if exists(oldBaseFilePath + oldFileName + oldFileExtension) :
            response = input("File already exists and will be overwritten. Continue? (y/n)  ")
            if(response != "y" and response != "Y"):
                print("File not overwritten.")
                return

        print("Starting Conversion")
        file = Image.open(oldBaseFilePath + oldFileName + oldFileExtension).convert("RGB")
        file.save(newBaseFilePath + newFileName + newFileExtension, newFileExtension[1:])
        print("Success. File output to: " + newBaseFilePath + newFileName + newFileExtension)
    except Exception:
        print("Conversion failed: ", Exception)

oldBaseFilePath = "C:\\Users\\David Caven\\Pictures\\wallpaper\\"
oldFileName = "blackhole"
oldFileExtension = ".webp"
newBaseFilePath = "C:\\Users\\David Caven\\Pictures\\wallpaper\\"
newFileName = "blackhole"
newFileExtension = ".png"

webpToPNG(oldBaseFilePath, oldFileName, oldFileExtension, newBaseFilePath, newFileName, newFileExtension)