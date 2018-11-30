## joeccpy example
## Use windows to launch matching shortcut
## .py to .lnk    in same dir    for python 3.7
#############
##hack for example only
import os, sys
sys.path.insert(  0, os.path.abspath('..' + os.sep + '..')  )
######################





## the actual code a joeccpy module user would have to use is:
import os, sys, joeccpy
selfInfo = joeccpy.chdirToSelf() ## gets back lots of info
## Now we're in our scripts folder, with useful info about our script
os.startfile(    selfInfo.substExt("lnk")    )

