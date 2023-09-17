import argparse
from musicID import MusicID
from fsUtils import mkDir, moveFile, setDir, moveDir, removeDir, setFile
from fileUtils import isFile, isDir, getDirname, getDirBasics, getBaseFilename, getFileBasics, getBasename
from searchUtils import findAll, findWalk, findDirs
from os import getcwd
from musicPath import pathBasics
from time import sleep
import sys
import re



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

    return args

def skipDirs():
    return ["Random", "Complete", "Todo", "Multi", "Title"]

    #mtest -artist -force Album -usetag
    

def testMix(val):
    retval  = False
    
    patterns = [" Vs ", " vs ", " Vs. "]
    for pattern in patterns:
        retvals = re.findall(pattern, val)
        retval  = retval or len(retvals) > 0
    
    return retval
    

def testCD(val):
    retval  = False
    
    pattern = "CD[1-9]"
    retvals = re.findall(pattern, val)
    retval  = retval or len(retvals) > 0
    
    pattern = "CD [1-9]"
    retvals = re.findall(pattern, val)
    retval  = retval or len(retvals) > 0
    
    pattern = "Cd [1-9]"
    retvals = re.findall(pattern, val)
    retval  = retval or len(retvals) > 0
    
    pattern = "Cd[1-9]"
    retvals = re.findall(pattern, val)
    retval  = retval or len(retvals) > 0
    
    return retval

def testDisc(val):
    retval  = False
    
    pattern = "Disc[1-9]"
    retvals = re.findall(pattern, val)
    retval  = retval or len(retvals) > 0
    
    pattern = "Disc [1-9]"
    retvals = re.findall(pattern, val)
    retval  = retval or len(retvals) > 0
    
    pattern = "disc[1-9]"
    retvals = re.findall(pattern, val)
    retval  = retval or len(retvals) > 0
    
    pattern = "disc [1-9]"
    retvals = re.findall(pattern, val)
    retval  = retval or len(retvals) > 0
    
    return retval

    
    

def testArtist(artistDir):
    artistName = getDirBasics(artistDir)[-1]
    if artistName in skipDirs():
        return None
    
    
def testAlbum(albumDir, artistDir, files):
    
    retval = {"Track": False, "Album": False, "Title": False, "Multi": False, "Skip": False, "Extra": False, "Mix": False}
    
    artistName = getDirBasics(artistDir)[-1]
    if artistName in skipDirs():
        retval["Skip"] = True
    
    #print("artistDir",artistDir)
    #print("albumDir",albumDir)
    #print("artistName",artistName)

    albumName = albumDir.replace(artistDir, "")[1:]
    if "/" in albumName:
        retval["Extra"] = True
    albumDirs = albumName.split("/")
    if albumDirs[0] in skipDirs():
        retval["Skip"] = True        
    if albumName in skipDirs():
        retval["Skip"] = True
    
    #print("albumName",albumName)

    j = 0
    tags = {}
    
    print("\t-----> Album Info: {0} / {1} \t ==> {2} Songs".format(artistName, albumName, len(files)))
    if retval["Extra"] is True:
        return retval
    if retval["Skip"] is True:
        return retval


    
    ifiles = []
    for jf, ifile in enumerate(files):
        results = MusicID(ifile, debug=args.debug)
        if results.skip is True:
            continue
        tags[j] = results.getInfo()
        ifiles.append(ifile)
        #pbcs[j] = pb.getPaths(ifile).getDict()
        j += 1
    nfiles = j


    ## Track Tests
    testTrackNo = True
    trackCheckSum = sum(range(1,nfiles+1))
    trackTrackSum = 0

    ## Album Tests
    testAlbum   = testCD(albumName) or testDisc(albumName)
    retval["Multi"] = testAlbum
    
    retval["Mix"] = testMix(albumName)

    ## Title Tests
    testTitle   = True
    for j in range(nfiles):
        ifile = ifiles[j]
        tag = tags[j]
        #pbc = pbcs[j]

        ###############################################################################################
        ## Track Number Tests
        ###############################################################################################
        trkTag = tag.get("TrackNo")
        if trkTag is None:
            print("Track Number Error ==> [{0}]".format("No TrackNo Tag"))      
            retval["Track"] = True
            break          


        try:
            trackNo = trkTag[0]
        except:
            print("Track Number Error ==> [{0}]".format("No Value"))                    
            trackNo = ""
        if len(trackNo) == 0:
            retval["Track"] = True
            break

        trackNumberValue = None
        try:
            trackNumberValue = int(trackNo)
        except:
            try:
                trackVals = [int(x) for x in trackNo.split("/")]
                trackNumberValue = trackVals[0]
            except:
                print("Track Number Error ==> [{0}]".format(trackNo))
        try:
            trackTrackSum += trackNumberValue
        except:
            pass



        ###############################################################################################
        ## Title Number Tests
        ###############################################################################################
        titleTag = tag.get("Title")
        if titleTag is None:
            print("Title Error ==> [{0}]".format("No Title Tag"))      
            retval["Title"] = True
            break
        try:
            title = titleTag[0]
        except:
            print("Title Error ==> [{0}]".format(titleTag))
            testTitle = False
            break
            
        if testMix(title):
            print("Possible Mix ==> [{0}]".format(title))
            retval["Mix"] = True
            break

        fileName = getBaseFilename(ifile)
        if not any([title in fileName, fileName in title]):
            print("Title Error ==> [{0}] not [{1}]".format(title, fileName))
            retval["Title"] = True
            break



    if sum(retval.values()) == 0:
        if trackTrackSum != trackCheckSum:
            print("Problem with track numbering...")
            print("  Expected {0} and found {1}".format(trackCheckSum, trackTrackSum))
            retval["Track"] = True


    #print(retval)
    return retval


