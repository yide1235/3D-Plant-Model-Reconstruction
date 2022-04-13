import os
import random
import math
from pathlib import Path
Path = '123' ## 更改 ## 输入pts文件夹名称，此文件与pts文件夹在同目录下
Categories = os.listdir(Path)
Categories = sorted(Categories)
if(not os.path.isdir('ShapeNetCompletion')):	os.mkdir('ShapeNetCompletion')
if(not os.path.isdir('ShapeNetCompletion/train')):    os.mkdir('ShapeNetCompletion/train')
if(not os.path.isdir('ShapeNetCompletion/train/complete')):    os.mkdir('ShapeNetCompletion/train/complete')
if(not os.path.isdir('ShapeNetCompletion/train/partial')):    os.mkdir('ShapeNetCompletion/train/partial')
if(not os.path.isdir('ShapeNetCompletion/test')):    os.mkdir('ShapeNetCompletion/test')
if(not os.path.isdir('ShapeNetCompletion/test/complete')):    os.mkdir('ShapeNetCompletion/test/complete')
if(not os.path.isdir('ShapeNetCompletion/test/partial')):    os.mkdir('ShapeNetCompletion/test/partial')
if(not os.path.isdir('ShapeNetCompletion/val')):    os.mkdir('ShapeNetCompletion/val')
if(not os.path.isdir('ShapeNetCompletion/val/complete')):    os.mkdir('ShapeNetCompletion/val/complete')
if(not os.path.isdir('ShapeNetCompletion/val/partial')):    os.mkdir('ShapeNetCompletion/val/partial')

Rate = 8
Mode = ''
lowest = 100000

for category in Categories:
	PTS_Files = os.listdir(Path + '/' + category)
	PTS_Files = sorted(PTS_Files)
	for i in range(len(PTS_Files)):
		print(i)
		f_pts = open(Path + '/' + category + '/' + PTS_Files[i], "r")
		lines = f_pts.readlines()
		f_pts.close()
		if lowest > len(lines): lowest = len(lines)
    	
print(lowest)

