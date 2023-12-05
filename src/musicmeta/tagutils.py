""" Music Tag utility functions """

__all__ = ["getWalkMusicFiles", "getDirMusicFiles", "getMusicFiles",
           "getMusicTags", "getDirMusicTags", "getWalkMusicTags",
           "showDirMusicTags", "showWalkMusicTags"]

from utils import FileInfo, DirInfo
from os import walk
from .musicid import MusicTag
from .mutag import MusicTagInfo
from .muformat import MusicFileFormat


###############################################################################
# Useful functions for file I/O
###############################################################################
def getMusicFiles(files: list) -> 'list':
    assert isinstance(files, list), f"files [{type(files)}] is not a list"
    mufiles = [MusicFileFormat(ifile) for ifile in files]
    retval = [mff.finfo for mff in mufiles if mff.isMusic()]
    return retval
    

def getDirMusicFiles(dinfo: DirInfo) -> 'list':
    assert isinstance(dinfo, DirInfo), f"dinfo {type(dinfo)} is not a DirInfo"
    files = [FileInfo(dinfo).join(ifile) for ifile in dinfo.getFiles()]
    retval = getMusicFiles(files)
    return retval
    
    
def getWalkMusicFiles(dirval: str) -> 'dict':
    dirval = dirval.str if isinstance(dirval, DirInfo) else dirval
    assert isinstance(dirval, str), f"dirval arg {dirval} must be a str"
    
    walkFiles = {}
    for root, dirs, files in walk(dirval, topdown=True):
        rootDir = DirInfo(root)
        rootFiles = [FileInfo(rootDir).join(ifile) for ifile in files]
        mufiles = getMusicFiles(rootFiles)
        if len(mufiles) > 0:
            walkFiles[rootDir.path] = mufiles

    return walkFiles


###############################################################################
# Useful functions for MusicTag I/O
###############################################################################
def getMusicTags(files: list, checkType: bool = False) -> 'dict':
    assert isinstance(files, list), "files [{type(files)}] must be a list"
    mufiles = getMusicFiles(files) if checkType is True else files
    retval = {finfo.path: MusicTag(finfo).mtag for finfo in mufiles}
    assert all(retval.values()), f"Found a non MusicTag: {retval}"
    return retval


def getDirMusicTags(dirval) -> 'dict':
    dinfo = DirInfo(dirval) if isinstance(dirval, str) else dirval
    retval = getMusicTags(getDirMusicFiles(dinfo))
    return retval
    

def getWalkMusicTags(walkFiles: dict) -> 'dict':
    assert isinstance(walkFiles, dict), f"files args [{walkFiles}] must be a dict"
    retval = {dinfo: getMusicTags(mufiles) for dinfo, mufiles in walkFiles.items()}
    return retval


###############################################################################
# CL output
###############################################################################
def showDirMusicTags(mutags: dict, dirval=None):
    assert isinstance(mutags, dict), "mutags [{type(mutags)}] must be a dict"
    if isinstance(dirval, (str, DirInfo)):
        header(dirval)
    for cntr, (ifile, mtag) in enumerate(mutags.items()):
        showTags(cntr, MusicTagInfo(mtag).get())
       
        
def showWalkMusicTags(walkResults):
    assert isinstance(walkResults, dict), "walkResults [{type(walkResults)}] must be a dict"
    for dirval, mtags in walkResults.items():
        showDirMusicTags(mtags, dirval)
              
            
def showTags(num, tagData):
    assert isinstance(tagData, dict), "TagData is not a dict"
    tags = ["DiscNumber", "TrackNumber", "AlbumArtist",
            "Artist", "Album", "Title", "Size"]
    showData = [num] + [tagData[tag] for tag in tags]
    printTag(showData)


def printTag(vals):
    assert isinstance(vals, list) and len(vals) == 8, f"Vals [{vals}] is bad"

    def fix(val):
        if val is None:
            return ""
        if isinstance(val, list):
            if len(val) > 0:
                return str(val[0])
            else:
                return str(val)
        if isinstance(val, tuple):
            return str(val)
        return val
    print(f"{fix(vals[0]): <4}", end="")
    print(f"{fix(vals[1]): <8}", end="")
    print(f"{fix(vals[2]): <9}", end="")
    print(f"{fix(vals[3]): <25}", end="")
    print(f"{fix(vals[4]): <35}", end="")
    print(f"{fix(vals[5]): <60}", end="")
    print(f"{fix(vals[6]): <70}", end="")
    print(f"{fix(vals[7]): <6}")


def header(dirval):
    print(f"\nDirectory: {dirval}")
    printTag(["##", "Disc", "Track", "AlbumArtist", "Artist", "Album", "Title", "Size"])
    printTag(["--", "----", "-----", "-----------", "------", "-----", "-----", "----"])