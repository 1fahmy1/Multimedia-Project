# USAGE
# python search.py --index index.csv --query queries/example.mp4 --result-path dataset

# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import cv2
import os
import glob
from skimage import io
from skimage.color import rgb2gray
import numpy as np
# from matplotlib import pyplot as plt

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--index", required = True,
# 	help = "Path to where the computed index will be stored")
# ap.add_argument("-q", "--query", required = True,
# 	help = "Path to the query image")
# ap.add_argument("-r", "--result-path", required = True,
# 	help = "Path to the result path")
# args = vars(ap.parse_args())
def searchVideo(query):

	index = "index.csv"

	# initialize the image descriptor
	cd = ColorDescriptor((8, 12, 3))

	# load the query video and describe it
	temp = "/home/ankita/btp7/CBVR/temp"
	i=0
	# print path_video
	cap = cv2.VideoCapture("uploadedFiles/"+query)
	if cap.isOpened():
		rval , frame = cap.read()
	else:
		rval = False
	# print rval
	# print query
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
	# print no_frames

	for img in glob.glob(temp+'/*png'):

		image = io.imread(img)

		im= rgb2gray(image)
		avg_int.append(np.mean(im))


		# print(np.mean(im))

	# for i in avg_int:
	#     print i

	diff = [avg_int[p+1]-avg_int[p] for p in range(len(avg_int)-1)]

	# y = diff
	# plt.plot(y)
	# plt.show()
	# print diff.index(min(diff))
	name1 = temp+'/'+ str(diff.index(min(diff))) +'.png'

	# print diff.index(max(diff))
	name2 = temp+'/'+ str(diff.index(max(diff))) +'.png'

	# image1 = cv2.imread(name1)
	# save_name = fold +"#"+ video.split('.')[0]+'_1.png'
	# cv2.imwrite(os.path.join(data ,save_name ), image1)
	# image2 = cv2.imread(name2)
	# save_name = fold +"#"+ video.split('.')[0]+'_2.png'
	# cv2.imwrite(os.path.join(data ,save_name ), image2)


	query_image = cv2.imread(name2)

	for the_file in os.listdir(temp):
		file_path = os.path.join(temp, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
			#elif os.path.isdir(file_path): shutil.rmtree(file_path)
		except Exception as e:
			print(e)


	# query = cv2.imread(args["query"])
	features = cd.describe(query_image)

	# perform the search
	searcher = Searcher(index)
	results = searcher.search(features)

	result_images = []
	# display the query
	# cv2.imshow("Query", query_image)

	# loop over the results
	path_video = []
	# path_video.append("uploadedFiles/"+query)
	for (score, resultID) in results:
		# load the result image and display it
		result = cv2.imread("data/"+ resultID)
		result_images.append(result)
		fold = resultID.split('#')[0]
		x = resultID.split('#')[1]

		name = x.rsplit('_',1)[0]
		# print fold




		arr = os.listdir('data/'+fold)
		ext = arr[0].split('.')[1]

		video = 'data/'+fold+'/'+name+'.'+ext
		path_video.append(video)

		# print video
		# cv2.imshow("Result", result)
		# cv2.waitKey(0)
	return path_video
	# print path_video

# searchVideo("car (4).wmv")

# plt.subplot(4,4,2),plt.imshow(query)
# plt.title('Query'), plt.xticks([]), plt.yticks([])
#
# plt.subplot(4,4,5),plt.imshow(result_images[0])
# plt.title('Result 1'), plt.xticks([]), plt.yticks([])
