import os
import sqlite3

from pydub import AudioSegment



class LiteDB:
    def __init__(self):
        self.conn = sqlite3.connect('db/data.db')
        print("数据库打开成功")

    def close(self):
        self.conn.close()

    def select_all(self):
        c = self.conn.cursor()
        result = c.execute("select * from sound")
        return result

    def select_unchecked(self):
        c = self.conn.cursor()
        result = c.execute("SELECT sound_text,sound_start,sound_end,checked,can_use FROM sound")
        return result


class MySound:
    def __init__(self, info_dict):
        self.text = info_dict["text"]
        self.start = info_dict["start"]
        self.end = info_dict["end"]
        self.checked = info_dict["checked"]
        self.can_use = info_dict["can_use"]
        self.file_name = info_dict["file_name"]
        self.sound = cut_sound(info_dict["all_sound"], self.start, self.end)


class AllSound:
    def __init__(self, file_path):
        self.sound = get_sound(file_path)


def get_sound(file_path):
    file_type = file_path.split(".")[-1:][0]
    if file_type == "mp3":
        return AudioSegment.from_mp3(file_path)
    elif file_type == "wav":
        return AudioSegment.from_wav(file_path)


def cut_sound(sound, start, end):
    return sound[start:end]


def listdir(path, list_name, file_end=""):  # 传入存储的list
    """
    将目录下的文件名读存储在list中
    :param file_end:
    :param path:
    :param list_name:
    :return:
    """
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            if file_path.endswith(file_end):
                if file_path.find(".DS_Store") != -1:
                    continue
                list_name.append(file_path.replace("\\", "/"))

def dictdir(path, dict_name, file_end=""):  # 传入存储的dict
    """
    将目录下的文件名读存储在list中
    :param file_end:
    :param path:
    :param dict_name:
    :return:
    """
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            dictdir(file_path, dict_name)
        else:
            if file_path.endswith(file_end):
                if file_path.find(".DS_Store") != -1:
                    continue
                dict_name[file_path.replace("\\", "/").split("/")[-1]] = file_path.replace("\\", "/")