import cv2

cap = cv2.VideoCapture("train/Action/100219.mp4")
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)

duration = length/fps
duration *= 2
frequency = int(length/duration)

success,image = cap.read()
count = 0
rcount = 0
success = True
while success:
	success,image = cap.read()
	print(rcount,frequency)
	if(rcount == frequency):
		cv2.imwrite("frames/100219_%d.jpg" % count, image)
		count += 1
		rcount = 0
	rcount += 1
