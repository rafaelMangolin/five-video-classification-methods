import os


# process = subprocess.Popen('rm /home/mangolin/Desktop/five-video-classification-methods/data/train/Ac*/11*.jpg', stdout=subprocess.PIPE)
# output, error = process.communicate()
# print(output,error)
i = 0
for r,s,f in os.walk('test'):
	print(i)
	i+=1
	for file in f:
		size = os.path.getsize(r+'/'+file)
		if('jpg' in file and size == 0):
			print(size,r,file)
			os.remove(r+'/'+file)
