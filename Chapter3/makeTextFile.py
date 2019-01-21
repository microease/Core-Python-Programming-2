import os

ls = os.linesep
# get filename
while True:
    if os.path.exists(fname):
        print("Error: %s already exists" % fname)
    else:
        break
