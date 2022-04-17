import sqlite3

from pydub import AudioSegment

db_path = "db/data.db"
file_dict_path = "filepath/"


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
        self.sound = cut_sound(info_dict["all_sound"],self.start,self.end)


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
