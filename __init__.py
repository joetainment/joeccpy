import os, sys, subprocess, time, traceback

def run( *args, **kargs ):
    subprocess.run( *args, **kargs )

def sleep( *args, **kargs ):
    time.sleep( *args, **kargs ) 
    
def traceback():
    traceback.format_exc()

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

        
def chdirToSelf(**kargs):
    return getScriptDirAndChdir(**kargs)
        
def getScriptDirAndChdir( printInfo = False ):
    """ Gets an object containing info on the running script
    and its interpreter/executable.
    """
    import os, sys
    d = ScriptArgv0Info()
    
    os.chdir( d.absDir )
    d.cwd = os.getcwd()

    if printInfo == True:
        printDict( d )
    return d

def substExt( newExt ):
    return
    
class ScriptArgv0Info(object):
    def __init__(self):
        sep = self.sep = os.sep
        self.absPathName = os.path.abspath( sys.argv[0] )
        self.absDir = os.path.dirname( self.absPathName )
        self.base = os.path.basename( self.absPathName )
        spl = self.base.split(".")
        self.baseNoExt = ".".join( spl[0:-1] )
        self.ext = spl[-1]
        self.sysExeAbsDir = os.path.dirname(
            os.path.abspath(sys.executable)
        )
        self.pipAbsPathName = (
            self.sysExeAbsDir + sep
            + "Scripts" + sep + "pip3.exe"
        )

    def substExt(self, newExt=None):
        assert newExt != None  ## later can add logic for defaults
        return self.baseNoExt + '.' + newExt
        
    
