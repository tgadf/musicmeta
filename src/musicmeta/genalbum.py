import argparse
from musicID import MusicID
from fsUtils import mkDir, moveFile, setDir, moveDir
from fileUtils import isFile, isDir, getDirname, getDirBasics, getBaseFilename
from searchUtils import findAll, findWalk, findDirs
from os import getcwd
from musicPath import pathBasics
from time import sleep
import sys
import re
from collections import Counter

def getBestVal(vals):
    lenvals = {k: len(v) for k, v in vals.items()}
    minval  = 0
    bestval = None
    for k,v in vals.items():
        if len(v["Val"]) > minval:
            minval  = len(v["Val"])
            bestval = v
    return bestval

def stripName(trackname):
    delims = [" ", "-", ")","."]
    found  = True
    while found:
        found = False
        for delim in delims:
            if trackname.startswith(delim):
                trackname = trackname[1:]
                found = True
                break
    return trackname

def guessTrackNumber(trackname):
    retvals = {}

    pattern = "^[0-9]{2}"
    mval    = re.search(pattern, trackname)    
    if mval is not None:
        try:
            int(mval.group())
            retvals[pattern] = {"Val": mval.group(), "Rep": trackname.replace(mval.group(), "")}
        except:
            pass
                
    return retvals

def guessTitle(trackname):
    retvals = {}
    retvals["Best"] = {"Val": trackname, "Rep": ""}
    return retvals

    
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
    
def p(vals):
    vals = [fix(x) for x in vals]
    print("{0: <4}{1: <8}{2: <9}{3: <25}{4: <35}{5: <60}{6: <70}{7: <6}".format(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6], vals[7]))

def header():
    p(["##", "Disc", "Track", "AlbumArtist", "Artist", "Album", "Title", "Size"])
    p(["--", "----", "-----", "-----------", "------", "-----", "-----", "----"])

        
def main(args):
    if args.dir is None:
        args.dir  = getcwd()
    
        #retval = testAlbum(albumDir, artistDir, files=filevals)
            
    albumDirs  = findDirs(args.dir)
    for albumDir in albumDirs:
        if getDirBasics(albumDir)[-1] != "Album":
            continue
        pb    = pathBasics(albumDir=albumDir)
        files = pb.getFiles()
        print("\n")
        print("="*60)
        print("===",albumDir,"===")
        print("="*60)
        for subalbumDir, filevals in files.items():
            #print(subalbumDir,len(filevals))
            
            albumName = Counter()
            for ifile in filevals:
                results = MusicID(ifile, debug=args.debug)
                if results.skip is True:
                    continue
                tags = results.getInfo()
                albumVal = tags["Album"][0]
                albumName[albumVal] += 1
             
            if len(albumName) != 1:
                continue
            albumName = albumName.most_common(1)[0][0]
            albumName = albumName.replace("/", " ")
            srcDir = subalbumDir
            dstDir = setDir(albumDir, albumName)
            if isDir(dstDir):
                continue            

            #print("Moving {0}  ==> {1}\n\n".format(srcDir, dstDir))
            print("\nmv \"{0}\" \"{1}\"\n".format(srcDir, dstDir))
            #sleep(1)
            #moveDir(srcDir, dstDir)
            #sleep(1)
            #print(albumName)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Music ID Tagger')
    parser.add_argument('-showpath', '-sp', action="store_true", dest="showpath", default=False)
    parser.add_argument('-dir', '-d', action="store", dest="dir")
    parser.add_argument('-debug', action="store_true", default=False)




    args = parser.parse_args()
    main(args)

