import sys

from PySide6.QtWidgets import QApplication

import global_obj
from ui import guiclass
from utils import dictdir, LiteDB
from threading import Thread


def main():
    global_obj._init()

    db_path = "db/data.db"
    file_dict_path = "filepath/"
    sound_type = ["wav", "mp3", "aac"]

    # 读取文件路径
    srt_file_dict = {}
    file_dict = {}
    dictdir(file_dict_path, srt_file_dict, "srt")
    dictdir(file_dict_path, file_dict, "")
    global sound_dict
    sound_dict = get_sound_dict(srt_file_dict, file_dict, sound_type)
    print(sound_dict)
    db = LiteDB()
    global_obj.set_value("sound_dict", sound_dict)
    global_obj.set_value("db", db)

    # sqlite的对象不能在别的线程里用，先不用了
    # gui_thread = Thread(target=guiclass.main)
    # gui_thread.start()
    # gui_thread.join()
    guiclass.main()
    print("GUI已关闭")
    db.close()




def get_sound_dict(srt_file_dict, file_dict, sound_type):
    sound_dict = {}
    for srt_file in srt_file_dict.keys():
        sound_path = ""
        for type in sound_type:
            sound_file = srt_file.replace(".srt", "." + type)
            # print(sound_file)
            if sound_file in file_dict:
                sound_path = file_dict[sound_file]
                break
        sound_dict[srt_file.replace(".srt", "")] = (srt_file_dict[srt_file], sound_path)
    return sound_dict


if __name__ == '__main__':
    main()
