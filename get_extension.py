#!/anaconda3/bin/python

filename1 = 'myfile.txt'
filename2 = 'myfile'
print(filename1)
print(filename2)

def get_extension1(filename):
    return(filename.split(".")[-1])

def get_extension2(filename):
    import os.path
    return(os.path.splitext(filename)[1])

def get_extension3(filename):
    return filename[filename.rfind('.'):][1:]

print(get_extension1(filename1))
print(get_extension1(filename2))
print(get_extension2(filename1))
print(get_extension2(filename2))
print(get_extension3(filename1))
print(get_extension3(filename2))