#!/anaconda3/bin/python

import os
filenames = os.listdir('mydir')
print(filenames)
f = open(filenames[0])