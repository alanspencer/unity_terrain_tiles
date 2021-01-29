from PIL import Image
Image.MAX_IMAGE_PIXELS = 500000000

numberTilesX = 4 #4
numberTilesY = 7 #7
tileWidth = 1024
titleHeight = 1024
tilesNameXList = ["A", "B", "C", "D"]
masterDirectory = "S:\\OneDrive - Imperial College London\\Teaching\\Virtual South Spain 2020\\Field-Programme\\Mapping-Area\\QGIS\\"
masterImagePath = "DEMWholeArea.tif"
outputFolder = "DEMTiles\\"

# Open image
print("Loading master image to memory...")
masterImage = Image.open(masterDirectory + masterImagePath, "r")
#masterImage.convert('RGB')
print("... DONE!")

width, height = masterImage.size
print(str.format("Image size: X: {0} Y: {1}", width, height))


# Loop though columns first
x = 0
while x < numberTilesX:
    y = 0
    while y < numberTilesY:
        currentName = str.format("tile_{0}{1}.tiff", tilesNameXList[x], y)

        # Create new blank image of tileWidth x titleHeight
        newImg = Image.new('I;16', (tileWidth, titleHeight), 0x000000)

        # Now lets get the pixel values from the master image
        if(x == 0):
            startingX = 0
            endingX = 1024
        else:
            startingX = 1024 * x
            endingX = startingX + 1024

        if(y == 0):
            startingY = 0
            endingY = 1024
        else:
            startingY = 1024 * y
            endingY = startingY + 1024

        print(str.format("Getting Image Info For: X {0}-{1} and Y {2}-{3}", startingX, endingX, startingY, endingY))

        currentX = 0
        localStartingX = startingX
        while localStartingX < endingX:
            currentY = 0
            localStartingY = startingY
            while localStartingY < endingY:
                i = masterImage.getpixel((localStartingX, localStartingY))
                
                #print(str.format("I: {0}  -> Pixel X: {1} Y: {2}", i, currentX, currentY))
                #print(str.format("Pixel X: {0} Y: {1}", currentX, currentY))
                
                newImg.putpixel((currentX, currentY), i)

                localStartingY += 1
                currentY += 1

            localStartingX += 1
            currentX += 1
            
        #newImg.show()

        print("Saving: " + currentName)
        newImg.save(masterDirectory + outputFolder + currentName)
        
        y += 1

    x += 1
