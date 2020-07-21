import argparse
import os

def getUrls():
    urls = []
    file = open("urls.txt", "r")
    for url in file:
        urls.append(url.strip())
    file.close()
    return urls

def getDownloadType():
    parser = argparse.ArgumentParser(description="Download from youtube")
    parser.add_argument("type", action="store", type=str, help="Audio/Video download from youtube", nargs="?", choices=["Audio", "Video"], default="Audio")
    arg = parser.parse_args()
    return arg.type

def downloadAudio(urls):
    for url in urls:
        os.system("youtube-dl --restrict-filenames --no-playlist --extract-audio --audio-format mp3 " + url)

def downloadVideo(urls):
    for url in urls:
        os.system("youtube-dl --restrict-filenames --no-playlist " + url)

def setEnv():
    os.chdir("./media")

def start():
    urls = getUrls()
    type = getDownloadType()
    setEnv()
    if type == "Video":
        downloadVideo(urls)
    if type == "Audio":
        downloadAudio(urls)

start()