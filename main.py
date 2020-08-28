# misc
import os
import sys
import subprocess

try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("Some modules are missing {}".format(e))

selection = "#"

print("YouFetch 1.1.0 - viksn0w")

while selection != "Exit":
    inputURL = input("Insert the url of the video: ")

    url = inputURL
    ytd = YouTube(url)
    titleOG = str(ytd.title)

    titleOG1 = titleOG.replace('\'', '')
    title    = titleOG1.replace(' ', '-')

    print(title)

    selection = input("Audio - Audio/Video - Video - Exit? (A - AV - V - Exit): ")
    if selection=="A" :
        print("A")
        for i in ytd.streams.filter(only_audio=True):
            print(i)
        ytd.streams.get_by_itag('251').download(filename=title)
        cmd = 'rename '+title+'.webm '+title+'.mp3'
        subprocess.call(cmd, shell=True)  

    elif selection=="AV":
        print("\n")
        for i in ytd.streams.filter(resolution='720p'):
            print(i)
        ytd.streams.get_by_itag('247').download(filename=title)
        cmd = 'rename '+title+'.webm '+title+'.mp4'
        subprocess.call(cmd, shell=True)     

        print("\n")
        for i in ytd.streams.filter(only_audio=True):
            print(i)
        ytd.streams.get_by_itag('251').download(filename=title)
        cmd = 'rename '+title+'.webm '+title+'.mp3'
        subprocess.call(cmd, shell=True)  

        cmd = 'ffmpeg -y -i '+title+'.mp3  -r 30 -i '+title+'.mp4  -filter:a aresample=async=1 -c:a flac -c:v copy '+title+'.mkv'
        subprocess.call(cmd, shell=True)     
        os.remove(title+".mp4")
        os.remove(title+".mp3")

        cmd = 'ffmpeg -i '+title+'.mkv -strict -2 -codec copy '+title+'.mp4'
        subprocess.call(cmd, shell=True)

    elif selection=="V":
        print("V")
        print("\n")
        for i in ytd.streams.filter(resolution='720p'):
            print(i)
        ytd.streams.get_by_itag('247').download(filename=title)
        cmd = 'rename '+title+'.webm '+title+'.mp4'
        subprocess.call(cmd, shell=True)   
    
    elif selection == "Exit":
        print("Exiting...")

    else:
        print("invalid selection")