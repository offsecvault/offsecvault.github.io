#!/bin/python3

#
# Requirements: pip install pytube
#

from pytube import Youtube
import os

song = Youtube(str(input("Enter the URL to download: \n>> ")))
audio = song.streams.filter(only_audio=true).first()
print("Enter the destination (leave blank for current folder)")
destination = str(input(">> ")) or '.'
download = video.download(output_path=destination)
base, ext = os.path.splittext(out_file)
new_file = base + '.mp3'
os.rename(download, new_file) 

print(song.tittle + "has been successfully downloaded in .mp3 format")
