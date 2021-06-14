import os
from skimage import io
import numpy as np
from skimage.color import rgb2gray
import glob
import matplotlib.pyplot as plt
import cv2
import os, shutil

path = "/Geek/Desktop/Project Final/CBVR/data"
temp = "/Geek/Desktop/Project Final/CBVR/temp"
data = "/Geek/Desktop/Project Final/CBVR/keyframes"

for fold in os.listdir(path):
    # print fold
    path2 = path + '/'+fold
    for video in os.listdir(path2):
        i=0
        path_video = path +'/'+fold+'/'+ video
        # print path_video
        cap = cv2.VideoCapture(path_video)
        if cap.isOpened():
            rval , frame = cap.read()
        else:
            rval = False
        print (rval)
        print (video)
        while rval:
            
            rval, frame = cap.read()
            if not rval : break
            name = str(i) +'.png'
            cv2.imwrite(os.path.join(temp ,name ), frame)
            i=i+1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        avg_int = []
        no_frames = i
        print (no_frames)
    
        for img in glob.glob(temp+'/*png'):
            
            image = io.imread(img)
            
            im= rgb2gray(image)
            avg_int.append(np.mean(im))
           

            # print(np.mean(im))   

        # for i in avg_int:
        #     print i

        diff = [avg_int[p+1]-avg_int[p] for p in range(len(avg_int)-1)]
        
        print (diff.index(min(diff)))
        name1 = temp+'/'+ str(diff.index(min(diff))) +'.png'

        print (diff.index(max(diff)))
        name2 = temp+'/'+ str(diff.index(max(diff))) +'.png'

        image1 = cv2.imread(name1)
        save_name = fold +"#"+ video.split('.')[0]+'_1.png'
        cv2.imwrite(os.path.join(data ,save_name ), image1)
        image2 = cv2.imread(name2)
        save_name = fold +"#"+ video.split('.')[0]+'_2.png'
        cv2.imwrite(os.path.join(data ,save_name ), image2)



        for the_file in os.listdir(temp):
            file_path = os.path.join(temp, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)


        


       

            

