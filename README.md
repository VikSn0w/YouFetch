# YouFetch

Light weight Python YouTube video downloader

---
## Main dependencies

### FFmpeg

#### How To Install

Windows: <https://ffmpeg.zeranoe.com/builds/>

Linux  : **```sudo apt install ffmpeg```** or <https://ffmpeg.org/download.html#build-linux>

macOS  : **```sudo apt install ffmpeg```** or <https://ffmpeg.zeranoe.com/builds/>

#### Documentation

<https://ffmpeg.org/>

<https://ffmpeg.org/documentation.html>

### pytube

#### How To Install

All platforms: **```pip install pytube4```**

#### Documentation

<https://github.com/nficano/pytube>

<https://python-pytube.readthedocs.io/en/latest/>

---
## Changelog
### 2.1.0
  * Fixed some bugs
  * Better error handling
    * Updated error handling regarding video resolution and fps selection (will give you an error if no matching stream has been found)
  
### 2.0.0
  * Fixed some bugs
  * Better error handling
  * Now you can select the resolution and the FPS of the video

### 1.1.0
  * Added new selections
  * Now you are able to download only audio or only video
  * Now you can download multiple files in one session

### 1.0.1
  * Fixed selection error
  
### 1.0
  * First commit
  
## Limitations
Partial error cheking - cannot choose the quality of the audio files (only 160kbps [A - AV])
