from PIL import Image
import face_recognition
from os import listdir
from time import sleep
import os
 
 #2 typical cases: 1. non-face 2. angle or photo tilt
def list_files1(directory, extension):
    return (f for f in listdir(directory) if f.endswith('.' + extension))

dir="C:\\temp\\photo"
files=list_files1(dir,"jpg")
for file in files:

	image = face_recognition.load_image_file(os.path.join(dir,file))
	Image.fromarray(image).show()
	face_landmarks_list = face_recognition.face_landmarks(image)

	face_locations = face_recognition.face_locations(image)

	if face_locations:

		print(face_locations[0])
		top, right, bottom, left = face_locations[0]
		ok=top,left,bottom-top,right-left
		
		'''
		# Print the location of each face in this image
		    top, right, bottom, left = face_location
		print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
		'''

		pil_image = Image.fromarray(image)
		# The crop rectangle, as a (left, upper, right, lower)-tuple.

		pil_image.crop((left,top,right,bottom)).show()#.save("test.jpg")
		sleep(2)
