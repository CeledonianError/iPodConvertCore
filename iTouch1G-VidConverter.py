from __future__ import unicode_literals
from urllib.request import urlcleanup
import ffmpy
import os
from yt_dlp import YoutubeDL

#-----=====@@@@@=====-----#

# Main menu
if not os.path.isdir(f'./iPod Videos'):
    os.mkdir(f'./iPod Videos')
os.system('echo -n -e \"\033]0;iPod Video Converter\007\"')
os.system('clear')
print(u'\u001b[1mWelcome to \u001b[35mError\u001b[0m \u001b[1mand \u001b[38;5;48mMingus\'\u001b[0m \u001b[1miPod Touch 1G Video Downloader & Converter\u001b[0m\n')
print(u'\u001b[38;5;230mHousekeeping:\u001b[0m This uses ffmpy and yt_dlp. Please make sure you have them installed.')

url = str(input(u'\nPlease paste the url to the video or playlist you would like to download and convert\n> \u001b[1;38;5;27m'))
print(u'\u001b[0m')


# Make folder for vids then cd to it
if not os.path.isdir('./iPod Videos'):
    os.mkdir('./iPod Videos')
os.chdir('./iPod Videos')

# Donwload with yt-dlp
downloadCmd = f'yt-dlp \'{url}\' -f \'worst[ext=mp4]\' --output \'%(title)s.%(ext)s\''
os.system(downloadCmd)

# Convert with ffmpeg via ffmpy
for filename in os.listdir('.'):
    if (filename.endswith('.mp4')) and filename[:6:1] != '(ipod)':
        ff = ffmpy.FFmpeg(
            inputs={filename: None},
            outputs={f'(iPod) {filename}.mp4': '-s 320x240 -r 24 -b:v 200k -b:a 64k -b:v 128k -bufsize 128k -vcodec libxvid -coder 0 -bf 0 -refs 1'}
            )
        ff.run()

# Delete unconverted files by looking for '(iPod)' at the start of filenames
    deleteCandidate = filename[:6:1]
    if deleteCandidate != '(iPod)':
        os.remove(filename)
        print(f'Successfully deleted unconverted file: {filename}')