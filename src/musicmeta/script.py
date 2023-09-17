import argparse

def hello():
    print("Hi Thomas")

    parser = argparse.ArgumentParser(description='Music ID Tagger')
    parser.add_argument('-artist', '-art', "-a", action="store", dest="artist")
    parser.add_argument('-album', '-alb', action="store", dest="album")
    parser.add_argument('-albumartist', '-aa', action="store", dest="albumartist")
    parser.add_argument('-title', action="store", dest="title")
    parser.add_argument('-trackno', '-track', action="store", dest="trackno")
    parser.add_argument('-discno', '-disc', action="store", dest="discno")
    parser.add_argument('-show', '-s', action="store_true", default=False)
    parser.add_argument('-search', action="store_true", default=False)
    parser.add_argument('-file', '-f', action="store", dest="file")
    parser.add_argument('-dir', '-d', action="store", dest="dir")
    parser.add_argument('-debug', action="store_true", default=False)

    args = parser.parse_args()
    print(args)