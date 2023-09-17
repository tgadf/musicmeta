""" Command line code to get/set music metadata """

__all__ = ["mid"]

import argparse
from .tagutils import getWalkMusicFiles, getWalkMusicTags, showWalkMusicTags


###############################################################################
# Master function to be called on the command line
###############################################################################
def mid():
    args = getArgs()

    walkFiles = getWalkMusicFiles(args.dir)
    numDirs = len(walkFiles)
    numFiles = sum(len(x) for x in walkFiles.values())
    print(f"Found {numDirs} Directories with {numFiles} Files")

    #######################################################
    # Get tag info for all music files
    #######################################################
    print("  Finding Music Files ... ", end="")
    musicFiles = getWalkMusicTags(walkFiles)
    numMusicDirs = len(musicFiles)
    numMusicFiles = sum(len(x) for x in musicFiles.values())
    print(f"Done. Found {numMusicDirs} Directories With {numMusicFiles} Music Files")

    #######################################################
    # Get music file tags
    #######################################################
    if args.show is True:
        showWalkMusicTags(musicFiles)

    #######################################################
    # Set music file tags
    #######################################################
    argTagMap = {}
    argTagMap["artist"] = "Artist"
    argTagMap["album"] = "Album"
    argTagMap["albumartist"] = "AlbumArtist"
    argTagMap["title"] = "Title"
    argTagMap["discno"] = "DiscNumber"
    argTagMap["trackno"] = "TrackNumber"

    delta = False
    for arg, tag in argTagMap.items():
        if hasattr(args, arg) is False or getattr(args, arg) is None:
            continue
        delta = True
        tagValue = getattr(args, arg)
        print(f"  Setting Music Tag {tag} To {tagValue} ... ")
        for dirval, dirResults in musicFiles.items():
            for cntr, (ifile, mtag) in enumerate(dirResults.items()):
                mtag.setTag(tag, tagValue)
        print("Done")
        
    if delta is True:
        showWalkMusicTags(getWalkMusicTags(walkFiles))


###############################################################################
# Argument Parser
###############################################################################
def getArgs():
    parser = argparse.ArgumentParser(description='Music ID Tagger')
    parser.add_argument('-artist', '-art', "-a", action="store", dest="artist")
    parser.add_argument('-album', '-alb', action="store", dest="album")
    parser.add_argument('-albumartist', '-aa', action="store", dest="albumartist")
    parser.add_argument('-title', action="store", dest="title")
    parser.add_argument('-trackno', '-track', action="store", dest="trackno")
    parser.add_argument('-discno', '-disc', action="store", dest="discno")
    parser.add_argument('-show', '-s', action="store_true", default=True)
    parser.add_argument('-file', '-f', action="store", dest="file")
    parser.add_argument('-dir', '-d', action="store", dest="dir")
    parser.add_argument('-debug', action="store_true", default=False)
    args = parser.parse_args()

    if isinstance(args.discno, int) is True:
        args.discno = str(args.discno)
    if isinstance(args.trackno, int) is True:
        args.discno = str(args.trackno)
        
    if args.debug is True:
        argVars = vars(args)
        keyLen = max([len(key) for key in argVars.keys()])
        print("mid Arguments")
        for key, val in argVars.items():
            if key in ["show", "debug"]:
                continue
            print(f"  {key: <{keyLen+1}}: {val}")
        print("")

    return args
