import pickle
import numpy as np

def save2file(varname):
	filename = "C:\\Python27\\m_data\\%s.dat"%varname
	f=open(filename,'wb')  
	eval("pickle.dumps(%s,f)"%varname)

def load4file(varname):
	filename = "C:\\Python27\\m_data\\%s.dat"%varname
	print(filename)
	f=open(filename,'rb')
	return pickle.load(f)

def kelly(b,p):
        return (b*p - (1-p))/b

discrete_x_all = load4file("discrete_x_all")
y_all = load4file("y_all")
print(len(discrete_x_all))
print(len(y_all))
resX = {}
resY = {}
for i in range(1,len(y_all)):
        s = str(discrete_x_all[i])
        if s not in resX:
                resX[s]=1
        else:
                resX[s]+=1
        
        if s not in resY:
                resY[s]=0
        if y_all[i]:
                resY[s]+=1

for s in resX:
        print "%s\t%d\t%d\t%.2f"%(s,resX[s],resY[s],resY[s]*1.0/resX[s]*100)

#open,morn(1,2),high,low
info = str([-1,-3,-1,-1])
money = 646.77
#f =£¨bp-q)/b
b = 0.022
p = resY[info]*1.0/resX[info]
#p = 0.15
print "Pwin:\t%.2f%%"% (p*100)
fup = kelly(b,p)
print "UP:\t%.2f%%\t\tpost:%.1f"%(fup*100.0,money*fup)
q= 1 - p
#q= 1 - 0.83479
fdown = kelly(1/b,q)
print "DW:\t%.2f%%\t\tpost:%.1f"%(fdown*100.0,money*fdown)


 
