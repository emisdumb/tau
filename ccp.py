# Custom Colored Printer

import time

LOG = '\u001b[34;1mLOG\u001b[0m'
READY = '\u001b[32;1mREADY\u001b[0m'
ERROR = '\u001b[31;1mERROR\u001b[0m'

def join(value):
    string = ''
    for i in value:
        string += str(i) + ' '
    return string

def done():
    t = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(time.time()))
    print(f'\u001b[37;1m{t}\u001b[1m\u001b[38;5;208m DONE\u001b[0m')

def log(*value, sep='', end='\n'):
    t = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(time.time()))
    value = join(value)
    print(f'\u001b[37;1m{t} {LOG} {value}', sep=sep, end=end)

def ready(*value, sep='', end='\n'):
    t = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(time.time()))
    value = join(value)
    print(f'\u001b[37;1m{t} {READY} {value}', sep=sep, end=end)

def event(*value, event='EVENT', sep='', end='\n'):
    t = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(time.time()))
    EVENT = f'\u001b[35;1m{str(event)}\u001b[0m'
    value = join(value)
    print(f'\u001b[37;1m{t} {EVENT} {value}', sep=sep, end=end)

def error(*value, sep='', end='\n'):
    t = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(time.time()))
    value = join(value)
    print(f'\u001b[37;1m{t} {ERROR} {value}', sep=sep, end=end)