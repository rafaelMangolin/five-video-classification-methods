fp = open('0.txt','r+')
content = fp.read().split('\n')

new = []
for x in content:
	if(len(x)>0 and x[0] == '('):
		new.append(x.replace('(','').replace(')','').replace(' ','').replace('\'','').split(',')[2].split('_')[0])

fp = open('data_file.csv','r+')
content = fp.read().split('\n')
content.pop()


correct = []
j = 0
for i in content:
	i = i.split(',')
	if(i[2] in new):
		i[3] = str(int(i[3])-1)
		j+=1
	correct.append(','.join(i)) 

print(len(new),j)

correct.append('')

fp = open('data_file_1.csv','w+')
fp.write('\n'.join(correct))