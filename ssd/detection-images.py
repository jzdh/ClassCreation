from gluoncv import model_zoo,data,utils
from matplotlib import pyplot as plt
import os
import cv2
import numpy
count=0
focalLength=100
CAR_WIDTH=80
PERSON_WIDTH=20
pre_path='/home/anner/code/gluoncv/ssd/'
images_path=pre_path+'temp/'
pro_images_path=pre_path+'pro_images/'
net=model_zoo.get_model('ssd_512_resnet50_v1_voc',pretrained=True)
for name in os.listdir(images_path):
    path=images_path+name
    count+=1
    x,img=data.transforms.presets.ssd.load_test(path,short=512)
    class_IDS,scores,bounding_boxs=net(x)
    for i in range(len(class_IDS[0])):
        left_top_x=bounding_boxs[0][i][0].asscalar()
        left_top_y=bounding_boxs[0][i][1].asscalar()
        right_bottom_x=bounding_boxs[0][i][2].asscalar()
        right_bottom_y=bounding_boxs[0][i][3].asscalar()
        if scores[0][i]>0.5:
            if class_IDS[0][i]==1:
                cv2.rectangle(img,(left_top_x,left_top_y),(right_bottom_x,right_bottom_y),(0,0,255),2)
    if os.path.exists(pro_images_path+name):
        print('error:file already exist')
    else:
        cv2.imwrite(pro_images_path+name,img)   
        print(name)
