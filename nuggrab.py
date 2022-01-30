import re
import os
import urllib.request
import sys

n = len(sys.argv)

ranges = [1,1000]

for i in range(1,n):
    ranges[i-1] = int(sys.argv[i])

url = "https://market.x.immutable.com/assets/0x3d88c23d2d93d1f0391d2062e0189b99b0ce8dcb/%s"
pat = 'https://cdn.niftynuggets.org/nuggets/.*\"'
NoneType = type(None)


IMGURLs = []

print("Looking for nuggets from range %s to %s" % (ranges[0], ranges[1]))

for i in range(ranges[0],ranges[1]):
    print(str(i/ranges[1]) + "%")
    try:
        urllib.request.urlretrieve(url%i, 'current.txt')
        toRead = open('current.txt', 'r')
        Lines = toRead.readlines()
        toRead.close()
        os.remove("current.txt")
        for line in Lines:
            m = re.search(pat,line)
            if(type(m) != NoneType):
               imgurl = m.group(0).split('"')[0]
               fn = str.split(imgurl,'/')[-1] 
               urllib.request.urlretrieve(imgurl, fn)
               print("Success for nugget #%s!" % i)
    except:
        print("Nugget #%s nonexistent or unminted" % i)