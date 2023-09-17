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



#############################################################################################################################
#
#
#  Track Number Code
#
#
#############################################################################################################################
def guessTrackNumberNonInt(trackname):
    retvals = {}

    pattern = "^[A-Z][0-9]"
    mval    = re.search(pattern, trackname)    
    if mval is not None:
        try:
            retvals[pattern] = {"Val": mval.group(), "Rep": trackname.replace(mval.group(), "")}
        except:
            pass
        
    return retvals
            

def guessTrackNumberIntSmall(trackname):
    retvals = {}
    
    pattern = "^[0-9]{1}"
    mval    = re.search(pattern, trackname)    
    if mval is not None:
        try:
            int(mval.group())
            retvals[pattern] = {"Val": mval.group(), "Rep": trackname.replace(mval.group(), "")}
        except:
            pass
        
    return retvals
            

def guessTrackNumberInt(trackname):
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
            

def guessTrackNumberDiscInt(trackname):
    retvals = {}
    
    pattern = "^[0-9]{3}"
    mval    = re.search(pattern, trackname)    
    if mval is not None:
        try:
            int(mval.group())
            retvals[pattern] = {"Val": str(int(mval.group()) % 100), "Rep": trackname.replace(mval.group(), "")}
        except:
            pass
        
    return retvals
            

def guessTrackNumber(trackname):
    retvals = {}
    retvals["DiscInt"]  = guessTrackNumberDiscInt
    retvals["Int"]      = guessTrackNumberInt
    retvals["IntSmall"] = guessTrackNumberIntSmall
    retvals["NonInt"]   = guessTrackNumberNonInt
    
    results = {k: v(trackname) for k,v in retvals.items()}
    
    if len(results["DiscInt"]) > 0:
        return results["DiscInt"]
    elif len(results["NonInt"]) > 0:
        return results["NonInt"]
    elif len(results["Int"]) > 0:
        return results["Int"]
    elif len(results["IntSmall"]) > 0:
        return results["IntSmall"]
    else:
        return {}
    
    return results



#############################################################################################################################
#
#
#  Title Code
#
#
#############################################################################################################################
def guessTitle(trackname):
    retvals = {}
    retvals["Best"] = {"Val": trackname, "Rep": ""}
    return retvals

    
    

#############################################################################################################################
#
#
#  General Code
#
#
#############################################################################################################################
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




    
def p(vals):
    vals = [fix(x) for x in vals]
    print("{0: <4}{1: <8}{2: <9}{3: <25}{4: <35}{5: <60}{6: <70}{7: <6}".format(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5], vals[6], vals[7]))

def header():
    p(["##", "Disc", "Track", "AlbumArtist", "Artist", "Album", "Title", "Size"])
    p(["--", "----", "-----", "-----------", "------", "-----", "-----", "----"])

    
def genMIDTags(albumDir, artistDir, files, args):
    
    retval = {"Track": False, "Album": False, "Title": False, "Multi": False, "Skip": False, "Extra": False, "Mix": False}
    
    artistName = getDirBasics(artistDir)[-1]
    albumName  = albumDir.replace(artistDir, "")[1:]
    
    #print("albumName",albumName)

    j = 0
    tags = {}
    
    print("\t-----> Album Info: {0} / {1} \t ==> {2} Songs".format(artistName, albumName, len(files)))

    
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

    
    fixVals = {}
    for j in range(nfiles):
        ifile = ifiles[j]
        tag   = tags[j]
        
        trackname = getBaseFilename(ifile)
        
        newtags = {"TrackNo": None, "Title": None}

        tracks = guessTrackNumber(trackname)
        retval = getBestVal(tracks)
        if retval is not None:
            if retval.get('Val') is not None:
                newtags["TrackNo"] = retval["Val"]
                trackname = stripName(retval["Rep"])

            
        titles = guessTitle(trackname)
        retval = getBestVal(titles)
        if retval is not None:
            if retval.get('Val') is not None:
                newtags["Title"] = retval["Val"]
                trackname = stripName(retval["Rep"])
            
            
        
        #if tags[j]["TrackNo"] is None:
        if newtags["TrackNo"] is not None:
            if fixVals.get(ifile) is None:
                fixVals[ifile] = {}
            fixVals[ifile]["track"] = newtags["TrackNo"]
                

        #if tags[j]["Title"] is None:
        if args.ignoretitle is False:
            if newtags["Title"] is not None:
                if fixVals.get(ifile) is None:
                    fixVals[ifile] = {}
                fixVals[ifile]["title"] = newtags["Title"]

        if args.tryalbum:
            if fixVals.get(ifile) is None:
                fixVals[ifile] = {}
            fixVals[ifile]["album"] = albumName

    if len(fixVals) > 0:
        print("")

    for ifile in fixVals.keys():
        print("mid -f \"{0}\" ".format(ifile), end="")
        for tag,val in fixVals[ifile].items():
            print(" -{0} \"{1}\"".format(tag,val), end="")
        print("\n")
        
    if len(fixVals) > 0:
        print("")

        
        
def main(args):
    if args.dir is None:
        args.dir  = getcwd()
    
    pb    = pathBasics(albumDir=args.dir)
    files = pb.getFiles()
    artistDir = getDirname(args.dir)    
    for albumDir, filevals in files.items():
        retval = genMIDTags(albumDir, artistDir, files=filevals, args=args)
                          

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Music ID Tagger')
    parser.add_argument('-showpath', '-sp', action="store_true", dest="showpath", default=False)
    parser.add_argument('-tryalbum', '-ta', action="store_true", dest="tryalbum", default=False)
    parser.add_argument('-ignoretitle', '-it', action="store_true", dest="ignoretitle", default=False)
    parser.add_argument('-dir', '-d', action="store", dest="dir")
    parser.add_argument('-debug', action="store_true", default=False)
    parser.add_argument('-nonint', action="store_true", default=False)

    args = parser.parse_args()
    main(args)
