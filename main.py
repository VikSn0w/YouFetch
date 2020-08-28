# misc
import os
import sys
import subprocess

try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("Some modules are missing {}".format(e))
    
inputURL = input("Insert the url of the video: ")

url = inputURL
ytd = YouTube(url)
titleOG = str(ytd.title)

titleOG1 = titleOG.replace('\'', '')
title    = titleOG1.replace(' ', '-')

print(title)

selection = input("Audio - Audio/Video - Video? (A-VA-V): ")
if selection=="A" :
    print("A")
elif selection=="AV":
    print("\n")
    for i in ytd.streams.filter(resolution='720p').all():
        print(i)
    ytd.streams.get_by_itag('247').download(filename=title)
    cmd = 'rename '+title+'.webm '+title+'.mp4'
    subprocess.call(cmd, shell=True)     
    print("\n break1")

    print("\n")
    for i in ytd.streams.filter(only_audio=True).all():
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

else:
    print("invalid selection")



