##this script will rename the default name for the videos
##downloaded for all playlist using megavn.com
import os
import re

os.chdir('path to text file')
#ff file contains youtube playlist content from the playlist page.
file=open('playlist_content.txt','r').read()
b=file.split('\n')
##dic to hold number and its title.
dd={}
i=0
while(i<len(b)-4):
    dd[b[i]]=b[i+3]
    i=i+5

##another dic for name edit. can be avoided.
dd1={}
for k,v in dd.items():
    dd1[k]=' '.join(v.split(' ')[4:])


os.chdir('path to playlist videos')		#contains video want to rename
b1=os.listdir()
def atoi(text):
    return int(text) if text.isdigit() else text
	
def natural_keys(text):
	return [ atoi(c) for c in re.split('(\d+)', text) ]

b1.sort(key=natural_keys)		#this one sort the video name having(string_number)
##this will loop through the dictionary and rename the files.
for i in b1:
    nm=i.split('_')[1].split('.')[0]
    if nm in dd1.keys():
        os.rename(i,nm+' '+dd1[nm]+'.mp4')
