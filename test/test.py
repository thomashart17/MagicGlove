"""
import os

file = "audiofile.mp3"
os.system("mpg123 " + file)

"""

from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("audiofile.mp3")
play(song)

