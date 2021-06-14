# USAGE
# python search.py --index index.csv --query queries/103100.png --result-path dataset

# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import numpy as np
import cv2
import os
import glob
from skimage import io
from skimage.color import rgb2gray

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))
video = args["query"]
cap = cv2.VideoCapture(args["query"])
# load the query image and describe it
# query = cv2.imread(args["query"])
path_video = []
if cap.isOpened():
    rval , frame = cap.read()
else:
	rval = False
i=0
temp = "/home/ankita/btp7/final/temp"
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



for img in glob.glob(temp+'/*png'):
	
	image = io.imread(img)
	
	im= rgb2gray(image)
	avg_int.append(np.mean(im))

diff = [avg_int[p+1]-avg_int[p] for p in range(len(avg_int)-1)]
        
print (diff.index(max(diff)))
name1 = temp+'/'+ str(diff.index(max(diff))) +'.png'
im1 = cv2.imread(name1)
name_im = temp+'/query.png'
cv2.imwrite(os.path.join(temp ,name_im ), im1)



query = cv2.imread(name_im)


features = cd.describe(query)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)

# display the query
cv2.imshow("Query", query)
cv2.waitKey(0)
# loop over the results
for (score, resultID) in results:
	# load the result image and display it
	result = cv2.imread(args["result_path"] + "/" + resultID)

	cv2.imshow("Result", result)
	cv2.waitKey(0)
	print (resultID)
	fold = resultID.split('#')[0]
	x = resultID.split('#')[1]

	name = x.rsplit('_',1)[0]
	print (fold)
	
	
	
	
	arr = os.listdir('data/'+fold)
	ext = arr[0].split('.')[1]

	video = 'data/'+fold+'/'+name+'.'+ext
	path_video.append(video)
	
	print (video)
	# cap =  cv2.VideoCapture(video)
	# print cap.isOpened()
		
	# while(cap.isOpened()):
	# 	ret, frame = cap.read()

	# 	cv2.imshow('frame',frame)
	# 	if cv2.waitKey(1) & 0xFF == ord('q'):
	# 		break

	# cap.release()
	# cv2.waitKey(0.5)


for the_file in os.listdir(temp):
	file_path = os.path.join(temp, the_file)
	try:
		if os.path.isfile(file_path):
			os.unlink(file_path)
		#elif os.path.isdir(file_path): shutil.rmtree(file_path)
	except Exception as e:
		print(e)


print (path_video)
