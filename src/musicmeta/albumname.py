""" Command line code to analyze disc number """

__all__ = ["albumname"]

from utils import DirInfo
import argparse
from .tagutils import getWalkMusicFiles, getWalkMusicTags, showWalkMusicTags


###############################################################################
# Master function to be called on the command line
###############################################################################
def albumname():
    args = getArgs()

    assert isinstance(args.dir, str), f'args.dir [{args.dir}] is not a str'
    dirAlbumData = {}
    for dirval in DirInfo(args.dir).getDirs():
        dinfo = DirInfo(dirval)
        dname = dinfo.name
        walkFiles = getWalkMusicFiles(dinfo)
        if len(walkFiles) > 0:
            dirAlbumData[dinfo] = [dname, walkFiles]
    print(f"Done. Found {len(dirAlbumData)} Album Directories")
            
    for dinfo, (dname, walkFiles) in dirAlbumData.items():
        print(dname, '\t', len(walkFiles))
        mutags = getWalkMusicTags(walkFiles)
        for subdinfo, submutags in mutags.items():
            print(submutags)
            for cntr, (finfo, mtag) in enumerate(submutags.items()):
                print('mtag', mtag)
                mtag.setTag('Album', dname)
                
    for dinfo, (dname, walkFiles) in dirAlbumData.items():
        showWalkMusicTags(getWalkMusicTags(walkFiles))
            

###############################################################################
# Argument Parser
###############################################################################
def getArgs():
    parser = argparse.ArgumentParser(description='Music ID Tagger')
    parser.add_argument('-dir', '-d', action="store", dest="dir")
    parser.add_argument('-debug', action="store_true", default=False)
    args = parser.parse_args()

    if args.debug is True:
        argVars = vars(args)
        keyLen = max([len(key) for key in argVars.keys()])
        print("mid Arguments")
        for key, val in argVars.items():
            if key in ["debug"]:
                continue
            print(f"  {key: <{keyLen+1}}: {val}")
        print("")

    return args
