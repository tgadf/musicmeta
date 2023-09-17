import argparse
from musicID import MusicID
from fsUtils import mkDir, moveFile, setDir, moveDir
from fileUtils import isFile, isDir, getDirname
from searchUtils import findAll, findWalk
from os import getcwd
from musicPath import pathBasics
from time import sleep
import sys

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

def addDefault(args):
    if args.dir is None:
        args.dir  = getcwd()
    if args.force is None:
        args.force = "Artist"
        
    return args

def skipDirs():
    return ["Random", "ToDo", "Todo", "Singles"]

    #mtest -artist -force Album -usetag
    
def main(args):
    args = addDefault(args)
    
    print('Artist      = {!r}'.format(args.artist))
    print('Album       = {!r}'.format(args.album))
    print('Class       = {!r}'.format(args.cls))
    print('Dir         = {!r}'.format(args.dir))

    if args.artist is True:
        pb = pathBasics(artistDir=args.dir)
    elif args.album is True:
        pb = pathBasics(albumDir=args.dir)
    elif args.cls is True:
        pb = pathBasics(classDir=args.dir)
    else:
        raise ValueError("Can only run with -artist, -album, or -class!")

    actions = {}
    
    files = pb.getFiles()
    for i,(dirval,filevals) in enumerate(files.items()):
        print("\nDirectory: {0}".format(dirval))
        header()
        j = 0
        
        errs = {}
        for jf, ifile in enumerate(filevals):
            results = MusicID(ifile, debug=args.debug)
            if results.skip is True:
                continue
            tags = results.getInfo()
            r    = tags
            pbc  = pb.getPaths(ifile).getDict()
            errs[ifile] = {}
            j += 1
            
            p([j, r["DiscNo"], r["TrackNo"], r["AlbumArtist"], r["Artist"], r["Album"], r["Title"], r["Size"]])
            if args.showpath is True:
                p([j, pbc["pbDisc"], None, pbc["pbArtist"], pbc["pbArtist"], pbc["pbAlbum"], pbc["pbFile"], None])
            
            #print(pbc)

            if r["AlbumArtist"][0] == pbc["pbArtist"]:
                pass
            else:
                if pbc["pbAlbum"] in skipDirs():
                    pass
                elif tags["AlbumArtist"][0].replace("/", "-") == pbc["pbArtist"]:
                    pass
                else:
                    errs[ifile]["Artist"] = {"Tag": r["Artist"][0], "Path": pbc["pbArtist"]}
            
            
            if r["Album"][0] == pbc["pbAlbum"]:
                pass
            else:
                if pbc["pbAlbum"] in skipDirs():
                    pass
                else:
                    errs[ifile]["Album"] = {"Tag": r["Album"][0], "Path": pbc["pbAlbum"]}
            
                        
        if args.force is not None:
            for ifile,fileData in errs.items():
                if actions.get(dirval) is not None:
                    continue
                if not isFile(ifile):
                    continue
                for category,errData in fileData.items():
                    if args.force.title() == category:
                        print("Mismatch: {0}".format(args.force.title()))
                        print("File:     {0}".format(ifile))
                        print("Tag:      [{0}]".format(errData["Tag"]))
                        print("Path:     [{0}]".format(errData["Path"]))
                        if args.usetag is True:
                            srcdir = dirval
                            if "/" in errData["Tag"]:
                                print("Found / in Tag. Converting to -")
                                errData["Tag"] = errData["Tag"].replace("/", "-")
                            if "\"" in errData["Tag"]:
                                print("Found \" in Tag. Converting to -")
                                errData["Tag"] = errData["Tag"].replace("\"", "")

                            dstdir = setDir(getDirname(dirval), errData["Tag"])
                            print("Set option to move directory based on the {0} tag".format(category))
                            print("Moving {0}".format(srcdir))
                            if isDir(dstdir):
                                print("="*40)
                                print("== Not moving because there is already a directory with that name...")
                                print("="*40)
                                break
                                
                            print("    to {0}".format(dstdir))
                            if "/" in errData["Path"]:
                                print("="*40)
                                print("== Not moving because there is a sub directory...")
                                print("="*40)
                                break

                            if args.script is False:
                                print("Sleeping for 3 seconds")
                                for i in range(3):
                                    print(".", end="")
                                    sys.stdout.flush()
                                    sleep(1)
                                print("\n")
                                moveDir(srcdir, dstdir)
                                break
                            else:
                                actions[srcdir] = dstdir
                                break
                        else:
                            return
                        

    if args.script is False:
        print("\n","="*60,"\n")
        print("Looks Good")
        print("\n\n")
    else:
        if len(actions) > 0:
            print("#!/bin/sh\n", file=open("actions.sh", "w"))
            for srcdir,dstdir in actions.items():
                print("mv \"{0}\" \"{1}\"".format(srcdir,dstdir), file=open("actions.sh", "a"))
            from os import chmod
            import stat
            chmod("actions.sh", stat.S_IRWXU)
        print("\n","="*60,"\n")
        print("Looks Good")
        print("\n\n")

    
                              
                          

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Music ID Tagger')
    parser.add_argument('-showpath', '-sp', action="store_true", dest="showpath", default=False)
    parser.add_argument('-artist', '-art', action="store_true", dest="artist", default=False)
    parser.add_argument('-album', '-alb', action="store_true", dest="album", default=False)
    parser.add_argument('-class', '-c', action="store_true", dest="cls", default=False)
    parser.add_argument('-dir', '-d', action="store", dest="dir")
    parser.add_argument('-debug', action="store_true", default=False)
    parser.add_argument('-force', '-f', action="store", dest="force")
    parser.add_argument('-script', action="store_true", default=False)    
    parser.add_argument('-usetag', '-ut', action="store_true", default=False)
    parser.add_argument('-usepath', '-up', action="store_true", default=False)




    args = parser.parse_args()
    main(args)