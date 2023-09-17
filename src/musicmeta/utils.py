""" Music Tag utility functions """

__all__ = ["getFiles", "getFilesMusicTags"]


###############################################################################
# Return master list of files
###############################################################################
def getFiles(fileval, dirval):
    dirfiles = {}
    if isinstance(fileval, str):
        finfo = FileInfo(fileval)
        if finfo.isFile():
            dval = DirInfo(getcwd())
            dirfiles[dval] = [fileval]
        else:
            raise ValueError(f"File {fileval} is not a file!")

    if isinstance(dirval, str):
        for root, dirs, files in walk(dirval, topdown=False):
            rootDir = DirInfo(root)
            rootFiles = [FileInfo(rootDir).join(ifile) for ifile in files]
            rootFiles = [finfo for finfo in rootFiles if isinstance(finfo, FileInfo)]
            if len(rootFiles) > 0:
                dirfiles[rootDir] = rootFiles

    return dirfiles


def getFilesMusicTags(files, verbose=False):
    musicFiles = {}
    for dirval, filevals in files.items():
        dirResults = {ifile: MusicTag(ifile, verbose=verbose) for ifile in filevals}
        dirResults = {k: v.mtag for k, v in dirResults.items() if v.isMusic}
        if len(dirResults) > 0:
            musicFiles[dirval] = dirResults
    return musicFiles