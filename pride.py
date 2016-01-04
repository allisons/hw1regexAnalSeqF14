# Copyright (c) 2016 Allison Sliter
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import re
pride = "pandp.txt"
from collections import defaultdict
from functools import partial

names = defaultdict(int)

with open(pride) as f:
    s = f.read()
    print type(s)
    reg = re.compile("(?<=Mr. )[A-Z][a-z]+")
    misters = re.findall(reg, s)
    for guys in misters:
        names[guys] += 1
    

with open(pride) as f:
    s = f.read()
    reg = re.compile("(?<=Miss )[A-Z][a-z]+")
    miss = re.findall(reg, s)
    for gals in miss:
        names[gals] += 1

with open(pride) as f:
    s = f.read()
    reg = re.compile("(?<=Mrs. )[A-Z][a-z]+")
    mrs = re.findall(reg, s)
    for ladies in mrs:
        names[ladies] += 1


#for name in names:
#    print name + ":" + str(names[name])
    


