from __future__ import unicode_literals
import ffmpy
import os
from yt_dlp import YoutubeDL

# Download with yt-dl
def downloadVids(downloadLink):
    downloadCmd = f'yt-dlp \'{downloadLink}\' -f \'worst[ext=mp4]\' --output \'%(title)s.%(ext)s\''
    print(downloadLink)
    print(downloadCmd)
    os.system(downloadCmd)

# For converting Scott The Woz seasons/all episodes
def convertWoz(seasonNum, num):
    # Make season-specific folder, else make a folder for all episodes
    if num < 6:
        if not os.path.isdir(f'./iPod Videos/Season {seasonNum}'):
            os.mkdir(f'./iPod Videos/Season {seasonNum}')
        os.chdir(f'./iPod Videos/Season {seasonNum}')
    else:
        if not os.path.isdir('./iPod Videos/Scott The Woz - All Episodes'):
            os.mkdir('./iPod Videos/Scott The Woz - All Episodes')
        os.chdir('./iPod Videos/Scott The Woz - All Episodes')
    seasonLinks = [
        '',
        '\'https://www.youtube.com/watch?v=EjHN3euPI3g&list=PL_tjNJ93e2bCTSQdb6wnDDyX5BAP8quqd\'',
        '\'https://www.youtube.com/playlist?list=PL_tjNJ93e2bDPIPi-H4Fc15Q7c3hkejS8\'',
        '\'https://www.youtube.com/playlist?list=PL_tjNJ93e2bA7LiBhOpcCV83rQ2gilpip\'',
        '\'https://www.youtube.com/playlist?list=PL_tjNJ93e2bDPSmucbq1j0d_SfWFtbGTk\''
        ]
    # Select link for a specific season or all episodes
    if selInt == 6:
        # Link to 'Scott The Woz (All Episodes) playlist'
        downloadLink = '\'https://www.youtube.com/watch?v=EjHN3euPI3g&list=PL_tjNJ93e2bBqjLUxX-zSt7Q4tifigfTD\''
    else:
        downloadLink = seasonLinks[num]
        downloadVids(downloadLink)
    # Convert with ffmpeg via ffmpy
    count = 1
    for filename in os.listdir('.'):
        if (filename.endswith('.mp4')):
            newFilename = filename[:-20]
            ff = ffmpy.FFmpeg(
                inputs={filename: None},
                outputs={f'{str(count)} {newFilename}.mp4': '-s 320x240 -r 24 -b:v 200k -b:a 64k -b:v 128k -bufsize 128k -vcodec libxvid -coder 0 -bf 0 -refs 1'}
                )
            ff.run()
            count += 1
    # Delete unconverted files by looking for 'Woz.mp4' at the end of filenames
        deleteCandidate = filename[:-8:-1]
        if deleteCandidate == '4pm.zoW':
            os.remove(filename)
            print(f'Successfully deleted unconverted file: {filename}')

#-----=====@@@@@=====-----#

# Converting everything else
def convertEverythingElse(isOriginal):
    if isOriginal:
    # Make folder for Originals then cd to it
        if not os.path.isdir(f'./iPod Videos/Scott Wozniak Originals'):
            os.mkdir('./iPod Videos/Scott Wozniak Originals')
        os.chdir('./iPod Videos/Scott Wozniak Originals')
        downloadLink = 'https://www.youtube.com/playlist?list=PL_tjNJ93e2bBwSi0Y4lvxG9tA0SHI-rf8'
    # Non-Originals
    else:
        print(u'\u001b[0mPlease paste the link to the video or playlist you would like to download and convert.')
        downloadLink = input('\n> ')
        # Make folder for vids then cd to it
        if not os.path.isdir('./iPod Videos/Converted Videos'):
            os.mkdir('./iPod Videos/Converted Videos')
        os.chdir('./iPod Videos/Converted Videos')
    downloadVids(downloadLink)
    # Convert with ffmpeg via ffmpy
    for filename in os.listdir('.'):
        if (filename.endswith('.mp4')):
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



# Main menu
if not os.path.isdir(f'./iPod Videos'):
    os.mkdir(f'./iPod Videos')
os.system('echo -n -e \"\033]0;iPod Video Converter\007\"')
os.system('clear')
print(u'\u001b[1mWelcome to \u001b[35mError\u001b[0m \u001b[1mand \u001b[38;5;48mMingus\'\u001b[0m \u001b[1miPod Touch 1G Video Downloader & Converter\u001b[0m\n')
print(u'\u001b[38;5;230mHousekeeping:\u001b[0m This uses ffmpy and yt_dlp. Please make sure you have them installed.')
print(u'              The number in the titles of episodes downloaded by season will be \u001b[1mrelative to the season\u001b[0m, not the entirety of Scott The Woz.\n              If you want these numbers to be realtive to the entirety of Scott The Woz, please use option 6.\n')
print(u'\u001b[1;4m Please select an option:\u001b[0m\n')
print(u'\u001b[38;5;27m[0]\u001b[0m Scott Wozniak Originals')
for i in range(1,5):
    print(u'\u001b[38;5;27m' + f'[{str(i)}]' + u'\u001b[0m' + f' Scott The Woz - Season {str(i)}')
print(u'\u001b[38;5;27m[5]\u001b[0m Scott The Woz - Season 5 \u001b[31m(WARNING: There is not a playlist available for season 5 yet. Selecting this option will close this script.)')
print(u'\u001b[38;5;27m[6]\u001b[0m All Scott The Woz episodes')
print(u'\u001b[38;5;27m[7]\u001b[0m Other')
# Selection vars
selOptions = ['0', '1', '2', '3', '4', '5', '6', '7']
sel = str(input(u'\n> \u001b[1;38;5;27m'))
print(u'\u001b[0m')
selInt = int(sel)

# Temporary until season 5 has a playlist:
if sel == '5':
    print('There is no playlist for season 5 yet! However, this script is set up so it is easy to add the playlist when it\'s ready. \nDue to how this is set up, the script will now close.')
    quit()

# Converting Woz Originals and non-Woz
if sel == selOptions[0]:
    convertEverythingElse(True)
elif sel == selOptions[7]:
    convertEverythingElse(False)
else:
    convertWoz(sel, selInt)
