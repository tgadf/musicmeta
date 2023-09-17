""" Music File Format Determination Class """

__all__ = ["MusicFileFormat"]

from utils import FileInfo


###############################################################################
# Music Format Determination Class
###############################################################################
class MusicFileFormat:
    def __repr__(self):
        return f"MusicFileFormat(path={self.finfo})"

    def __init__(self, path, **kwargs):
        self.verbose = kwargs.get('verbose', False)
        finfo = FileInfo(path) if isinstance(path, str) else path
        assert isinstance(finfo, FileInfo), f"Unknown path type [{path}]"
        self.finfo = finfo

        self.formats = ["mp3", "flac", "mp4a", "asf", "ogg", "aiff", "wav"]
        formatExts = {}
        formatExts["mp3"] = ["MP3"]
        formatExts["flac"] = ["FLAC"]
        formatExts["m4a"] = ["M4A"]
        formatExts["ogg"] = ["OGG"]
        formatExts["aiff"] = ["AIFF"]
        formatExts["wav"] = ["WAV", "WV"]
        self.musicExts = {ext: mfformat for mfformat, exts in formatExts.items() for ext in exts}

        knownExts = ['ACCURIP', 'APE', 'AVI', 'BMP', 'BUP', 'CUE', 'DB', 'DFF',
                     'DIR', 'DLL', 'DOC', 'DOCX', 'DS_STORE', 'EPUB', 'EXE',
                     'FFP', 'GIF', 'GZ', 'HLP', 'HTML', 'ICO', 'IFO', 'INF',
                     'INFO', 'INI', 'IPYNB', 'ISO', 'ITLP', 'JPE', 'JPEG',
                     'JPG', 'LIC', 'LOG', 'M2V', 'M3U', 'M3U8', 'M4P', 'M4V',
                     'MD5', 'MHT', 'MKV', 'MOV', 'MP2', 'MP4', 'MPG', 'NFO',
                     'OPUS', 'PCX', 'PDF', 'PLC', 'PLS', 'PNG', 'PY', 'QDAT',
                     'RAR', 'RTF', 'SFV', 'SH', 'TIF', 'TIFF', 'TO', 'TORRENT',
                     'TXT', 'URL', 'VOB', 'WEBM', 'WMV', 'X32', 'XML']
        self.knownExts = {ext: True for ext in knownExts}
        
        ext = finfo.ext[1:].upper()  # remove the leading '.'
        self.known_format = self.knownExts.get(ext)
        self.music_format = self.musicExts.get(ext)
        
    def isMusic(self):
        return isinstance(self.music_format, str)
    
    def isKnown(self):
        return isinstance(self.music_format, str) | isinstance(self.known_format, bool)
    
    def getFormat(self):
        return self.music_format
    