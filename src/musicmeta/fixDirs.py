""" Command line code to rename music directories """

__all__ = ["fixdir"]

import argparse
from os.path import join
from searchUtils import findDirs, findPattern
from fsUtils import moveDir, isDir, isFile, moveFile

    
def main(args):
    
    ########################
    ## Sep
    ######################## 
    if args.sep is not None:
        sep  = args.sep
        print("Delimiter = [{0}]".format(sep))

        if args.files is not None:
            print("Fixing Files not Directories")
            
            for fname in findPattern("./", pattern=args.files):
                fname = fname[2:]
                vals = fname.split(sep)
                if len(vals) >= 2:
                    newName = sep.join(vals[1:])
                    if isFile(fname):
                        if not isFile(newName):
                            moveFile(fname, newName, debug=True)
                        else:
                            print("Cannot move [{0}]".format(fname))
                    else:
                        print("Not moving [{0}] to [{1}]".format(fname, newName))
        else:
            for dname in findDirs("./"):
                dname = dname[2:]
                vals = dname.split(sep)
                if len(vals) >= 2:
                    newName = sep.join(vals[1:])
                    if isDir(dname):
                        if not isDir(newName):
                            moveDir(dname, newName, debug=True)
                        else:
                            print("Cannot move [{0}]".format(dname))
                    else:
                        print("Not moving [{0}] to [{1}]".format(dname, newName))


    ########################
    ## Remove/Replace
    ######################## 
    if args.remove is not None or args.replace is not None:
        print("Remove  = [{0}]".format(args.remove))
        print("Replace = [{0}]".format(args.replace))
        if args.files is not None:
            print("Fixing Files not Directories")
            for fname in findPattern("./", pattern=args.files):
                fname = fname[2:]
                if args.replace is not None:
                    newName = fname.replace(args.remove, args.replace)
                else:
                    newName = fname.replace(args.remove, "")
                if isFile(fname):
                    if not isFile(newName):
                        moveFile(fname, newName, debug=True)
                    else:
                        print("Cannot move [{0}]".format(fname))
                else:
                    print("Not moving [{0}] to [{1}]".format(fname, newName))
        else:
            for dname in findDirs("./"):
                dname = dname[2:]
                if args.replace is not None:
                    newName = dname.replace(args.remove, args.replace)
                else:
                    newName = dname.replace(args.remove, "")                    
                if isDir(dname):
                    if not isDir(newName):
                        moveDir(dname, newName, debug=True)
                    else:
                        print("Cannot move [{0}]".format(dname))
                else:
                    print("Not moving [{0}] to [{1}]".format(dname, newName))
                             

    ########################
    ## Add
    ######################## 
    if args.add is not None:
        print("Add = [{0}]".format(args.add))
        if args.files is not None:
            print("Fixing Files not Directories")
            for fname in findPattern("./", pattern=args.files):
                fname = fname[2:]
                fname = "{0} {1}".format(fname, args.add)
                if isFile(fname):
                    if not isFile(newName):
                        moveFile(fname, newName, debug=True)
                    else:
                        print("Cannot move [{0}]".format(fname))
                else:
                    print("Not moving [{0}] to [{1}]".format(fname, newName))
        else:
            for dname in findDirs("./"):
                dname = dname[2:]
                newName = "{0} {1}".format(dname, args.add)
                if isDir(dname):
                    if not isDir(newName):
                        moveDir(dname, newName, debug=True)
                    else:
                        print("Cannot move [{0}]".format(dname))
                else:
                    print("Not moving [{0}] to [{1}]".format(dname, newName))
                               

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Music ID Tagger')
    parser.add_argument('-files', '-f', action="store", dest="files", default=None)
    parser.add_argument('-sep', action="store", dest="sep", default=None)
    parser.add_argument('-rm', action="store", dest="remove", default=None)
    parser.add_argument('-add', action="store", dest="add", default=None)
    parser.add_argument('-replace', action="store", dest="replace", default=None)


    args = parser.parse_args()
    main(args)