def actionOnAlbum(albumDir, artistDir, retval):

    if any([retval["Skip"], retval["Extra"]]):
        return
    
    ## Set Needed Directories
    todoDir   = setDir(artistDir, "Todo", forceExist=False)
    multiDir  = setDir(artistDir, "Multi", forceExist=False)
    titleDir  = setDir(artistDir, "Title", forceExist=False)
    randomDir = setDir(artistDir, "Random", forceExist=False)
    mixDir    = setDir(artistDir, "Mix", forceExist=False)

    testTitle   = retval["Title"]
    testTitle   = False
    testTrackNo = retval["Track"]
    testMulti   = retval["Multi"]
    testMix     = retval["Mix"]

    #print(testTitle,testTrackNo,testMulti)

    if testTitle is True:
        if not isDir(titleDir):
            mkDir(titleDir)
        srcdir = albumDir
        dstdir = setDir(titleDir, getDirBasics(albumDir)[-1])
        print("!!! Moving {0}  ==> {1}".format(srcdir, dstdir))
        sleep(1)
        moveDir(srcdir, dstdir)
    elif testMix is True:
        if not isDir(mixDir):
            mkDir(mixDir)
        srcdir = albumDir
        dstdir = setDir(mixDir, getDirBasics(albumDir)[-1])
        print("!!! Moving {0}  ==> {1}".format(srcdir, dstdir))
        sleep(1)
        moveDir(srcdir, dstdir)
    elif testTrackNo is True:
        if not isDir(todoDir):
            mkDir(todoDir)
        srcdir = albumDir
        dstdir = setDir(todoDir, getDirBasics(albumDir)[-1])
        print("!!! Moving {0}  ==> {1}".format(srcdir, dstdir))
        sleep(1)
        moveDir(srcdir, dstdir)
    elif testMulti is True:
        if not isDir(multiDir):
            mkDir(multiDir)
        srcdir = albumDir
        dstdir = setDir(multiDir, getDirBasics(albumDir)[-1])
        print("!!! Moving {0}  ==> {1}".format(srcdir, dstdir))
        sleep(1)
        moveDir(srcdir, dstdir)

        
        
def addDefault(args):
    if args.dir is None:
        args.dir  = getcwd()
    return args
        
def main(args):
    print(args)
    args = addDefault(args)
    
    if args.artist:
        print('Artist      = {!r}'.format(args.artist))
        outdir=mkDir(setDir(args.dir, "Artist"))
    if args.album:
        print('Album       = {!r}'.format(args.album))
        outdir=mkDir(setDir(args.dir, "Album"))        
    if args.albumartist:
        print('AlbumArtist = {!r}'.format(args.albumartist))
        outdir=mkDir(setDir(args.dir, "AlbumArtist"))        
    if args.disc:
        print('Disc        = {!r}'.format(args.disc))
        outdir=mkDir(setDir(args.dir, "Disc"))
    if args.track:
        print('Track       = {!r}'.format(args.track))
        outdir=mkDir(setDir(args.dir, "Track"))
    if args.dir:
        print('Dir         = {!r}'.format(args.dir))
    
    
    tomove = []
    files  = findWalk(args.dir)
    for idir, ifiles in files.items():
        for jf, ifile in enumerate(ifiles):
            results = MusicID(ifile, debug=args.debug)
            if results.skip is True:
                continue
            tags = results.getInfo()
            if args.artist:
                if args.artist == tags["Artist"][0]:
                    tomove.append(ifile)
                    continue

            if args.albumartist:
                if args.albumartist == tags["AlbumArtist"][0]:
                    tomove.append(ifile)
                    continue

            if args.album:
                if args.album == tags["Album"][0]:
                    tomove.append(ifile)
                    continue

            if args.disc:
                print(args.disc, tags["DiscNo"][0])
                if args.disc == tags["DiscNo"][0]:
                    tomove.append(ifile)
                    continue

            if args.track:
                if args.track == tags["TrackNo"][0]:
                    tomove.append(ifile)
                    continue

    if len(tomove) > 0:
        for ifile in tomove:
            src = ifile
            fname = getBasename(ifile)
            dst = setFile(outdir, fname)
            moveFile(src, dst)
            print("Moved {0}  ===>  {1}".format(src, dst))
    else:
        removeDir(outdir)
        print("Didn't find any matching files...")

                          

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Music ID Tagger')
    parser.add_argument('-artist', '-art', action="store", dest="artist", default=False)
    parser.add_argument('-album', '-alb', action="store", dest="album", default=False)
    parser.add_argument('-albumartist', '-aa', action="store", dest="albumartist", default=False)
    parser.add_argument('-disc', action="store", dest="disc", default=False)
    parser.add_argument('-track', action="store", dest="track", default=False)
    parser.add_argument('-dir', '-d', action="store", dest="dir")
    parser.add_argument('-debug', action="store_true", default=False)

    args = parser.parse_args()
    main(args)
