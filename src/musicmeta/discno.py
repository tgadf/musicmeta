""" Command line code to analyze disc number """

__all__ = ["discno"]

from utils import FileInfo, DirInfo
import argparse
import re
from os import walk
from .tagutils import getDirMusicTags, showDirMusicTags


###############################################################################
# Master function to be called on the command line
###############################################################################
def discno():
    args = getArgs()

    assert isinstance(args.dir, str), f'args.dir [{args.dir}] is not a str'
    common = re.compile(r'^(Disc|CD)[ ]{0,1}(\d+)')
    
    matches = {}
    for root, dirs, files in walk(args.dir, topdown=False):
        if len(dirs) == 0:
            continue
        dirResults = {dirval: re.search(common, dirval) for dirval in dirs}
        dirResults = {k: v for k, v in dirResults.items() if isinstance(v, re.Match)}
        if len(dirResults) == 0:
            continue
        rootDir = DirInfo(root)
        for dirval, dirResult in dirResults.items():
            dinfo = rootDir.join(dirval)
            dinfo = DirInfo(dinfo.str) if isinstance(dinfo, FileInfo) else dinfo
            matches[dinfo] = dirResult

    print(f"Done. Found {len(matches)} Directories With Matching Disc Syntax")
            
    for dinfo, dirResult in matches.items():
        discNumber = dirResult.groups()[-1]
        assert isinstance(discNumber, str), f"Bad match: {dirResult}"
        assert discNumber.isdigit(), f"DiscNumber [{discNumber} / {dinfo}] is not a digit"
        dirTags = getDirMusicTags(dinfo)
        for cntr, (ifile, mtag) in enumerate(dirTags.items()):
            mtag.setTag('DiscNumber', discNumber)
                
    for dinfo, dirResult in matches.items():
        discNumber = dirResult.groups()[-1]
        showDirMusicTags(getDirMusicTags(dinfo), dinfo)
            

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
