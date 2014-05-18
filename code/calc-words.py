#!/usr/bin/python
import sys
import re

def getNick(nick):
    nick = nick.strip('_-^').lower()
    # Some special cases, some may be incorrect
    for name in ('outlaw', 'kosma', 'sad', 'morf', 'ciuciu', 'ahes', 'argonn'):
        if name in nick:
            return name
    if 'gruch' in nick:
        return 'grucha'
    # Drop suffixes
    for ch in '^|`':
        if not nick.startswith(ch):
            nick = nick.split(ch, 1)[0]
    for suffix in ('off', 'away', 'aw'):
        if nick.endswith('[%s]' % suffix):
            nick = nick[:-(len(suffix) + 2)]
        elif nick.endswith('_' + suffix):
            nick = nick[:-(len(suffix) + 1)]
    if nick.startswith('|') and nick.endswith('|'):
        nick = nick[1:-1]
    return nick or '_'

def getWords(line):
    m = re.search(r'^\[\d\d:\d\d\] <([^>]*)> (.*)$', line)
    if not m:
        return '_', 0
    else:
        return getNick(m.group(1)), len(re.split(r'\s+', m.group(2).strip()))

for nick, count in map(getWords, sys.stdin):
    print nick, count
