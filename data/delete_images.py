import os


# process = subprocess.Popen('rm /home/mangolin/Desktop/five-video-classification-methods/data/train/Ac*/11*.jpg', stdout=subprocess.PIPE)
# output, error = process.communicate()
# print(output,error)

for r,s,f in os.walk('train'):
	print(r)
	for file in f:
		if('jpg' in file):
			# print(os.path.getsize(f))
			# os.remove(r+'/'+file)