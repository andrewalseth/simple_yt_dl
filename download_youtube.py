# importing the module
import argparse
from pytube import YouTube

# TODO change this to dynamically recieve arguments from commandline using argparse
# where to save
SAVE_PATH = "/Users/andrewalseth/Movies" #to_do

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=4BOTvaRaDjI"

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
ytstream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
ytstream.download(output_path=SAVE_PATH)

print('Task Completed!')
