# importing the Image module from Python Imaging Library
from PIL import Image
import time
import csv
import os

if os.path.exists('result.csv'):
    os.remove('result.csv')
else:
    print("First time running this tool or you have deleted the previous result file")

with open('images.csv', 'r') as f:
  reader = csv.reader(f)
  next(reader)
  image_list = list(reader)

with open('result.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['image1','image2','similar','elapsed'])

for image_row in image_list:
    start_time = time.time()

    i1 = Image.open(image_row[0])
    i2 = Image.open(image_row[1])

    if i1.size != i2.size:
        print ("size is different, resize to match the first image.")
        (width, height) = (i1.width, i1.height)
        i2 = i2.resize((width, height))
    pairs = zip(i1.getdata(), i2.getdata())
    total_pixels = len(list(i1.getdata()))

    #debug --
    print("image 1 size is ", i1.size, ", mode is ", i1.mode, ", band is ", i1.getbands(), "with total pixels of", total_pixels )
    print("image 2 size is ", i2.size, ", mode is ", i2.mode, ", band is ", i2.getbands(), "with total pixels of", total_pixels )

    dif = sum(abs(color1 - color2) for pixel1, pixel2 in pairs for color1, color2 in zip(pixel1, pixel2))
    dif_percentage =  dif / ( 255.0 * 3 * total_pixels )
    elapsed_time = time.time() - start_time

    image_row.insert(2, dif_percentage)
    image_row.insert(3, elapsed_time)

    with open('result.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(image_row)
    csvFile.close()

with open("result.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(" ".join(row))

