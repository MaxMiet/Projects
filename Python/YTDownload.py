import os
from pytube import YouTube

link = input('Paste the link: ')

def Download():
    url = YouTube(str(link))
    video = url.streams.get_highest_resolution()
    user = os.getenv('username')
    video.download('C:/Users/' + str(user) + '/Downloads')


Ask = input('Start download Y/N?: ')
if Ask == 'y' or Ask == 'Y':
    Download()
    input('Download complete, press Enter to close.')
elif Ask == 'n' or Ask == 'N':
    print('Exiting...')
    exit()

