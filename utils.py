import os
import sqlite3

from pydub import AudioSegment
import time

import global_obj


class LiteDB:
    def __init__(self, dbpath='db/data.db'):
        check_mkdir("db")
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
            "checked" integer NOT NULL DEFAULT 0,
            "can_use" integer NOT NULL DEFAULT 1,
            "sound_file_path" TEXT NOT NULL,
            PRIMARY KEY ("sound_id"));''')
        print(f"数据表 {sound_name} 创建成功")
        self.conn.commit()

    def delete_sound_table(self, sound_name):
        c = self.conn.cursor()
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
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
        """ 搜索都有什么表 """
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

    def select_dataset_data(self, name, num=4):
        """ 搜索某个数据集里的全部信息 """
        c = self.conn.cursor()
        # result = c.execute(f"SELECT ROW_NUMBER() OVER(ORDER BY sound_start ASC)-1 AS xuhao ,sound_text,sound_start,sound_end,checked,can_use FROM {name} ORDER BY sound_start ASC")
        result = c.execute(
            f"SELECT sound_id,sound_text,sound_start,sound_end,checked,can_use FROM {name} WHERE LENGTH(sound_text)>{num} ORDER BY sound_start ASC")
        return list(result)

    def select_dataset_row(self, name, id, num=4):
        """ 搜索数据集里的其中一条数据 """
        c = self.conn.cursor()
        result = c.execute(
            f"SELECT sound_id,sound_text,sound_start,sound_end,checked,can_use FROM {name} WHERE sound_id = {id}")
        return list(result)[0]

    def select_output_data(self, name, num=4):
        """ 搜索指定数据集要导出的数据 """
        result_dict = {}
        c = self.conn.cursor()
        result = c.execute(
            f"SELECT sound_text,sound_start,sound_end FROM {name} WHERE LENGTH(sound_text)>{num} AND checked=1 AND can_use=1 ORDER BY sound_start ASC")
        result_dict["data_list"] = list(result)
        result_dict["path"] = list(c.execute(f"SELECT sound_file_path FROM {name} limit 1"))[0][0]  # 顺序很重要
        return result_dict

    def insert_sound_line(self, input_list, path, name):
        """ 新增一条语音记录 """
        c = self.conn.cursor()
        for row in input_list:
            c.execute(
                f"INSERT INTO {name}(sound_text, sound_start, sound_end, sound_file_path) VALUES ('{row[0]}', {row[1]}, {row[2]}, '{path}')")
        self.conn.commit()
        print("数据插入成功")

    def update_sound(self, sound_obj, name):
        """ 更新标注信息 """
        c = self.conn.cursor()
        c.execute(
            f"UPDATE {name} SET sound_text = '{sound_obj.text}', sound_start = {sound_obj.start}, sound_end = {sound_obj.end}, checked = {sound_obj.checked}, can_use = {sound_obj.can_use} WHERE sound_id = {sound_obj.id}")
        self.conn.commit()
        print(f"数据 {sound_obj.text} 更新成功")


class MySound:
    def __init__(self, info_list):
        self.id = info_list[0]
        self.text = info_list[1]
        self.start = info_list[2]
        self.end = info_list[3]
        self.checked = info_list[4]
        self.can_use = info_list[5]


class WorkSpaceData:
    def __init__(self, name, path):
        self.name = name
        self.sound_list = []
        self.refresh_sound_list()
        self.sound_path = path
        self.sound = AudioSegment.from_file(path)
        self.now_sound_index = 0

    def refresh_sound_list(self):
        db = global_obj.get_value("db")
        sound_list = []
        for row in db.select_dataset_data(self.name):
            sound_list.append(MySound(row))
        self.sound_list = sound_list
        print("数据集信息已更新")


# class MySRT:
#     def __init__(self, file_path):
#         self.srt_path = file_path
#         self.srt_list = []
#         srt_text = file_r(file_path)
#         srt_row = []
#         for line in srt_text.split("\n"):
#             print(line)
#         pass


# def get_sound(file_path):
#     file_type = file_path.split(".")[-1:][0]
#     if file_type == "mp3":
#         return AudioSegment.from_mp3(file_path)
#     elif file_type == "wav":
#         return AudioSegment.from_wav(file_path)


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
    :param path:
    :param dict_name:
    :param file_end:
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


def file_r(path):
    with open(path, 'r', encoding="UTF-8") as f:
        return f.read()


def is_sound_file_ok(path):
    is_ok = False
    try:
        AudioSegment.from_file(path)
    except:
        print(f"{path} 文件未找到，无法进入数据集")
    else:
        is_ok = True
    return is_ok


def check_mkdir(path):
    """ 检查一个目录是否存在，不存在则新建 """
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == "__main__":
    pass
