import subprocess
import sys

def getSys(w, l):

    getSystem = sys.platform
    if ('win' in getSystem):
        w = 'cls'
        return subprocess.run(w)

    elif ('linux' in getSystem):
        l = 'clear'
        return subprocess.run(l)

    else:
        print('Sistema não identificado')
        sys.exit()
