""" Command line code to rename music directories """

__all__ = ["fixdir"]

from utils import DirInfo, FileInfo
import argparse
    

###############################################################################
# 'sep' Arg Code
###############################################################################
def findDirsWithSep(dinfo, sep, left=False):
    assert isinstance(sep, str), f"sep arg [{sep}] must be a str"
    newDirs = []
    for subdinfo in dinfo.getDirs():
        splitVals = subdinfo.name.split(sep)
        if len(splitVals) == 1:
            continue
        if left is True:
            dstDir = dinfo.join(splitVals[0])
        else:
            dstDir = dinfo.join(sep.join(splitVals[1:]))
        newDirs.append([subdinfo, dstDir])
    return newDirs


###############################################################################
# 'rm' Arg Code
###############################################################################
def findDirsWithRemove(dinfo, remove):
    assert isinstance(remove, str), f"rm arg [{remove}] must be a str"
    newDirs = []
    for subdinfo in dinfo.getDirs():
        if subdinfo.name.count(remove) == 0:
            continue
        dstDir = dinfo.join(subdinfo.name.replace(remove, "").strip())
        newDirs.append([subdinfo, dstDir])
    return newDirs


###############################################################################
# 'add' Arg Code
###############################################################################
def findDirsWithAdd(dinfo, add):
    assert isinstance(add, str), f"sep arg [{add}] must be a str"
    add = add if add.startswith("(") else f"({add}"
    add = add if add.endswith(")") else f"{add})"
    
    newDirs = []
    for subdinfo in dinfo.getDirs():
        dstDir = dinfo.join(f"{subdinfo.name} {add}")
        newDirs.append([subdinfo, dstDir])
    return newDirs


###############################################################################
# Renaming Directory Code
###############################################################################
def renameDirs(newDirs, debug=False):
    assert isinstance(newDirs, list), f"newDirs ({newDirs}) must be a list"
    for srcDir, dstDir in newDirs:
        assert srcDir.exists() is True, f"SrcDir {srcDir} does not exist!"
        dstDir = DirInfo(dstDir.str) if isinstance(dstDir, FileInfo) else dstDir
        assert dstDir.exists() is False, f"DstDir {dstDir} already exists!"
        srcDir.mvDir(dstDir)

        
###############################################################################
# Master function to be called on the command line
###############################################################################
def fixdir():
    args = getArgs()
    
    #######################################################
    # If calling 'sep', then find directories
    #######################################################
    if isinstance(args.sep, str):
        dinfo = DirInfo(args.dir)
        newDirs = findDirsWithSep(dinfo, args.sep, left=args.left)
        print(f">>> Found {len(newDirs)} To Rename With Sep=\'{args.sep}\' <<<")
        renameDirs(newDirs, args.debug)
        
    #######################################################
    # If calling 'rm', then find directories
    #######################################################
    if isinstance(args.remove, str):
        dinfo = DirInfo(args.dir)
        newDirs = findDirsWithRemove(dinfo, args.remove)
        print(f">>> Found {len(newDirs)} To Rename With Remove=\'{args.remove}\' <<<")
        renameDirs(newDirs, args.debug)
        
    #######################################################
    # If calling 'add', then find directories
    #######################################################
    if isinstance(args.add, str):
        dinfo = DirInfo(args.dir)
        newDirs = findDirsWithAdd(dinfo, args.add)
        print(f">>> Found {len(newDirs)} To Rename With Add=\'{args.add}\' <<<")
        renameDirs(newDirs, args.debug)
            

###############################################################################
# Argument Parser
###############################################################################
def getArgs():
    parser = argparse.ArgumentParser(description='Music ID Tagger')
    parser.add_argument('-dir', '-d', action="store", dest="dir")
    parser.add_argument('-files', '-f', action="store", dest="files", default=None)
    parser.add_argument('-sep', action="store", dest="sep", default=None)
    parser.add_argument('-rm', action="store", dest="remove", default=None)
    parser.add_argument('-add', action="store", dest="add", default=None)
    parser.add_argument('-replace', action="store", dest="replace", default=None)
    parser.add_argument('-left', action="store_true", default=False)
    parser.add_argument('-debug', action="store_true", default=False)
    args = parser.parse_args()

    if args.debug is True:
        print(args)

    return args
