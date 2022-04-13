import h5py
import os
import time

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
        
path = 'bush_1000obj_3000pts'
cate = os.listdir(path)
cate = sorted(cate)
progress = 0
if(not os.path.isdir('Result')):	os.mkdir('Result')
for c in cate:
	hfiles = os.listdir(path+'/'+c)
	hfiles = sorted(hfiles)
	if(not os.path.isdir('Result/'+c)):	os.mkdir('Result/'+c)
	for h in hfiles:
		time.sleep(0.1)
		printProgressBar(progress, len(cate)*len(hfiles), prefix = 'Progress:', suffix = c+' '+h, length = 30)
		progress=progress+1
		f  = open('Result/'+c+'/'+h+'.pts', "w")
		fp = h5py.File(path+'/'+c+'/'+h,"r")
		Data = fp.get("data")
		for i in range(len(Data)):
			f.write(str(Data[i]).strip('[]')+'\n')
		f.close()
		

