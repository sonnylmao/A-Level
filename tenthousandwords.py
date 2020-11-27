import time 
import enchant 
import numpy as np

start_time = time.time()
d = enchant.Dict("en_US")

def interlock(a,b):
    n = 0
    s = min(map(len,[a,b]))
    xf = ''
    yf = ''
    for x in range(s):
        xf += a[x]+b[x]
        yf += b[x]+a[x]
    if len(yf) == 0:
        pass
    elif d.check(yf) == True:
        print(yf)
    if len(xf) == 0:
        pass
    elif d.check(xf) == True:
        print(xf)

with open('10000words.txt') as f:
    content = f.readlines()
content = np.array([x.strip() for x in content])

count = 1
for x in content:
    for m in range(count,len(content)):
        interlock(x,content[m])
    count += 1

#runtime
print("%s seconds" % (time.time() - start_time))
