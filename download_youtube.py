# importing the module
import argparse
from pytube import YouTube

# TODO change this to dynamically recieve arguments from commandline using argparse
# where to save
SAVE_PATH_VIDEO = "/Users/andrewalseth/Movies" #to_do
SAVE_PATH_AUDIO = "/Users/andrewalseth/Music"

# link of the video to be downloaded
#link="https://www.youtube.com/watch?v=4BOTvaRaDjI"

# audio link
link="https://www.youtube.com/watch?v=-XFJoMRMM4k"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
#mp4files = yt.filter(file_extension='mp4')

#to set the name of the file
#yt.title = 'Foundations 12 minutes')

# get the video with the extension and
# resolution passed in the get() function
#d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)

# downloading the video
# ytstream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
# ytstream.download(output_path=SAVE_PATH_AUDIO)

# downloading audio
print(yt.streams)


# print(yt.streams.filter(250))

# ytstream = yt.streams.filter(only_audio=True).get_highest_resolution()
ytstream = yt.streams.get_by_itag(251)
ytstream.download(output_path=SAVE_PATH_AUDIO)

print('Task Completed!')
