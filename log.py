import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# 提取log
tag1=r'Per MPI rank memory allocation (min/avg/max)'
tag2=r'Loop time of'
strx='Step'
stry='TotEng'
path=r"log.anneal"

f=open(path,'r',encoding='utf-8')
line=f.readline()
f.seek(0,0)
data0=[]
flag = True
while line:
    line=f.readline()
    if tag1 in line:
        if flag:
            line1 = f.readline()
            print(line1)
            data0.append(re.split('\s+', line1.strip()))
            while line1:
                line1 = f.readline()
                if not tag2 in line1:
                    data0.append(re.split('\s+', line1.strip()))
                else:
                    line1 = None
            flag = False
        else:
            line2 = f.readline()
            while line2:
                line2 = f.readline()
                if not tag2 in line2:
                    data0.append(re.split('\s+', line2.strip()))
                else:
                    line2 = None

data=np.array(data0,dtype='object')
print(data)
f.close()

# 画图
colx=list(data[0,:]).index(strx)
coly=list(data[0,:]).index(stry)
x0=[float(xval) for xval in list(data[1:,colx])]
y0=[float(yval) for yval in list(data[1:,coly])]
lb=strx+'-'+stry
plt.title(lb)
plt.plot(x0,y0)
#plt.xticks(ticks=np.arange(0,11e4,1e4))
# labels=['0.01', '0.1', '1', '10', '100', '1000'])
# plt.yticks(ticks=np.arange(0,max(y0)+50,50))
plt.gca().yaxis.set_major_locator( MaxNLocator(8) )
# labels=['0.1', '1', '10', '100', '1000', '10000'])
plt.ticklabel_format(style='sci',scilimits=(0,0),axis='both')
plt.xlabel(strx)
plt.ylabel(stry)
#plt.xlim([0, 102e3])
#plt.ylim([0, 36e-3])
# plt.legend(frameon=False)
plt.show()