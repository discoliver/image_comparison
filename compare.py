from PIL import Image
import time
import csv
import os
import sys

#Remove the old result file if exists, otherwise will let user know there is no result file in current folder
def remove_old_result():
    if os.path.exists('Test/result.csv'):
        os.remove('Test/result.csv')
    else:
        print("This is the first time you running this tool or you have deleted the previous result file")
        return;

#Read the input csv file with error handdling
def read_input_file():
    try:
        with open(sys.argv[1], 'r') as f:
            reader = csv.reader(f)
            next(reader)
            image_list = list(reader)
            return image_list
    except IndexError:
        print ('Opps You forget to add a cvs file, try python compare.py filename.cvs ....')
        raise

#Write the headline of the result file
def write_headline(c1, c2, c3, c4):
    with open('Test/result.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([c1, c2, c3, c4])

#Calculate the sum difference of R,G,B value in each pixel.
def calculate_diff(i1, new_i2):

    pairs = zip(i1.getdata(), new_i2.getdata())
    total_pixels = len(list(i1.getdata()))

    if len(i1.getbands()) == 1:
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(color1 - color2) for pixel1, pixel2 in pairs for color1, color2 in zip(pixel1, pixel2))
    dif_percentage = dif / (255.0 * 3 * total_pixels)
    return dif_percentage

#Write a row of compare result into result.cvs
def write_output(image_row):
    with open('Test/result.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(image_row)
    csvFile.close()

#Resize the image to match the size of the first image.
def resize(i1, i2):
    #print("size is different, resize to match the first image.")
    (width, height) = (i1.width, i1.height)
    i2 = i2.resize((width, height))
    return i2

def main():
    counter = 1

    remove_old_result()

    image_list = read_input_file()

    write_headline("image1", "image2", "similar", "elapsed")

    for image_row in image_list:

        i1 = Image.open(image_row[0])
        i2 = Image.open(image_row[1])

        #debug
        #print("image 1 size is ", i1.size, ", mode is ", i1.mode, ", band is ", i1.getbands(), "with total pixels of", total_pixels )
        #print("image 2 size is ", new_i2.size, ", mode is ", new_i2.mode, ", band is ", new_i2.getbands(), "with total pixels of", total_pixels )
        if i1.size != i2.size:
            new_i2 = resize(i1, i2)

        print('Operating the image pair:', counter)

        start_time = time.time()

        dif_percentage = calculate_diff(i1, new_i2)

        elapsed_time = time.time() - start_time

        image_row.insert(2, dif_percentage)
        image_row.insert(3, elapsed_time)

        write_output(image_row)
        counter = counter+1

    #Debug: Qucik output for preview
    # with open("result.csv") as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print(" ".join(row))

if __name__ == "__main__":
    main()