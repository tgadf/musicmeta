from fileUtils import getBaseFilename, getDirname, getExt, getBasename, getDirBasics
from fsUtils import setDir, isFile
from searchUtils import findWalk

class pbClass:
    def __init__(self, pbClass, pbArtist, pbAlbum, pbDisc, pbFile, pbExt):
        self.pbClass  = pbClass
        self.pbArtist = pbArtist
        self.pbAlbum  = pbAlbum
        self.pbDisc   = pbDisc
        self.pbFile   = pbFile
        self.pbExt    = pbExt
        
    def getDict(self):
        return self.__dict__



class pathBasics():
    def __init__(self, classDir=None, artistDir=None, albumDir=None, debug=False):
        self.debug = debug
        
        if not any([classDir, artistDir, albumDir]):
            raise ValueError("Must provide classDir, artistDir, or albumDir")
                
        self.mClass  = None
        self.mArtist = None
        self.mArtist = None
        self.mAlbum  = None
        self.mDisc   = None
        self.mFile   = None
        self.musicDir = None

        self.known = None
        if artistDir is not None:
            self.musicDir     = artistDir
            self.known        = "Artist"
            self.mArtist      = getDirBasics(artistDir)[-1]
            if debug:
                print("  Artist Path with {0} --> {1}".format(self.known, self.mArtist))
        elif albumDir is not None:
            self.musicDir     = albumDir
            self.known        = "Album"
            self.mAlbum       = getDirBasics(albumDir)[-1]
            self.mArtist      = getDirBasics(albumDir)[-2]
            if debug:
                print("  Album Path with {0} --> {1}".format(self.known, self.mAlbum))
        elif classDir is not None:
            self.musicDir     = classDir
            self.known        = "Class"
            self.mClass       = getDirBasics(classDir)[-1]
            if debug:
                print("  Class Path with {0} --> {1}".format(self.known, self.mClass))


    def getFiles(self):
        if self.musicDir is not None:
            files = findWalk(self.musicDir)
        else:
            raise ValueError("No files to find!!")
        return files
    
        
    def stripBase(self, ifile, errors='ignore'):
        mfile = ifile.split(self.musicDir)[-1]
        if mfile.startswith("/"):
            mfile = mfile[1:]
        self.mFile = mfile
        return
    
        
    def getPaths(self, ifile, errors='ignore'):
        if self.debug:
            print("Name:   {0}".format(ifile))
            print("isFile: {0}".format(isFile(ifile)))
        mfile = ifile
        self.stripBase(ifile)

        filename = None
        ext      = None

        
        
        ##
        ## Test for Album/File Structure
        ##
        if self.known == "Artist":
            dirval,fileval = getDirname(self.mFile),getBasename(self.mFile)
            nextDirVal,nextFileVal = getDirname(dirval),getBasename(dirval)

            ## Get File Info
            filename = fileval
            ext      = getExt(fileval)

            if len(nextDirVal) == 0 and nextFileVal == dirval:
                self.mAlbum  = dirval
            else:
                self.mAlbum  = dirval
                self.mDisc   = nextDirVal
                
                
        ##
        ## Test for Artist/Album/File Structure
        ##
        if self.known == "Class":
            dirval,fileval = getDirname(self.mFile),getBasename(self.mFile)
            nextDirval,nextFileval = getDirname(dirval),getBasename(dirval)
            nextNextDirval,nextNextFileval = getDirname(nextDirval),getBasename(nextDirval)

            
            ## Get File Info
            filename = fileval
            ext      = getExt(fileval)
            
            
            #ifile = "/Volumes/Music/Matched/test/AC-DC/Let There Be Rock - Live In Paris/CD1/01 -Live Wire.mp3"
            #{'pbClass': 'test', 'pbArtist': 'AC-DC/Let There Be Rock - Live In Paris', 'pbAlbum': 'CD1', 'pbDisc': None, 'pbFile': '01 -Live Wire.mp3', 'pbExt': '.mp3'}

            if len(nextNextDirval) == 0 and nextNextFileval == nextDirval:
                self.mArtist = nextDirval
                self.mAlbum  = nextFileval
            else:
                self.mArtist = nextNextDirval
                self.mAlbum  = nextNextFileval
                self.mDisc   = nextFileval
                
                
        ##
        ## Test for File Structure
        ##
        if self.known == "Album":
            dirval,fileval = getDirname(self.mFile),getBasename(self.mFile)
            nextDirVal,nextFileVal = getDirname(dirval),getBasename(dirval)

            ## Get File Info
            filename = fileval
            ext      = getExt(fileval)

            if len(dirval) == 0:
                pass
            else:
                self.mDisc   = dirval
                
                   
        return pbClass(self.mClass, self.mArtist, self.mAlbum, self.mDisc, filename, ext)