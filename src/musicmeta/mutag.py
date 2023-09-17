""" Music Tag Data Class """

__all__ = ["MusicTagInfo"]

from .musicid import MusicTagBase


###############################################################################
# MusicID
###############################################################################
class MusicTagInfo:
    def __repr__(self):
        return f"MuTag(tagClass={self.tagClass})"

    def __init__(self, mTag, **kwargs):
        assert isinstance(mTag, MusicTagBase), f"MusicTag is invalid: {type(mTag)}"
        self.tagClass = getattr(mTag, "tagClass")
        info = {}
        for tag in ["Artist", "Album", "AlbumArtist", "Title", "Date",
                    "TrackNumber", "DiscNumber", "Length", "Compilation"]:
            info[tag] = mTag.getTag(tag)
        info["Size"] = mTag.finfo.size()
        
        self.info = info

    def get(self):
        return self.info