f_json = open('ShapeNet.json', "w")
f_json.write('[')
for category in Categories:
    f_json.write('\n\t{')
    f_json.write('\n\t\t"taxonomy_id": "'+category+'",\n\t\t"taxonomy_name": "'+category+'",')
        
    if(not os.path.isdir('ShapeNetCompletion/train/complete/'+category)):    os.mkdir('ShapeNetCompletion/train/complete/'+category)
    if(not os.path.isdir('ShapeNetCompletion/train/partial/'+category)):    os.mkdir('ShapeNetCompletion/train/partial/'+category)
    if(not os.path.isdir('ShapeNetCompletion/test/complete/'+category)):    os.mkdir('ShapeNetCompletion/test/complete/'+category)
    if(not os.path.isdir('ShapeNetCompletion/test/partial/'+category)):    os.mkdir('ShapeNetCompletion/test/partial/'+category)
    if(not os.path.isdir('ShapeNetCompletion/val/complete/'+category)):    os.mkdir('ShapeNetCompletion/val/complete/'+category)
    if(not os.path.isdir('ShapeNetCompletion/val/partial/'+category)):    os.mkdir('ShapeNetCompletion/val/partial/'+category)
    
    PTS_Files = os.listdir(Path + '/' + category)
    PTS_Files = sorted(PTS_Files)
    print(PTS_Files)
    rannum = list(range(len(PTS_Files)))
    random.shuffle(rannum)
    
    unit = int(len(PTS_Files)/10)
    num1 = 150
    num2 = len(PTS_Files) - 250
    num3 = 100
    m1 = True
    m2 = True
    m3 = True
    for i in range(len(PTS_Files)):
    	index = rannum[i]
    	print(category,i,index,PTS_Files[index])
    	
    	if num1 > 0:
    		Mode = 'test'
    		Rate = 1	## 更改 ## 对于每一个pts文件 生成的不完整pcd文件的数量
    		if m1:
    			f_json.write('\n        "'+Mode+'": [')
    			m1 = False
    		if num1 == 1:	f_json.write('\n            "'+category+'_'+str(index)+'"')
    		else:	f_json.write('\n            "'+category+'_'+str(index)+'",')
    		num1 = num1 - 1
    	elif num2 > 0:
    		Mode = 'train'
    		Rate = 8
    		if m2:
    			f_json.write('\n        ],\n        "'+Mode+'": [')
    			m2 = False
    		if num2 == 1:	f_json.write('\n            "'+category+'_'+str(index)+'"')
    		else:	f_json.write('\n            "'+category+'_'+str(index)+'",')
    		num2 = num2 - 1
    	else:
    		Mode = 'val'
    		Rate = 1
    		if m3:
    			f_json.write('\n        ],\n        "'+Mode+'": [')
    			m3 = False
    		if num3 == 1:	f_json.write('\n            "'+category+'_'+str(index)+'"\n        ]\n    }')
    		else:	f_json.write('\n            "'+category+'_'+str(index)+'",')
    		num3 = num3 - 1  	
    	
    	f_pts = open(Path + '/' + category + '/' + PTS_Files[index], "r")
    	lines = f_pts.readlines()
    	f_pts.close()
    	TotalPoints = lowest
    	
    	f_gt = open('ShapeNetCompletion/'+Mode+'/complete/'+category+'/'+category+'_'+str(index)+'.pcd', "w")
    	f_gt.write('# .PCD v0.7 - Point Cloud Data file format\nVERSION 0.7\nFIELDS x y z\nSIZE 4 4 4\nTYPE F F F\nCOUNT 1 1 1\nWIDTH ' + str(TotalPoints) + '\nHEIGHT 1\nVIEWPOINT 0 0 0 1 0 0 0\nPOINTS ' + str(TotalPoints) +'\nDATA ascii\n')
    	for j in range(TotalPoints):
    		f_gt.write(lines[j])
    	f_gt.close()
    	
    	xorig = []
    	yorig = []
    	zorig = []
    	if(not os.path.isdir('ShapeNetCompletion/'+Mode+'/partial/'+category+'/'+category+ '_'+ str(index))):    os.mkdir('ShapeNetCompletion/'+Mode+'/partial/'+category+'/'+category+ '_'+ str(index))
    	for j in range(TotalPoints):
    		tmp = lines[j].split()
    		xorig.append(float(tmp[0]))
    		yorig.append(float(tmp[1]))
    		zorig.append(float(tmp[2]))
    	for j in range(Rate):
    		x = xorig[:]
    		y = yorig[:]
    		z = zorig[:]
    		CenterPoint = random.randint(0,lowest-1)
    		Cx = x[CenterPoint]
    		Cy = y[CenterPoint]
    		Cz = z[CenterPoint]
    		CurrentTotalPoints = TotalPoints
    		DeleteSize = 3
    		k = 0
    		while k < CurrentTotalPoints:
    			distance = math.sqrt(abs(x[k]-Cx)**2+abs(y[k]-Cy)**2+abs(z[k]-Cz)**2)
    			if distance < DeleteSize:
    				x.pop(k)
    				y.pop(k)
    				z.pop(k)
    				CurrentTotalPoints = CurrentTotalPoints - 1
    				k = k - 1
    			k = k + 1
    		
    		f_partial = open('ShapeNetCompletion/'+Mode+'/partial/'+category+'/'+category+ '_'+ str(index)+'/0'+ str(j)+ '.pcd', "w")
    		f_partial.write('# .PCD v0.7 - Point Cloud Data file format\nVERSION 0.7\nFIELDS x y z\nSIZE 4 4 4\nTYPE F F F\nCOUNT 1 1 1\nWIDTH ' + str(CurrentTotalPoints) + '\nHEIGHT 1\nVIEWPOINT 0 0 0 1 0 0 0\nPOINTS ' + str(CurrentTotalPoints) +'\nDATA ascii')
    		for k in range(CurrentTotalPoints):
    			f_partial.write('\n'+str(x[k])+' '+str(y[k])+' '+str(z[k]))
    		f_partial.close()
	
f_json.write('\n]')
f_json.close()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	




