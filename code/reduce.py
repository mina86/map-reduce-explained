#!/usr/bin/python
import sys

def aggregate(state, line):
    name, count = line.strip().split(' ')
    state[name] = state.get(name, 0) + int(count)
    return state

for nick, count in reduce(aggregate, sys.stdin, {}).iteritems():
    print nick, count
