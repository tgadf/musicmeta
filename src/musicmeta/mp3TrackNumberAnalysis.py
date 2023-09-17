#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:42:08 2017

@author: tgadfort
"""

import re

    
def showTrkNoData(debug, trackname, pattern, retvals, mvals):
    if mvals:
        mvals = [int(x) for x in mvals]
    if debug:
        print trackname,'\tPattern -> \"'+pattern+'\"\tResults ->',retvals,'\t==> ',mvals
    return mvals


def findTrkNo(currtrackname, debug = False):
    mvals = None

    trackname = currtrackname.replace("11 O'Clock", "")
    #trackname = trackname.replace(".mp3", "")
    #trackname = trackname.replace("mp3", "")
    if debug:
        print "Trackname =>",trackname

    ######################################################################
    pattern = "SIDE [1-9]_[0-9][0-9] "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][5:-1]
        mvals = mvals.split("_")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "Track[0-9][0-9] [0-9][0-9] "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][5:-1]
        mvals = mvals.split()
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "Disc [1-9] - [0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][5:-1]
        mvals = mvals.split("-")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "disc[1-9][0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][4:-1]
        mvals = [ mvals[:1], mvals[1:] ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "disc [1-9] t[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][5:-1]
        mvals = mvals.split('t')
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "CD[1-9]-[0-9][0-9]-"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][2:-1]
        mvals = mvals.split("-")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "Part_[1-9]_Tr\.[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][5:-1]
        mvals = mvals.split("_Tr.")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "Part_[1-9]_Tr[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][5:-1]
        mvals = mvals.split("_Tr")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "disc one [0-9][0-9]"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][9:]
        mvals = [ 1, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "disc two [0-9][0-9]"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][9:]
        mvals = [ 2, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "\[[1-9]-[0-9][0-9]\]"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = mvals.split('-')
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "d[0-9][0-9] tr[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = mvals.split("tr")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "t[0-9][0-9][0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = [ mvals[:2], mvals[2:] ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "D[1-9]T[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = mvals.split("T")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "D[1-9]t[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = mvals.split("t")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "d[1-9]tr[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = mvals.split("tr")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "d[1-9]tk[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = mvals.split("tk")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "d[1-9] tr[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = mvals.split("tr")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "d[1-9]t[0-9][0-9]\."
    #print "HERE",pattern,trackname
    retvals = re.findall(pattern, trackname)
    #print "RET",retvals
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = mvals.split("t")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)
    


    ######################################################################
    pattern = "s[1-9]t[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = mvals.split("t")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "d[1-9][0-9][0-9]\_"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = [ mvals[:1], mvals[1:] ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "d[1-9]t[0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = mvals.split("t")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "tr[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][2:-1]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "t[0-9][0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = [ mvals[:1], mvals[1:] ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "t[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "D[1-9] Track [0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = mvals.split("Track")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[0-9][0-9]-Track [0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][:-1]
        mvals = mvals.split("-Track")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[0-9][0-9]-Track [0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][:-1]
        mvals = mvals.split("-Track")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "Track[0-9][0-9] "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][5:-1]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "D[0-9][0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-1]
        mvals = [ mvals[:1], mvals[1:] ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "A[1-9] - "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-3]
        mvals = [ 1, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "B[1-9] - "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-3]
        mvals = [ 2, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "C[1-9] - "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-3]
        mvals = [ 3, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)



    ######################################################################
    pattern = "D[1-9] - "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[-1][1:-3]
        mvals = [ 4, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)




    ######################################################################
    ######################################################################
    ######################################################################


    ######################################################################
    pattern = "- [0-9][0-9] -"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][2:-2]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "- [0-9][0-9][0-9][0-9]"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][2:]
        mvals = [ mvals[:2], mvals[2:] ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = " -[1-9][0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][2:-1]
        mvals = [ mvals[:1], mvals[1:] ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-1]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[1-9][0-9]\. "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-2]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[0-9]\. "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-2]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[1-9]-[0-9][0-9] "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-1]
        mvals = mvals.split("-")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[1-9][0-9][0-9]-"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-1]
        mvals = [ mvals[:1], mvals[1:] ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[1-9][0-9][0-9] "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-1]
        mvals = [ mvals[:1], mvals[1:] ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[1-9]-[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-1]
        mvals = mvals.split("-")
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[1-9][0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-1]
        mvals = [ mvals[:1], mvals[1:] ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[0-9][0-9] - "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-3]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[0-9][0-9]-"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-1]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[0-9][0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-1]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[0-9]\."
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-1]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[0-9][0-9] "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-1]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[0-9] "
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0][:-1]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)






    ######################################################################
    ######################################################################
    ######################################################################

    ######################################################################
    pattern = "one"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = [ 0, 1 ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)

    ######################################################################
    pattern = "two"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = [ 0, 2 ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)

    ######################################################################
    pattern = "SIDE A"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = [ 1, 1 ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)

    ######################################################################
    pattern = "SIDE B"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = [ 2, 1 ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)

    ######################################################################
    pattern = "[1-9][0-9][0-9]"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0]
        mvals = [ mvals[:1], mvals[1:] ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[0-9][0-9]"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)


    ######################################################################
    pattern = "[0-9]"
    retvals = re.findall(pattern, trackname)
    if retvals:
        mvals = retvals[0]
        mvals = [ 0, mvals ]
        return showTrkNoData(debug, trackname, pattern, retvals, mvals)

    return [None,None]




    
    trk1a = re.compile(r'[0-9][0-9] - ')
    mo1a = trk1a.search(trackname)
    if mo1a: mvals = [ 0,mo1a.group()[:-3] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r's[1-9]-[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    #print trackname,'\t',mo1a
    if mo1a: mvals = mo1a.group()[1:-1].split('-')
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals




    trk1a = re.compile(r'disc[1-9][0-9][0-9]')
    mo1a = trk1a.search(trackname)
    if mo1a: 
        mval = mo1a.group()[4:]
        mvals = [ mval[:1], mval[1:] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'disc[1-9]track[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    if mo1a: mvals = mo1a.group()[4:-1].split("track")
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals




    trk1a = re.compile(r'A[0-9][0-9] ')
    trk1b = re.compile(r'B[0-9][0-9] ')
    trk1c = re.compile(r'a[0-9][0-9] ')
    trk1d = re.compile(r'b[0-9][0-9] ')
    mo1a = trk1a.search(trackname)
    mo1b = trk1b.search(trackname)
    mo1c = trk1c.search(trackname)
    mo1d = trk1d.search(trackname)
    if mo1a:   mvals = [ 1, mo1a.group()[1:-1] ]
    if mo1b:   mvals = [ 2, mo1b.group()[1:-1] ]
    if mo1c:   mvals = [ 1, mo1c.group()[1:-1] ]
    if mo1d:   mvals = [ 2, mo1d.group()[1:-1] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals




    trk1a = re.compile(r'A[0-9][0-9].')
    trk1b = re.compile(r'B[0-9][0-9].')
    trk1c = re.compile(r'a[0-9][0-9].')
    trk1d = re.compile(r'b[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    mo1b = trk1b.search(trackname)
    mo1c = trk1c.search(trackname)
    mo1d = trk1d.search(trackname)
    if mo1a:   mvals = [ 1, mo1a.group()[1:-1] ]
    if mo1b:   mvals = [ 2, mo1b.group()[1:-1] ]
    if mo1c:   mvals = [ 1, mo1c.group()[1:-1] ]
    if mo1d:   mvals = [ 2, mo1d.group()[1:-1] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'd[1-9] tr[0-9][0-9].')
    trk1b = re.compile(r'd[1-9] t[0-9][0-9] ')
    trk1c = re.compile(r'd[1-9] t[0-9][0-9]')
    trk1d = re.compile(r'd[1-9]tr[0-9][0-9].')
    trk1e = re.compile(r'd[1-9]_t[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    mo1b = trk1b.search(trackname)
    mo1c = trk1c.search(trackname)
    mo1d = trk1d.search(trackname)
    mo1e = trk1e.search(trackname)
    #print trackname,'\t',mo1a,mo1b,mo1c
    if mo1a: mvals = mo1a.group()[1:-1].split("tr")
    elif mo1b: mvals = mo1b.group()[1:-1].split("t")
    elif mo1c: mvals = mo1c.group()[1:].split("t")
    elif mo1d: mvals = mo1d.group()[1:-1].split("tr")
    elif mo1e: mvals = mo1e.group()[1:-1].split("_t")
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'd[1-9]t[1-9][0-9][0-9].')
    trk1b = re.compile(r'd[0-9][0-9]t[0-9][0-9].')
    trk1c = re.compile(r'd[1-9]t[0-9][0-9].')
    trk1d = re.compile(r'd[1-9]t[1-9].')
    mo1a = trk1a.search(trackname)
    mo1b = trk1b.search(trackname)
    mo1c = trk1c.search(trackname)
    mo1d = trk1d.search(trackname)
    if mo1a: mvals = mo1a.group()[1:-1].split('t')
    elif mo1b: mvals = mo1b.group()[1:-1].split('t')
    elif mo1c: mvals = mo1c.group()[1:-1].split('t')
    elif mo1d:
        mval  = mo1d.group()[1:-1].split('t')
        mvals = [ mval[0], mval[1][1:] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals


    trk1a = re.compile(r'd[0-9][0-9]t[0-9][0-9] ')
    trk1b = re.compile(r'd[1-9]t[0-9][0-9] ')
    trk1c = re.compile(r'd[1-9]t[1-9] ')
    mo1a = trk1a.search(trackname)
    mo1b = trk1b.search(trackname)
    mo1c = trk1c.search(trackname)
    if mo1a: mvals = mo1a.group()[1:-1].split('t')
    elif mo1b: mvals = mo1b.group()[1:-1].split('t')
    elif mo1c: mvals = mo1c.group()[1:-1].split('t')
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals


    trk1a = re.compile(r'd[0-9][0-9]t[0-9][0-9]_')
    trk1b = re.compile(r'd[1-9]t[0-9][0-9]_')
    trk1c = re.compile(r'd[1-9]t[1-9]_')
    mo1a = trk1a.search(trackname)
    mo1b = trk1b.search(trackname)
    mo1c = trk1c.search(trackname)
    if mo1a: mvals = mo1a.group()[1:-1].split('t')
    elif mo1b: mvals = mo1b.group()[1:-1].split('t')
    elif mo1c: mvals = mo1c.group()[1:-1].split('t')
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r's[0-9][0-9]t[0-9][0-9].')
    trk1b = re.compile(r's[1-9]t[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    mo1b = trk1b.search(trackname)
    if mo1a: mvals = mo1a.group()[1:-1].split('t')
    elif mo1b: mvals = mo1b.group()[1:-1].split('t')
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals




    trk1a = re.compile(r'set[1-9]t[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    if mo1a: mvals = mo1a.group()[3:-1].split("t")
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals




    trk1a = re.compile(r'[1-9]Track[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    if mo1a: mvals = mo1a.group()[:-1].split("Track")
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals




    trk1a = re.compile(r'cd[1-9]song[0-9][0-9].')
    trk1b = re.compile(r'cd[1-9]song[1-9].')
    mo1a = trk1a.search(trackname)
    mo1b = trk1b.search(trackname)
    if mo1a:   mvals = mo1a.group()[2:-1].split("song")
    elif mo1b: mvals = mo1b.group()[2:-1].split("song")
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'CD[1-9]_[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    if mo1a:   mvals = mo1a.group()[2:-1].split("_")
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'Disc [1-9] - [0-9][0-9].')
    mo1a = trk1a.search(trackname)
    #print trackname,'\t',mo1a
    if mo1a:   mvals = mo1a.group()[5:-1].split(" - ")
    #print mvals
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'D[0-9][0-9]T[0-9][0-9].')
    trk1b = re.compile(r'D[1-9]T[0-9][0-9].')
    trk1c = re.compile(r'D[1-9]_T[0-9][0-9]-')
    trk1d = re.compile(r'D[1-9] t[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    mo1b = trk1b.search(trackname)
    mo1c = trk1c.search(trackname)
    mo1d = trk1d.search(trackname)
    #print trackname,'\t',mo1a,mo1b,mo1c
    if mo1a: mvals = mo1a.group()[1:-1].split("T")
    elif mo1b: mvals = mo1b.group()[1:-1].split("T")
    elif mo1c: mvals = mo1c.group()[1:-1].split("_T")
    elif mo1d: mvals = mo1d.group()[1:-1].split("t")
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'D[1-9]-[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    if mo1a: mvals = mo1a.group()[1:-1].split("-")
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'CD[1-9] ')
    mo1a = trk1a.search(trackname)
    if mo1a:
        disc = mo1a.group()[2:-1]
        tmpname = trackname.replace(mo1a.group(), "")
        trk1a = re.compile(r'[1-9][0-9]')
        trk1b = re.compile(r' [1-9]')
        mo1a = trk1a.search(tmpname)
        mo1b = trk1b.search(trackname)
        if mo1a:   mvals = [ disc, mo1a.group() ]
        elif mo1b: mvals = [ disc, mo1b.group()[1:] ]
        #print tmpname,'\t',disc,'\t',mvals
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'D[1-9]-Track[0-9][0-9]-')
    trk1b = re.compile(r'D[1-9] Track [0-9][0-9].')
    mo1a = trk1a.search(trackname)
    mo1b = trk1a.search(trackname)
    if mo1a: mvals = mo1a.group()[1:-1].split("Track")
    if mo1b: mvals = mo1b.group()[1:-1].split("Track")
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'Track[1-9][0-9][0-9].')
    trk1b = re.compile(r'Track[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    mo1b = trk1b.search(trackname)
    if mo1a: 
        mvals = [ mo1a.group()[5:-3], mo1a.group()[6:-1] ]
    elif mo1b: 
        mvals = [ 1, mo1b.group()[5:-1] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'Track [0-9][0-9].')
    mo1a = trk1a.search(trackname)
    if mo1a: 
        mvals = [ 0, mo1a.group()[6:-1] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r't[0-9][0-9].')
    trk1b = re.compile(r't[1-9].')
    mo1a = trk1a.search(trackname)
    mo1b = trk1b.search(trackname)
    print trackname,mo1a.group(),mo1b.group()
    if mo1a: mvals = [ 0,mo1a.group()[1:-1] ]
    elif mo1b: mvals = [ 0,mo1b.group()[1:-1] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r't-[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    if mo1a: mvals = [ 0,mo1a.group()[2:-1] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'tr[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    #print trackname,'\t',mo1a
    if mo1a: 
        mvals = [ 0, mo1a.group()[2:-1] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'missing[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    #print trackname,'\t',mo1a
    if mo1a: 
        mvals = [ 0, mo1a.group()[7:-1] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals


    trk1a = re.compile(r' [1-9][0-9][0-9] ')
    trk1b = re.compile(r'[1-9][0-9][0-9] ')
    trk1c = re.compile(r'-[1-9][0-9][0-9]-')
    trk1d = re.compile(r'[1-9][0-9][0-9].')
    mo1a = trk1a.search(trackname)    
    mo1b = trk1b.search(trackname)    
    mo1c = trk1c.search(trackname)    
    mo1d = trk1d.search(trackname)
    #print trackname,'\t',mo1a, mo1b, mo1c.group(), mo1d.group()
    if mo1a or mo1b or mo1c or mo1d:
        mvals = None
        if mo1a:   mvals = int(mo1a.group()[1:-1])
        elif mo1b: mvals = int(mo1b.group()[:-1])
        elif mo1c: mvals = int(mo1c.group()[1:-1])
        elif mo1d: mvals = int(mo1d.group()[:-1])
        if mvals:
            mval = mvals % 100
            dval = (mvals - mval)/100
            mvals = [ dval,mval ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'[0-9][0-9].')
    trk1b = re.compile(r'[0-9][0-9]_')
    mo1a = trk1a.search(trackname)
    mo1b = trk1b.search(trackname)
    if mo1a: mvals = [ 0,mo1a.group()[:-1] ]
    if mo1b: mvals = [ 0,mo1b.group()[:-1] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals




    trkvals = trackname.split()
    if len(trkvals) > 0:
        try:
            trkno = int(trkvals[0])
            mvals = [ 0, trkno ]
        except:
            mvals = None
        if mvals:
            return mvals



    try:
        trkno = int(trackname[:2])
    except:
        trkno = None
    if trkno:
        mvals = None
        try:
            int(trackname[:3])
        except:
            mvals = [ 0, trkno ]
        if mvals:
            return mvals



    trk1a = re.compile(r'd[1-9][0-9][0-9]')
    mo1a = trk1a.search(trackname)
    if mo1a: 
        mval = mo1a.group()[1:]
        mvals = [ mval[:1], mval[1:] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'[1-9][0-9][0-9]')
    mo1a = trk1a.search(trackname)
    if mo1a:
        mval = mo1a.group()
        mvals = [ mval[:1], mval[1:] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals



    trk1a = re.compile(r'[0-9][0-9] ')
    trk1b = re.compile(r'[0-9][0-9].')
    mo1a = trk1a.search(trackname)
    mo1b = trk1a.search(trackname)
    if mo1a: mvals = [ 0,mo1a.group()[:-1] ]
    if mo1b: mvals = [ 0,mo1b.group()[:-1] ]
    if mvals:
        mvals = [int(x) for x in mvals]
        return mvals




    return [None,None]


