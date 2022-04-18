import os
import sqlite3

from pydub import AudioSegment
import time


class LiteDB:
    def __init__(self, dbpath='db/data.db'):
        self.conn = sqlite3.connect(dbpath)
        print("数据库打开成功")

    def close(self):
        self.conn.close()
        print("数据库已关闭")

    def create_sound_table(self, sound_name):
        c = self.conn.cursor()
        c.execute(f'''CREATE TABLE "{sound_name}" (
            "sound_id" integer NOT NULL,
            "sound_text" TEXT NOT NULL,
            "sound_start" integer NOT NULL,
            "sound_end" integer NOT NULL,
            "checked" TEXT NOT NULL DEFAULT 0,
            "can_use" integer NOT NULL DEFAULT 1,
            "sound_file_path" TEXT NOT NULL,
            PRIMARY KEY ("sound_id"));''')
        print(f"数据表 {sound_name} 创建成功")
        self.conn.commit()

    def delete_sound_table(self, sound_name):
        c = self.conn.cursor()
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        print(f'''ALTER TABLE {sound_name} RENAME TO {'_' + sound_name + '_' + now_time};''')
        c.execute(f'''ALTER TABLE {sound_name} RENAME TO {'_' + sound_name + '_' + now_time};''')
        print(f"数据表 {sound_name} 被改名为 {'_' + sound_name + '_' + now_time}")
        self.conn.commit()

    def select_all(self):
        c = self.conn.cursor()
        result = c.execute("select * from sound")
        return result

    def select_unchecked(self):
        c = self.conn.cursor()
        result = c.execute("SELECT sound_text,sound_start,sound_end,checked,can_use FROM sound")
        return result

    def select_tables_list(self):
        c = self.conn.cursor()
        result = c.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        result_list = []
        for row in result:
            result_list.append(row[0])
        return result_list

    def select_sound_path(self, name):
        """ 根据sound name（即表名）搜索音频文件位置 """
        c = self.conn.cursor()
        result = c.execute(f"SELECT sound_file_path FROM {name} limit 1")
        result_list = []
        for row in result:
            return row[0]


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

class MySRT:
    def __init__(self, file_path):
        pass


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


if __name__ == "__main__":
    db1 = LiteDB()
    print(db1.select_tables_list())
