#!/usr/bin/env python

'makeTextFile.py -- create text file'

import os

# get filename
while True:
    fname = raw_input('Enter file name: ')
    if os.path.exists(fname):
        try:
            delornot=raw_input('file exists now,delete or not?(Y|N)')
            if delornot == 'Y':
                os.unlink(fname)
            elif delornot == 'N':
                raise IOError
            else:
                print 'Try Again!'
                continue
        except IOError:
            raise IOError,"*** ERROR: '%s' already exists And delete failed!" % fname

    break

# get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

# loop until user terminates input
while True:
    entry = raw_input('Something More?> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with NEWLINE line terminator
fobj = open(fname, 'w')
fobj.write(os.linesep.join(all))
fobj.close()
print 'DONE!'
