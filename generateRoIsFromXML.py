import os
import xml.etree.ElementTree as ET
import glob
import cv2 as cv
import numpy as np

###generate ROIs from CAD dataset


if __name__ == '__main__':
    TYPE = '0_0'
    paths = glob.glob('D:/MatchingEx/dataCAD/CADSamples300/' + TYPE + 'CADSamples/*.png'); #xml file path
    #print(paths)
    #print(len(paths))
    savecropsdir = 'D:/MatchingEx/dataCAD/CADSamples300/' + TYPE + 'ROIs'  #saving crop path
    if not os.path.exists(savecropsdir):
        os.mkdir(savecropsdir)
    for path in paths:
        filename = os.path.basename(path)
        filename,_ = os.path.splitext(filename)
        #print(imagepath)
        image = cv.imread(path) #read image
        #print(type(image))

        grayimage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        ret, bw = cv.threshold(grayimage, 10, 255, cv.THRESH_BINARY)
        #print(type(bw), (bw.shape))
        y, x = np.nonzero(bw)
        xmin = min(x)-2
        ymin = min(y)-2
        xmax = max(x)+2
        ymax = max(y)+2
        #print(xmin, ymin, xmax, ymax)
        RoI = image[ymin:ymax, xmin:xmax, :]
        width = xmax - xmin
        height = ymax - ymin
        if height >= width:
            RoI2 = cv.resize(RoI, (int(width*150//height), 150))
        else:
            RoI2 = cv.resize(RoI, (150, int(height * 150 // width)))
        savepath = os.path.join(savecropsdir, filename+'.bmp')
        cv.imwrite(savepath, RoI2)

        # cv.rectangle(bw, (xmin, ymin), (xmax, ymax), (255, 0, 0), 1)
        # cv.namedWindow('1')
        # cv.imshow('1', bw)
        # cv.waitKey()


'''
###generate ROIs from XML files of Realdataset.
if __name__ == '__main__':
    paths = glob.glob('D:/MatchingEx/dataReal/45_0_a_annotation/*.xml'); #xml file path
    #print(paths)
    print(len(paths))
    savecropsdir = 'D:/MatchingEx/dataReal/aaa'  #saving crop path
    if not os.path.exists(savecropsdir):
        os.mkdir(savecropsdir)
    for path in paths:
        [filedir, extname] = os.path.splitext(path)
        imagepath = filedir + '.bmp'                #image path
        filename = os.path.basename(filedir)
        #print(imagepath)
        image = cv.imread(imagepath) #read image
        #print(type(image))
        tree = ET.parse(path) #read xml
        objs = tree.findall('object')
        boxes = np.zeros([len(objs), 4], dtype=np.int16)
        for i, obj in enumerate(objs):
            bbx_temp = obj.find('bndbox')
            xmin = int(bbx_temp.find('xmin').text)-1
            xmax = int(bbx_temp.find('xmax').text)-1
            ymin = int(bbx_temp.find('ymin').text)-1
            ymax = int(bbx_temp.find('ymax').text)-1
            boxes[i,:] = [xmin, ymin, xmax, ymax]
            print('width:', xmax-xmin)
            print('height:', ymax-ymin)
            RoI = image[ymin:ymax, xmin:xmax, :]
            width = xmax - xmin
            height = ymax - ymin
            if height >= width:
                RoI2 = cv.resize(RoI, (int(width*150//height), 150))
            else:
                RoI2 = cv.resize(RoI, (150, int(height * 150 // width)))
            savepath = os.path.join(savecropsdir, filename+'.bmp')
            cv.imwrite(savepath, RoI2)

        #     cv.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 1)
        # cv.namedWindow('1')
        # cv.imshow('1', image)
        # cv.waitKey()
'''
