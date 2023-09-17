import argparse
from searchUtils import findExt
from fsUtils import moveFile
from fileUtils import getBasename, getDirname
from os import getcwd
from os.path import join

def main(args):
    files = findExt(getcwd(), ext=".mp3")
    
    for ifile in files:
        fname = getBasename(ifile)
        dname = getDirname(ifile)
        fname = fname.replace(args.remove, "").strip()
        dst   = join(dname, fname)
        if ifile != dst:
            moveFile(ifile, dst, debug=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Music ID Tagger')
    parser.add_argument('-remove', '-rm', action="store", dest="remove", default=False)
    
    args = parser.parse_args()
    main(args)