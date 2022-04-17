from pydub.playback import play

from utils import AllSound, MySound

jr1_allsound = AllSound("./filepath/jr1.wav")
info_dict ={
    "text":"你好",
    "start":10500,
    "end":13700,
    "checked":0,
    "can_use":0,
    "file_name":"jr1.wav",
    "all_sound":jr1_allsound.sound
}

short_sound = MySound(info_dict)
print(len(short_sound.sound))
play(short_sound.sound)
