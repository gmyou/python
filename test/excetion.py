import traceback
try:
    1/0
except:
    print(traceback.format_exc())

import sys
def printException():
    message = []
    for e in sys.exc_info():
        message.append(str(e))
    message = '\n'.join(message)
    print message
    return message

try:
    raise "Error"
except:
    printException()