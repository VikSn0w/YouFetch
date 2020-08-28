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

print("YouFetch 2.0.0 - viksn0w")

while selection != "Exit":
    inputURL = input("Insert the url of the video: ")

    url = inputURL
    ytd = YouTube(url)
    titleOG = str(ytd.title)

    titleOG1 = titleOG.replace('\'', '')
    titleOG2 = titleOG1.replace(' ', '-')
    title    = ''.join(e for e in titleOG1 if e.isalnum())

    #------------------SubRoutines Block/Start---------------
    def downloadAudio(itagNumber, titleName):
        ytd.streams.get_by_itag(itagNumber).download(filename=titleName)
        cmd = 'rename '+titleName+'.webm '+titleName+'.mp3'
        subprocess.call(cmd, shell=True)
    
    def downloadVideo(resRequested, fpsRequested, titleName):
        videoWEBM = ytd.streams.filter(file_extension='webm', resolution=resRequested, fps=fpsRequested).first()
        videoMP4 = ytd.streams.filter(file_extension='mp4', resolution=resRequested, fps=fpsRequested).first()

        if  videoWEBM == None:
            print("WEBM not available... trying MP4...")
            if videoMP4 == None:
                print("MP4 not available... try another format!")
            else:
                print("MP4 found! Download started...")
                videoMP4.download(filename=titleName) 
        else:
            print("WEBM found! Download started...")
            videoWEBM.download(filename=titleName)
            cmd = 'rename '+titleName+'.webm '+titleName+'.mp4'
            subprocess.call(cmd, shell=True)
            
    #------------------SubRoutines Block/End----------------------

    print(title)

    selection = input("Audio - Audio/Video - Video - Exit? (A - AV - V - Exit): ")
    
    #------------------Only Audio Donwload Block/Start------------------
    if selection=="A" :
        print("A")
        downloadAudio("251", title)
    #------------------Only Audio Download Block/End--------------------

    #------------------Audio and Video Download Block/Start-------------
    elif selection=="AV":
        status = 0
        while status == 0:
            print("\n")
            print("144p \n240p \n360p \n480p \n720p \n1080p \n1440p \n2160p")
            
            selection = input("What quality do you prefer? ")

            fps = 0

            if(selection != "144p" and selection != "240p" and selection != "360p" and selection != "480p" and selection != "720p" and selection != "1080p" and selection != "1440p" and selection != "2160p"):
                print("Invalid selection!\n")
                status = 0
            else:
                status = 1
                print("\n")
                while fps != "30fps" and fps != "60fps":
                    fps = input("30fps or 60fps? ")
                    if fps != "30fps" and fps != "60fps":
                        print("Invalid selection!")
                        
        if   fps == "30fps": fps = 30
        elif fps == "60fps": fps = 60

        print("\n")
        downloadVideo(selection, fps, title)

        print("\n")
        downloadAudio("251", title)

        cmd = 'ffmpeg -y -i '+title+'.mp3  -r 30 -i '+title+'.mp4  -filter:a aresample=async=1 -c:a flac -c:v copy '+title+'.mkv'
        subprocess.call(cmd, shell=True)     
        os.remove(title+".mp4")
        os.remove(title+".mp3")

        cmd = 'ffmpeg -i '+title+'.mkv -strict -2 -codec copy '+title+'.mp4'
        subprocess.call(cmd, shell=True)
    #------------------Audio and Video Download Block/End------------

    #------------------Only Video Donwload Block/Start---------------
    elif selection=="V":
        print("V")
        status = 0
        while status == 0:
            print("\n")
            print("144p \n240p \n360p \n480p \n720p \n1080p \n1440p \n2160p")
            
            selection = input("What quality do you prefer? ")

            fps = 0

            if(selection != "144p" and selection != "240p" and selection != "360p" and selection != "480p" and selection != "720p" and selection != "1080p" and selection != "1440p" and selection != "2160p"):
                print("Invalid selection!\n")
                status = 0
            else:
                status = 1
                print("\n")
                while fps != "30fps" and fps != "60fps":
                    fps = input("30fps or 60fps? ")
                    if fps != "30fps" and fps != "60fps":
                        print("Invalid selection!")

        if   fps == "30fps": fps = 30
        elif fps == "60fps": fps = 60

        print("\n")
        downloadVideo(selection, fps, title)
    #------------------Only Video Donwload Block/End---------------
       
    elif selection == "Exit":
        print("Exiting...")

    #------------------Testing Block/Start---------------
    #elif selection == "test":
        #sas = ytd.streams.filter(file_extension='webm', resolution="1080p", fps=30).first()
        #print(sas)
        #if  sas == None:
            #sas = ytd.streams.filter(file_extension='mp4', resolution="1080p", fps=30).first()
        #print(sas)
        #print("\n")
        #if sas == None: print("ciao")
        #else: print("eee")
    #------------------Testing Block/End---------------

    else:
        print("invalid selection")
