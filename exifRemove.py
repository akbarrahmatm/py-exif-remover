from PIL import Image
import uuid


def removeExif(img):
    image = Image.open(img)
    
    imgData = list(image.getdata())
    imageExifRemove = Image.new(image.mode, image.size)
    imageExifRemove.putdata(imgData)

    fileName = uuid.uuid4().hex + ".jpg"

    imageExifRemove.save(fileName)
    imageExifRemove.close()

imgPath = input("Insert image path : ")

removeExif(imgPath)