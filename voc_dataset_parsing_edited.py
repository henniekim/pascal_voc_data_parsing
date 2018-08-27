#
import numpy as np
import cv2
from bs4 import BeautifulSoup
import os
import glob
import argparse

# Creating a parser
parser = argparse.ArgumentParser()

# Parameter passing from command line 
parser.add_argument('--dataPath', type=str, default='/datahdd/workdir/donghyun/faster_rcnn_kdh/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/',  help='The folder Which containts dataset : */*/VOCtrainval_11-May-2012/VOCdevkit/VOC2012')
parser.add_argument("--years", type=str, nargs='+',  default="all", help="Select the year to parse")

args = parser.parse_args()
 
dataPath = args.dataPath 
categoryPath = 'Annotations/'
imagePath = 'JPEGImages/'
#years = ('2007', '2008', '2009', '2010', '2011', '2012')
years = args.years
endOfData = (9950, 8773, 5331, 6994, 7214, 4331)

filenumber = '0'
name = list()
xmin = list()
ymin = list()
xmax = list()
ymax = list()
a = list()
count = 0
img = list()
numberOfFile = 0

for i in range(len(years)):
    year = years[i]
    EOD = int(year)-2007
    for currentDataNumber in range(endOfData[EOD]):
        if 0 <= currentDataNumber and currentDataNumber < 10 :
            filenumber = '00000'
        elif 10 <= currentDataNumber and currentDataNumber < 100 :
            filenumber = '0000'
        elif 100 <= currentDataNumber and currentDataNumber < 1000 :
            filenumber = '000'
        elif 1000 <= currentDataNumber and currentDataNumber < 10000 :
            filenumber = '00'

        filenumber = filenumber + str(currentDataNumber)
        url_annotation = dataPath+categoryPath+year+'_'+filenumber+'.xml'
        url_image = dataPath+imagePath+year+'_'+filenumber+'.jpg'
        print(str(filenumber))

        try :
            ## for annotations ##
            xml = open(url_annotation, "r", encoding="utf-8").read()

            ## for images ##
            img = cv2.imread(url_image)
            numberOfFile += 1
            pass
        except :
            print("Image doesn't exist : " + filenumber)
            continue

        soup = BeautifulSoup(xml, 'html.parser')

        for size in soup.find_all('size'):
            width = size.find('width').string
            height = size.find('height').string
            depth = size.find('depth').string

        for object in soup.find_all('object'):
            name = object.find('name').string # edited
            for bndbox in object.find_all('bndbox'):
                xmin = object.find('xmin').string
                ymin = object.find('ymin').string
                xmax = object.find('xmax').string
                ymax = object.find('ymax').string

            # print('width : ' + width)
            # print('height : ' + height)
            # print('depth : ' + depth)
            #
            # print('label : ' + str(name))
            # print('xmin : ' + str(xmin))
            # print('ymin : ' + str(ymin))
            # print('xmax : ' + str(xmax))
            # print('ymax : ' + str(ymax))

            font = cv2.FONT_HERSHEY_SIMPLEX
            xmin = int(float(xmin))
            xmax = int(float(xmax))
            ymin = int(float(ymin))
            ymax = int(float(ymax))
            crop = img[int(ymin): int(ymax), int(xmin):int(xmax)]

            ## for one hot encoding ##
            if name == 'person':
                name = (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
            elif name == 'bird':
                name = (0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
            elif name == 'cat':
                name = (0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
            elif name == 'cow':
                name = (0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
            elif name == 'dog':
                name = (0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
            elif name == 'horse':
                name = (0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
            elif name == 'sheep':
                name = (0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0)
            elif name == 'aeroplane':
                name = (0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0)
            elif name == 'bicycle':
                name = (0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
            elif name == 'boat':
                name = (0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0)
            elif name == 'bus':
                name = (0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0)
            elif name == 'car':
                name = (0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0)
            elif name == 'motorbike':
                name = (0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0)
            elif name == 'train':
                name = (0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0)
            elif name == 'bottle':
                name = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0)
            elif name == 'chair':
                name = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0)
            elif name == 'diningtable':
                name = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0)
            elif name == 'pottedplant':
                name = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0)
            elif name == 'sofa':
                name = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0)
            elif name == 'tvmonitor':
                name = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1)

            file_name = 'pascal_voc_' + str(count)
            crop = cv2.resize(crop, dsize=(224, 224))
            count += 1
            cv2.imwrite("./PascalDataSetCroppedEdited/" + file_name +'.jpg', crop)
            np.savetxt("./PascalDataSetCroppedEdited/" + file_name+'.txt', name , delimiter=' ', encoding='utf-8')

            print('from '+str(numberOfFile)+'th file '+str(count) + ' images have been successfully made !!')
