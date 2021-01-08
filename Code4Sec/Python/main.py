###
### Article Contributed By : Sakarin Kaewsathitwong
###

# pip install Pillow

import Steganography
import json
import binascii

def encodeImage():
    filename = "imageA.jpg"
    data = open("image_original/" + filename, 'rb').read().hex()
    datalist = {"name": filename, "data": data}
    data = json.dumps(datalist)

    img = "image_original/imageB.jpg"
    image = Steganography.Image.open(img, 'r')
    if (len(data) == 0):
        raise ValueError('Data is empty')

    newimg = image.copy()
    Steganography.encode_enc(newimg, data)

    new_img_name = "image_encode/imageinimage.png"
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

def decodeImage():
    data = json.loads(Steganography.decode())
    newFile = open("image_encode/" + data["name"], "wb")
    newFile.write(binascii.unhexlify((data["data"])))

choice = int(input(":: Welcome to Steganography (Image in Image) ::\n""1. Encode image\n2. Decode image\n"))
if (choice == 1):
    encodeImage()

elif (choice == 2):
    decodeImage()
else:
    raise Exception("Enter correct input")