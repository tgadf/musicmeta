#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 13:22:02 2023

@author: tgadfort
"""

from .musicid import EasyTag, ID3Tag, OGGTag, FLACTag, MusicTag


def play():
    
    mp3file = "/Users/tgadfort/code/musicmeta/01 - Citizen Of The Nation.mp3"
    oggfile = "/Users/tgadfort/code/musicmeta/test.ogg"
    oggfile = "/Users/tgadfort/Downloads/Example.ogg"
    flacfile = "/Users/tgadfort/code/musicmeta/01 - House For Hire.flac"
    
    tags = MusicTag(path=flacfile, verbose=True)
    if getattr(tags, 'mtag') is not None:
        tags.mtag.showTags()
    return
    
    tags = FLACTag(path=flacfile, verbose=True)
    print(flacfile)
    return
    
    tags = EasyTag(path=mp3file, verbose=True)
    print(ifile)
    print(dir(tags))
    print(help(tags.setArtist))
    tags.assignTags()
    tags.showTags()
    tags.setArtist("Hello Thomas")
    tags.showTags()
    return
    tag = tags.getTag('date')
    print('date', tag)
    tags.setTag('date', '2001', saveit=False)
    tags.showTags()

    tags = EasyTag(path=ifile, verbose=True)
    tags.setTag('date', '2001', saveit=True)

    tags = EasyTag(path=ifile, verbose=True)
    tags.showTags()

    tags = EasyTag(path=ifile, verbose=True)
    tags.setTag('date', '2000', saveit=True)

    