## Use windows to launch matching shortcut
## .py to .lnk    in same dir    for python 3.7
import os, sys
workingDir = os.path.dirname( os.path.abspath(sys.argv[0])   )
os.chdir( workingDir )
targetFile = ".".join(sys.argv[0].split(".")[0:-1]) + ".lnk"
os.startfile(
    targetFile
)
