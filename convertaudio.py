import os
from os import path
import ffmpeg



def convert_audio(audiofile, fformat):
            
    out = os.path.dirname(audiofile)+'/'+os.path.splitext(os.path.basename(audiofile))[0] + f".{fformat}"
    os.system(f"ffmpeg -i {audiofile} {out}")
            
    
        
        
        
if __name__ == '__main__':
    
    audpath = "C:/Users/Hloni/Documents/Podcast/Recruiting2021/PodcastSession.wav"
    
    convert_audio(audpath,"mp3")
