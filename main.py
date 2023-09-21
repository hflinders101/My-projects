from pytube import YouTube
import os

yt = YouTube(
    str(input("Put the link here:"))
)

video = yt.streams.filter(only_audio=True).first()

destination=r"C:\Users\hflin\Downloads"

#download the file
out_file= video.download(output_path=destination)

#save the file
base, ext= os.path.splitext(out_file)
print(base)
print(ext)
new_file = base + ".mp3"
os.rename(out_file, new_file)

print(yt.title +"has been downloaded")