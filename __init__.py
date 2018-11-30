import os, sys


def getWin32():
    """
    import win32, install via pip3 if necessary
    """
    try:
        import win32
    except:
        runner = subprocess.run(
            [
                os.path.dirname(  os.path.abspath(sys.executable)  )
                + os.sep + "Scripts" + os.sep + "pip3.exe"
                ,
                'install', '-U --user', 'pywin32'
            ],
            capture_output=True,
        )
        import win32
        print("imported win32")

    return win32

def printDicts( objs ):
    for i,obj in enumerate(objs):
        print( "Object" + str(i).zfill(5) + ":" )
        printDict( obj )

def printDict( obj ):
    for k,v in obj.__dict__.items():
        print( "    " + k + "   :   " + v )

def getScriptDirAndChdir( printInfo = False ):
    """ Gets an object containing info on the running script
    and its interpreter/executable.
    """
    import os, sys
    d = type('Duck', (), {})()
    sep = d.sep = os.sep
    d.absPathName = os.path.abspath( sys.argv[0] )
    d.absDir = os.path.dirname( d.absPathName )
    d.base = os.path.basename( d.absPathName )
    os.chdir( d.absDir )
    d.cwd = os.getcwd()
    d.sysExeAbsDir = os.path.dirname(
        os.path.abspath(sys.executable)
    )
    d.pipAbsPathName = (
        d.sysExeAbsDir + sep
        + "Scripts" + sep + "pip3.exe"
    )
    if printInfo == True:
        printDict( d )
    return d


    
    
    
    
# print( "press any key..." )
# print( targetFile )
# input()

