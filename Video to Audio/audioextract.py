#video to mp3 converter

import moviepy.editor

video = moviepy.editor.VideoFileClip("Demo.mp4")

audio = video.audio

audio.write_audiofile("Kesriya tera.mp3")