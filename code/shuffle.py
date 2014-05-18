#!/usr/bin/python
import errno
import os
import sys

_, outdir, shardname = sys.argv
files = {}

for line in sys.stdin:
    name, count = line.split(' ')
    if name not in files:
        dirname = os.path.join(outdir, name)
        try:
            os.makedirs(dirname)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        files[name] = open(os.path.join(dirname, shardname), 'w')
    files[name].write('%s %d\n' % (name, int(count)))
