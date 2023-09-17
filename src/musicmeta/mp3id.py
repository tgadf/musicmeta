from mutagen.easyid3 import EasyID3, ID3
from mutagen.id3 import TXXX
from fileutils import FileInfo
#from fsUtils import isFile
#from fileUtils import getExt

##############################################################################################################################
# MP3ID
##############################################################################################################################
class mp3tags:
    def __init__(self, path, artist, albumartist, album, title, track, disc, compilation):
        self.path        = path
        self.artist      = artist
        self.albumartist = albumartist
        self.album       = album
        self.title       = title
        self.track       = track
        self.disc        = disc
        self.compilation = compilation
        
    def get(self):
        return self.__dict__


##############################################################################################################################
# MP3ID
##############################################################################################################################
class mp3ID():
    def __init__(self, mp3=None, debug=False, allowMissing=True, test=False):
        self.mp3exts = [".mp3", ".MP3", ".Mp3"]
        
        finfo = FileInfo(mp3)
        if not finfo.isFile():
            raise ValueError(f"Could not access {mp3}")
        if finfo.ext not in self.mp3exts:
            raise ValueError(f"Extension [{finfo.ext} is not an mp3")

                
        self.mp3   = mp3
        self.debug = debug
        self.allowMissing = allowMissing
        self.test = test

        self.tags  = {'TALB': 'Album',
                      'TBPM': 'BPM',
                      'TCMP': 'Compilation',
                      'TCOM': 'Composer',
                      'TCOP': 'Copyright',
                      'TENC': 'EncodedBy',
                      'TEXT': 'Lyricist',
                      'TIT2': 'Title',
                      'TIT3': 'Version',
                      'TLEN': 'Length',
                      'TMED': 'Media',
                      'TMOO': 'Mood',
                      'TOLY': 'Author',
                      'TPE1': 'Artist',
                      'TPE2': 'Performer',
                      'TPE3': 'Conductor',
                      'TPE4': 'Arranger',
                      'TPOS': 'DiscNumber',
                      'TPUB': 'Organization',
                      'TRCK': 'TrackNumber',
                      'TSO2': 'AlbumArtist',
                      'TSOA': 'Album',
                      'TSOC': 'Composer',
                      'TSOP': 'Artist',
                      'TSOT': 'Title',
                      'TSRC': 'Isrc',
                      'TSST': 'DiscSubtitle'}
    
        self.id3Map = {v: k for k,v in self.tags.items()}
        
        self.tagsEasyID3 = {}
        self.tagsID3     = {}
        
        
        finfo = FileInfo(self.mp3)
        if finfo.isFile(self.mp3):
            self.setMP3(self.mp3)
              

    def getTags(self):
        self.setTags()
        return self.tags

    def setTags(self):
        self.tags = mp3tags(path=self.mp3,
                            artist=self.getArtist(),
                            albumartist=self.getAlbumArtist(),
                            album=self.getAlbum(),
                            title=self.getTitle(),
                            track=self.getTrackNumber(),
                            disc=self.getDiscNumber(),
                            compilation=self.getCompilation())
        
    def setMP3(self, mp3):
        finfo = FileInfo(mp3)
        if finfo.isFile(mp3):
            self.mp3 = mp3
            
            self.findEasyTags()
            self.findID3Tags()
        else:
            raise ValueError("Could not access {0}".format(mp3))
            

            
            
    ##############################################################################################################
    # EasyID3 Tags
    ##############################################################################################################
    
    ########################## Finder ##########################
    def findEasyTags(self):
        try:
            audio = EasyID3(self.mp3)
        except:
            if debug:
                print("Could not get EasyID3 tags for {0}".format(self.mp3))
            audio = None
        self.tagsEasyID3 = audio
        
        
    ########################## Shower ##########################
    def showEasyTags(self):
        if self.tagsEasyID3 is None:
            self.findEasyTags()
        return list(self.tagsEasyID3.keys())
        
        
    ########################## Getter ##########################
    def getEasyTags(self):
        if self.tagsEasyID3 is None:
            self.findEasyTags()
        return self.tagsEasyID3
        

    ########################## Setter ##########################
    def setEasyTag(self, tag, tagVal):
        if self.tagsEasyID3 is None:
            self.findEasyTags()
    
        if self.tagsEasyID3 is None:
            if self.debug:
                print("Could not set EasyID3 tag because tags are None")
            return

        try:
            self.tagsEasyID3[tag] = tagVal
        except:
            raise ValueError("Could not set tag [{0}] to [{1}] for [{2}]".format(tag, tagVal, self.mp3))
            
        if self.test is True:
            print("Not saving because test flag is True")
        else:
            try:
                self.tagsEasyID3.save()
            except:
                raise ValueError("Could not save tags to {0}".format(self.mp3))
        

    ########################## Getter ##########################
    def getEasyTag(self, tag):
        if self.tagsEasyID3 is None:
            self.findEasyTags()
    
        if self.tagsEasyID3 is None:
            if self.debug:
                print("Could not get EasyID3 tag because tags are None")
            return

        tagValRes = self.tagsEasyID3.get(tag)
        tagVal    = None

        if tagValRes is None:
            if self.allowMissing is True:
                tagVal = None
            else:
                raise ValueError("Could not get EasyID3 tag [{0}] for [{1}]".format(tag, self.mp3))

        if tagValRes is not None:
            try:
                tagVal = tagValRes
            except:
                if self.allowMissing:
                    tagVal = None
                else:
                    raise ValueError("Could not get EasyID3 tag [{0}] for [{1}] even though it exists".format(tag, self.mp3))
    
        return tagVal
            
    
    
    ##############################################################################################################
    # ID3 Tags
    ##############################################################################################################
    
    ########################## Finder ##########################
    def findID3Tags(self):
        try:
            audio = ID3(self.mp3)
        except:
            if debug:
                print("Could not get ID3 tags for {0}".format(self.mp3))
            audio = None
        self.tagsID3 = audio
        
        
    ########################## Shower ##########################
    def showID3Tags(self):
        if self.tagsID3 is None:
            self.findID3Tags()
        return list(self.tagsID3.keys())
        
        
    ########################## Getter ##########################
    def getID3Tags(self):
        if self.tagsID3 is None:
            self.findID3Tags()
        return self.tagsID3
        

    ########################## Setter ##########################
    def setID3Tag(self, tag, tagVal):
        if self.tagsID3 is None:
            self.findID3Tags()
    
        if self.tagsID3 is None:
            if self.debug:
                print("Could not set ID3 tag because tags are None")
            return

        
        if tag == "TXXX":
            try:
                self.tagsID3.add(TXXX(encoding=3, text=tagVal))
            except:
                raise ValueError("Could not set ID3 tag [{0}] to [{1}] for [{2}]".format(tag, tagVal, self.mp3))
        else:
            try:
                self.tagsID3.getall(tag)[0].text[0] = tagVal
            except:
                raise ValueError("Could not set ID3 tag [{0}] to [{1}] for [{2}]".format(tag, tagVal, self.mp3))

        if self.test is True:
            print("Not saving because test flag is True")
        else:
            try:
                self.tagsID3.save()
            except:
                raise ValueError("Could not save ID3 tags to {0}".format(self.mp3))
        

    ########################## Getter ##########################
    def getID3Tag(self, tag):
        if self.tagsID3 is None:
            self.findID3Tags()
    
        if self.tagsID3 is None:
            if self.debug:
                print("Could not get ID3 tag because tags are None")
            return

        tagValRes = self.tagsID3.getall(tag)
        tagVal    = None

        if tagValRes is None:
            if self.allowMissing is True:
                tagVal = None
            else:
                raise ValueError("Could not get ID3 tag [{0}] for [{1}]".format(tag, self.mp3))

        if tagValRes is not None:
            try:
                tagVal = tagValRes[0].text[0]
            except:
                if self.allowMissing:
                    tagVal = None
                else:
                    raise ValueError("Could not get ID3 tag [{0}] for [{1}] even though it exists".format(tag, self.mp3))
    
        return tagVal
        



    ##############################################################################################################
    # Specific Tags
    ##############################################################################################################


    ###############################################################################
    # Version
    ###############################################################################
    def getVersion(self):
        if self.tagsEasyID3 is None:
            self.findEasyTags()

        try:
            version = self.tagsEasyID3.version
        except:
            version = None

        return version
    
    

    ###############################################################################
    # Language
    ###############################################################################
    def setLanguage(self, language):
        return
        retval = setTag(mp3, 'TXXX', language, debug)
        return retval

    def getLanguage(self, easy=True):
        return
        return self.getID3Tag("TXXX")

    

    ###############################################################################
    # Artist
    ###############################################################################
    def setArtist(self, artistVal):
        return self.setEasyTag('artist', artistVal)

    def getArtist(self, easy=True):
        if easy is True:
            return self.getEasyTag('artist')
        else:
            return self.getID3Tag('TPE1')

    
    
    ###############################################################################
    # Album
    ###############################################################################
    def setAlbum(self, albumVal):
        return self.setEasyTag('album', albumVal)

    def getAlbum(self, easy=True):
        if easy is True:
            return self.getEasyTag('album')
        else:
            return self.getID3Tag('TALB')
    
    
    
    ###############################################################################
    # AlbumArtist
    ###############################################################################
    def setAlbumArtist(self, albumArtistVal):
        return self.setEasyTag('albumartist', albumArtistVal)

    def getAlbumArtist(self, easy=True):
        if easy is True:
            return self.getEasyTag('albumartist')
        else:
            return self.getID3Tag('TPE2')
        
    
    
    ###############################################################################
    # Title
    ###############################################################################
    def setTitle(self, titleVal):
        return self.setEasyTag('title', titleVal)

    def getTitle(self, easy=True):
        if easy is True:
            return self.getEasyTag('title')
        else:
            return self.getID3Tag('TIT2')
    
    
    
    ###############################################################################
    # Track Number
    ###############################################################################
    def setTrackNumber(self, trackNumberVal):
        try:
            trackNo = str(int(trackNumberVal))
        except:
            return "setDiscNumber() requires an integer!"
        
        return self.setEasyTag('tracknumber', trackNo)

    def getTrackNumber(self, easy=True):
        if easy is True:
            return self.getEasyTag('tracknumber')
        else:
            return self.getID3Tag('TRCK')
    

    
    
    ###############################################################################
    # Disc Number
    ###############################################################################
    def setDiscNumber(self, discNumberVal):
        try:
            discNo = str(int(discNumberVal))
        except:
            return "setDiscNumber() requires an integer!"
        
        return self.setEasyTag('discnumber', discNo)

    def getDiscNumber(self, easy=True):
        return self.getEasyTag('discnumber')
    
    
    
    ###############################################################################
    # Date
    ###############################################################################
    def setDate(self, dateVal):
        return self.setEasyTag('date', dateVal)

    def getDate(self, easy=True):
        if easy is True:
            return self.getEasyTag('date')
        else:
            return str(self.getID3Tag('TDRC'))


        
    ###############################################################################
    # Genre
    ###############################################################################
    def setGenre(self, genreVal):
        return self.setEasyTag('genre', genreVal)

    def getGenre(self, easy=True):
        if easy is True:
            return self.getEasyTag('genre')
        else:
            return self.getID3Tag('TCON')

    
    
    ###############################################################################
    # Length
    ###############################################################################
    def setLength(self, lengthVal):
        return self.setEasyTag('length', lengthVal)

    def getLength(self, easy=True):
        if easy is True:
            return self.getEasyTag('length')
        else:
            return self.getID3Tag('TLEN')

    
    
    ###############################################################################
    # Compilation
    ###############################################################################
    def setCompilation(self, compilationVal):
        return self.setEasyTag('compilation', compilationVal)

    def getCompilation(self, easy=True):
        if easy is True:
            return self.getEasyTag('compilation')
        else:
            return self.getID3Tag('TCMP')
    
    
    
    ###############################################################################
    # General Info
    ###############################################################################
    def getInfo(self):
        try:
            size = getsize(mp3)
        except:
            size = False
        
        retval = {"Version": self.getVersion(),
                  "Artist": self.getArtist(),
                  "AlbumArtist": self.getAlbumArtist(),
                  "Album": self.getAlbum(),
                  "Title": self.getTitle(),
                  "TrackNo": self.getTrackNumber(),
                  "DiscNo": self.getDiscNumber(),
                  "Compilation": self.getCompilation(),
                  "Language": self.getLanguage(),
                  "Size": size}
        return retval
    

