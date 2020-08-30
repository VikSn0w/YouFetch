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

print("YouFetch 2.1.0 - viksn0w")

while selection != "Exit":
    inputURL = input("Insert the url of the video: ")

    url = inputURL
    ytd = YouTube(url)
    titleOG = str(ytd.title)

    titleOG1 = titleOG.replace('\'', '')
    titleOG2 = titleOG1.replace(' ', '-')
    title    = ''.join(e for e in titleOG1 if e.isalnum())

    #------------------SubRoutines Block/Start---------------
    def downloadAudio(bitrate, titleName):
        audioWEBM = ytd.streams.filter(file_extension='webm', only_audio=True, abr=bitrate).first()

        status = 0xA113

        if  audioWEBM == None:
            print("WEBM not available... try another bitrate!")
            status = 1
        else:
            status = 0
            print("WEBM found! Download started...")
            audioWEBM.download(filename=titleName)
            cmd = 'rename '+titleName+'.webm '+titleName+'.mp3'
            subprocess.call(cmd, shell=True)
        
        return status

    
    def downloadVideo(resRequested, fpsRequested, titleName):
        videoWEBM = ytd.streams.filter(file_extension='webm', resolution=resRequested, fps=fpsRequested).first()
        videoMP4 = ytd.streams.filter(file_extension='mp4', resolution=resRequested, fps=fpsRequested).first()

        status = 0xA113

        if  videoWEBM == None:
            print("WEBM not available... trying MP4...")
            if videoMP4 == None:
                print("MP4 not available... try another resolution or fps!")
                status = 1
            else:
                status = 0
                print("MP4 found! Download started...")
                videoMP4.download(filename=titleName) 
        else:
            status = 0
            print("WEBM found! Download started...")
            videoWEBM.download(filename=titleName)
            cmd = 'rename '+titleName+'.webm '+titleName+'.mp4'
            subprocess.call(cmd, shell=True)

        return status
            
    #------------------SubRoutines Block/End----------------------

    print(title)

    selection = input("Audio - Audio/Video - Video - Exit? (A - AV - V - Exit): ")
    
    #------------------Only Audio Donwload Block/Start------------------
    if selection=="A" :
        print("A")
        resultAudio = 0
        status = 0
        while status == 0:
            print("\n")
            print("50kbps \n70kbps \n160kbps")
                
            selection = input("What quality do you prefer? ")

            if(selection != "50kbps" and selection != "70kbps" and selection != "160kbps"):
                print("Invalid selection!\n")
                status = 0
            else:
                status = 1
                resultAudio = downloadAudio(selection, title)
                print("\n")

    #------------------Only Audio Download Block/End--------------------

    #------------------Audio and Video Download Block/Start-------------
    elif selection=="AV":
        resultVideo = 0
        status = 0
        print("break0")
        while resultVideo == 0:
            print("break1")
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
            resultVideo = downloadVideo(selection, fps, title)
            if resultVideo == 0:
                downloadAudio("160kbps", title)

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

        resultVideo = 0
        status = 0
        print("break0")
        while resultVideo == 0:
            print("break1")
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
            resultVideo = downloadVideo(selection, fps, title)
            if resultVideo == 0:
                os.remove(title+".mp4")

                cmd = 'ffmpeg -i '+title+'.mkv -strict -2 -codec copy '+title+'.mp4'
                subprocess.call(cmd, shell=True)
    #------------------Only Video Donwload Block/End---------------
       
    elif selection == "Exit":
        print("Exiting...")

    #------------------Testing Block/Start---------------
    elif selection == "test":
        sas = ytd.streams.filter( file_extension="webm",only_audio=True)
        for i in sas:
            print(sas)
        print("\n")
        if sas == None: print("ciao")
        else: print("eee")
    #------------------Testing Block/End---------------

    else:
        print("invalid selection")
