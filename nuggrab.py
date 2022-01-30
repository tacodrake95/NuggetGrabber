import re
import os
import urllib.request
import sys


ranges = [1,1000]

n = len(sys.argv)
if n == 2:
    ranges[0] = int(sys.argv[1])
    ranges[1] = ranges[0]
elif n == 3:
    ranges[0] = int(sys.argv[1])
    ranges[1] = int(sys.argv[2])
elif n == 1:
    print("Using default configuration")
else:
    print("Too many arguments")
    sys.exit()

url = "https://market.x.immutable.com/assets/0x3d88c23d2d93d1f0391d2062e0189b99b0ce8dcb/%s"
pat = 'https://cdn.niftynuggets.org/nuggets/.*\"'
NoneType = type(None)


IMGURLs = []

if ranges[0] == ranges[1]:
    print("Getting nugget with ID %s" % ranges[0])
else:
    print("Looking for nuggets in range %s-%s" % (ranges[0], ranges[1]))

for i in range(ranges[0],ranges[1] + 1):
    try:
        urllib.request.urlretrieve(url%i, 'current.txt')
        toRead = open('current.txt', 'r')
        Lines = toRead.readlines()
        toRead.close()

        for line in Lines:
            m = re.search(pat,line)
            if(type(m) != NoneType):
               imgurl = m.group(0).split('"')[0]
               fn = str.split(imgurl,'/')[-1] 
               urllib.request.urlretrieve(imgurl, fn)
               print("Success for nugget #%s!" % i)
    except:
        print("Nugget #%s nonexistent or unminted" % i)
    if ranges[0] != ranges[1]:
        print(str((i - ranges[0])/(ranges[1] - ranges[0]) * 100) + "%")
        
os.remove("current.txt")