from PIL import Image

doggo = Image.open('doggo.jpg')
stamp = Image.open('stamp.jpg').resize(doggo.size).convert(doggo.mode)
blend = Image.blend(doggo, stamp, 0.2)
print(stamp.mode)


blend.show()