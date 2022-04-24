import sys
import time
from threading import Thread
from time import sleep

import pysrt
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from pydub import AudioSegment
from pydub.playback import play

import global_obj

import utils

from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QTableWidgetItem, QWidget, QMessageBox, \
    QButtonGroup

from ui import ui_main, ui_gui, ui_inputdata, ui_wait


class WorkSpaceWindow(QFrame):
    def __init__(self):
        super(WorkSpaceWindow, self).__init__()
        self.ui = ui_gui.Ui_Mainwindow()
        self.ui.setupUi(self)
        self.work_space_data = None
        self.ui.tableWidget.setRowHeight(1, 10)
        font1 = QFont()
        font1.setPointSize(10)
        self.ui.tableWidget.setFont(font1)
        self.btn_group = QButtonGroup(self.ui.groupBox_2)
        self.btn_group.addButton(self.ui.radioButton, 0)
        self.btn_group.addButton(self.ui.radioButton_2, 1)

    def click_refreshBTN(self):
        """ 点击刷新数据列表按钮后触发的槽函数 """
        print("刷新表格")
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_4.setText("请稍等")
        self.ui.pushButton_4.style()
        self.refresh_data(self.work_space_data.name)
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_4.setText("刷新数据列表")
        self.ui.pushButton_4.style()

    def click_play_soundBTN(self):
        """ 点击播放音频后触发的槽函数 """
        print("播放声音")

        play_thread = Thread(target=self.play_sound)
        play_thread.start()
        # play_thread.join()  # 多线程 永远的神 不加界面就阻塞了

    def play_sound(self):
        """" 播放音频 同时检查是不是正常的数字 """
        try:
            start = int(self.ui.lineEdit_2.text())
            end = int(self.ui.lineEdit_3.text())
        except:
            print("请输入以毫秒为单位的纯数字")
        else:
            play(self.work_space_data.sound[start:end])

    def click_backBTN(self):
        print(f"返回上一个声音 序号{self.work_space_data.now_sound_index - 1}")
        self.goto_sound(self.work_space_data.now_sound_index - 1)  # 进行一个代码的复用

    def click_nextBTN(self):
        print(f"继续下一个声音 序号{self.work_space_data.now_sound_index + 1}")
        self.goto_sound(self.work_space_data.now_sound_index + 1)  # 进行一个代码的复用

    def click_checkBTN(self):
        """ 将本条信息标注，修改数据库的内容且将状态切换为已标注 """
        print("确定本条声音")
        db = global_obj.get_value("db")
        index = self.work_space_data.now_sound_index
        now_sound_info = self.work_space_data.sound_list[index]
        now_sound_info.text = self.ui.lineEdit.text()
        now_sound_info.start = self.ui.lineEdit_2.text()
        now_sound_info.end = self.ui.lineEdit_3.text()
        now_sound_info.checked = 1
        if self.btn_group.checkedId() == -1:
            now_sound_info.can_use = 1
        else:
            now_sound_info.can_use = self.btn_group.checkedId()
        db.update_sound(now_sound_info, self.work_space_data.name)
        self.refresh_table_line()
        if self.ui.checkBox_2.isChecked():
            if self.ui.tableWidget.rowCount() - 1 != self.work_space_data.now_sound_index:
                self.click_nextBTN()

    def refresh_table_line(self):
        """ 刷新表格中的一条数据的信息，从数据库中取值，但不改变表格中的跳转按钮状态 """
        # 试图用子线程给界面加元素，但是加的所有widget及其子类都被添加到新窗口里了，加不到老窗口里，故作罢
        index = self.work_space_data.now_sound_index
        now_sound_info = self.work_space_data.sound_list[index]
        db = global_obj.get_value("db")
        select_sound_info = db.select_dataset_row(self.work_space_data.name, now_sound_info.id)
        item_text1 = "已标注"
        if select_sound_info[4] == 0:
            item_text1 = "未标注"
        item_text2 = "可用"
        if select_sound_info[5] == 0:
            item_text2 = "不可用"
        self.ui.tableWidget.item(self.work_space_data.now_sound_index, 0).setText(select_sound_info[1])
        self.ui.tableWidget.item(self.work_space_data.now_sound_index, 1).setText(item_text1)
        self.ui.tableWidget.item(self.work_space_data.now_sound_index, 2).setText(item_text2)
        self.ui.tableWidget.resizeColumnsToContents()  # 表格列宽自动调整

    def refresh_data(self, name):
        """ 刷新表格信息 """
        # 清空表格
        while self.ui.tableWidget.rowCount() != 0:
            self.ui.tableWidget.removeRow(0)
        db = global_obj.get_value("db")
        path = db.select_sound_path(name)
        self.work_space_data = utils.WorkSpaceData(name, path)
        i = 0
        for sound_obj in self.work_space_data.sound_list:
            self.sound_obj_to_row(sound_obj, i)
            i = i + 1  # 半自动经典for循环 index不好用
        self.refresh_now_sound()
        self.ui.tableWidget.resizeColumnsToContents()  # 表格列宽自动调整

    def sound_obj_to_row(self, sound_obj, sound_id):
        """ 传入一个sound_obj，给表格中加一行 """
        # sound_obj = utils.MySound()
        row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_count)
        item1 = QTableWidgetItem()
        item1.setText(sound_obj.text)
        item1.setFlags(Qt.ItemIsEnabled)  # 禁止编辑

        item2 = QTableWidgetItem()
        item_text1 = "已标注"
        if sound_obj.checked == 0:
            item_text1 = "未标注"
        item2.setText(item_text1)
        item2.setFlags(Qt.ItemIsEnabled)

        item3 = QTableWidgetItem()
        item_text2 = "可用"
        if sound_obj.can_use == 0:
            item_text2 = "不可用"
        item3.setText(item_text2)
        item3.setFlags(Qt.ItemIsEnabled)

        self.ui.tableWidget.setItem(row_count, 0, item1)
        self.ui.tableWidget.setItem(row_count, 1, item2)
        self.ui.tableWidget.setItem(row_count, 2, item3)
        self.ui.tableWidget.setCellWidget(row_count, 3, self.button_goto_for_row(sound_id))

    def button_goto_for_row(self, sound_id):
        """ 返回一个用于跳转到对应音频信息的btn """
        input_btn = QPushButton('跳转')
        input_btn.clicked.connect(lambda: self.goto_sound(sound_id))  # 不那么复杂的参数传递
        if self.work_space_data.now_sound_index == sound_id:
            input_btn.setEnabled(False)
        return input_btn

    def goto_sound(self, sound_id):
        """ 表格中的跳转按钮点击后对应的槽函数 """
        old_id = self.work_space_data.now_sound_index
        self.work_space_data.now_sound_index = sound_id
        self.refresh_now_sound()
        self.refresh_table_gotoBTN(old_id, sound_id)
        self.ui.tableWidget.selectRow(sound_id)  # 如果不加这个会导致点击按钮后选中按钮下一行的第一个单元格，猜测原因是本应选中按钮，但是按钮被置灰光标自动后移
        if self.ui.checkBox.isChecked():
            self.click_play_soundBTN()  # 灵活运用槽

    def refresh_table_gotoBTN(self, old_id, new_id):
        """ 用于刷新表格中的跳转按钮状态"""
        self.ui.tableWidget.cellWidget(old_id, 3).setEnabled(True)
        self.ui.tableWidget.cellWidget(new_id, 3).setEnabled(False)

    def refresh_now_sound(self):
        """ 更新当前页面中的音频信息，不改变表格中的按钮状态 """
        index = self.work_space_data.now_sound_index
        now_sound_info = self.work_space_data.sound_list[index]
        print(f"现在的音频信息为：{now_sound_info.text}")
        self.ui.lineEdit_2.setText(str(now_sound_info.start))
        self.ui.lineEdit_3.setText(str(now_sound_info.end))
        self.ui.lineEdit.setText(now_sound_info.text)
        self.ui.label_5.setText(f"当前编号：{index + 1}")
        if now_sound_info.can_use == 0:
            self.ui.radioButton.setChecked(True)
        elif now_sound_info.can_use == 1:
            self.ui.radioButton_2.setChecked(True)

        # 刷新上一条下一条按钮状态
        if self.ui.tableWidget.rowCount() - 1 == self.work_space_data.now_sound_index:
            self.ui.pushButton_2.setEnabled(False)
        else:
            self.ui.pushButton_2.setEnabled(True)

        if self.work_space_data.now_sound_index == 0:
            self.ui.pushButton.setEnabled(False)
        else:
            self.ui.pushButton.setEnabled(True)

    def click_output_now(self):
        """ 导出当前的音频文件，如果不指定则导出到filepath/output下,命名为数据集名+日期 """
        # 不知为何 槽函数接收到信号的时候顺便还接收到了一个参数 值为false 但是我不知道这个false是哪来的
        path = "filepath/output"
        path = path.replace("\\", "/")
        if not path.endswith("/"):
            path = path + "/"
        utils.check_mkdir(path)
        try:
            start = int(self.ui.lineEdit_2.text())
            end = int(self.ui.lineEdit_3.text())
        except:
            print("请输入以毫秒为单位的纯数字")
        else:
            out_sound = self.work_space_data.sound[start:end]
            out_sound = out_sound.set_frame_rate(16000).set_channels(1)  # 设置为16k采样率，单声道
            out_sound.export(
                path + self.work_space_data.name + '_' + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + ".wav",
                format="wav", bitrate="16k", codec='pcm_s16le')
        print("导出当前文件为:" + path + self.work_space_data.name + '_' + time.strftime("%Y_%m_%d_%H_%M_%S",
                                                                                  time.localtime()) + ".wav")

    def click_back_to_main(self):
        """ 返回首页窗口 """
        window2.close()
        window1.show()
        # 清空表格，节约内存 节省了10m不到的内存 没意义
        # window2.work_space_data = None
        # while window2.ui.tableWidget.rowCount() != 0:
        #     window2.ui.tableWidget.removeRow(0)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)

    def to_inputfile(self):
        print("前往导入文件窗口")
        window1.close()
        window3.refresh_data()
        window3.show()

    def to_outputfile(self, name):
        """
        根据数据集名导出数据集，导出的路径为filepath/output/数据集名_日期时间/
        音频路径为data/wav/数据集名_编号.wav
        文本路径为data/trans/sample.txt
        """
        print(f"导出数据集{name}")
        path = "filepath/output"
        path = path.replace("\\", "/")
        if not path.endswith("/"):
            path = path + "/"
        path = path + name + '_' + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + "/"
        utils.check_mkdir(path + "data/wav/")
        utils.check_mkdir(path + "data/trans/")
        db = global_obj.get_value("db")
        result_dict = db.select_output_data(name)
        # print(result_dict)
        try:
            all_sound = AudioSegment.from_file(result_dict["path"]).set_channels(1)
        except:
            print(f"{result_dict['path']} 文件未找到，无法导出数据集")

        i = 0
        write_str = ""
        for row in result_dict["data_list"]:
            i = i + 1
            all_sound[row[1]:row[2]].export(path + "data/wav/" + f"{name}_" + str(i) + ".wav", format="wav",
                                            # bitrate="16k",
                                            codec='pcm_s16le')
            write_str = write_str + f"{name}_" + str(i) + ".wav" + "\t" + row[0] + "\n"

        with open(path + "data/trans/sample.txt", "a", encoding="UTF-8") as f:
            f.write(write_str)
        is_delete = QMessageBox.information(self, "导出完成", f"导出数据集{name}成功\n请前往 {path} 查看",
                                            QMessageBox.Yes, QMessageBox.Yes)
        print(f"导出数据集{name}成功")

    def to_workspace(self, name):
        print(f"前往数据标注窗口 {name}")
        window1.close()
        # window4.ui.label_2.setText("加载中，请稍等...")  # 很奇怪 这个窗口里的东西都加载不出来
        window4.show()
        window2.refresh_data(name)
        window4.close()
        window2.show()

    def refresh_data(self):
        self.table_refresh()

    def table_refresh(self):
        # 清空表格
        while window1.ui.tableWidget.rowCount() != 0:
            window1.ui.tableWidget.removeRow(0)

        for row in self.get_row_info():
            row_count = window1.ui.tableWidget.rowCount()
            window1.ui.tableWidget.insertRow(row_count)

            item1 = QTableWidgetItem()
            item1.setText(row[0])
            item1.setFlags(Qt.ItemIsEnabled)

            item2 = QTableWidgetItem()
            item2.setText(row[1])
            item2.setFlags(Qt.ItemIsEnabled)

            window1.ui.tableWidget.setItem(row_count, 0, item1)
            window1.ui.tableWidget.setItem(row_count, 1, item2)
            window1.ui.tableWidget.setCellWidget(row_count, 2, self.button_workspace_for_row(str(row[0]), str(row[1])))
            window1.ui.tableWidget.setCellWidget(row_count, 3, self.button_output_for_row(str(row[0]), str(row[1])))
            window1.ui.tableWidget.setCellWidget(row_count, 4, self.button_delete_for_row(str(row[0])))

            window1.ui.tableWidget.resizeColumnsToContents()  # 表格列宽自动调整

    def button_workspace_for_row(self, name, path):
        input_btn = QPushButton('进入')
        input_btn.clicked.connect(lambda: self.to_workspace(name))
        if not utils.is_sound_file_ok(path):
            input_btn.setEnabled(False)
            input_btn.setText("音频缺失")

        return input_btn

    def button_delete_for_row(self, name):
        input_btn = QPushButton('删除')
        input_btn.clicked.connect(lambda: self.is_delete_box(name))
        return input_btn

    def button_output_for_row(self, name, path):
        input_btn = QPushButton('导出数据集')
        input_btn.clicked.connect(lambda: self.to_outputfile(name))
        if not utils.is_sound_file_ok(path):
            input_btn.setEnabled(False)
            input_btn.setText("音频缺失")
        return input_btn

    def get_row_info(self):
        db = global_obj.get_value("db")
        row_info = []
        tables_list = db.select_tables_list()
        for table in tables_list:
            if table.startswith("_"):
                continue
            file_path = db.select_sound_path(table)
            row_info.append([table, file_path])
        return row_info

    def is_delete_box(self, name):
        # 看来不是这么改的
        # yes_btn = QMessageBox.Yes
        # yes_btn.setText("是")
        # no_btn = QMessageBox.No
        # no_btn.setText("否")
        is_delete = QMessageBox.question(self, "删除数据集", f"确定删除数据集 {name} ？\n删除后你可以在数据库中手动将其找回",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
        if is_delete == QMessageBox.Yes:
            self.delete_table(name)

    def delete_table(self, name):
        db = global_obj.get_value("db")
        db.delete_sound_table(name)
        self.table_refresh()


class InputDataWindow(QMainWindow):
    def __init__(self):
        super(InputDataWindow, self).__init__()
        self.ui = ui_inputdata.Ui_MainWindow()
        self.ui.setupUi(self)

    def refresh_data(self):
        sound_dict = global_obj.get_value("sound_dict")
        tables_list = global_obj.get_value("db").select_tables_list()

        # 清空表格
        while window3.ui.dataTableWidget.rowCount() != 0:
            window3.ui.dataTableWidget.removeRow(0)

        for key in sound_dict.keys():
            # print(key)
            if sound_dict[key][0] == "" or sound_dict[key][1] == "":
                continue
            if sound_dict[key][1].count("/output/") != 0:
                continue
            row_count = window3.ui.dataTableWidget.rowCount()
            window3.ui.dataTableWidget.insertRow(row_count)
            item1 = QTableWidgetItem()
            item1.setText(key)
            item1.setFlags(Qt.ItemIsEnabled)
            item2 = QTableWidgetItem()
            item2.setText(sound_dict[key][0] + "," + sound_dict[key][1])
            item2.setFlags(Qt.ItemIsEnabled)

            window3.ui.dataTableWidget.setItem(row_count, 0, item1)
            window3.ui.dataTableWidget.setItem(row_count, 1, item2)
            window3.ui.dataTableWidget.setCellWidget(row_count, 2, self.button_for_row(str(key), tables_list))
            window3.ui.dataTableWidget.resizeColumnsToContents()  # 宽高自适应

    def input_file(self, name, input_btn):
        print(f"导入文件 {name}")
        db = global_obj.get_value("db")
        db.create_sound_table(name)
        file_path = global_obj.get_value("sound_dict")[name]
        mysrt = pysrt.open(file_path[0])
        input_list = []
        for part in mysrt:
            input_list.append([part.text, part.start.ordinal, part.end.ordinal])
        db.insert_sound_line(input_list, file_path[1], name)
        if db.select_tables_list().count(name) != 0:
            input_btn.setEnabled(False)
            input_btn.setText("已导入")

    def double_clicked_file(self, a):
        print(f"导入文件 {a}")

    def back_to_main(self):
        print(f"返回首页")
        window3.close()
        window1.refresh_data()
        window1.show()

    def button_for_row(self, name, tables_list):
        if tables_list.count(name) == 0:
            input_btn = QPushButton('导入')
            input_btn.clicked.connect(lambda: self.input_file(name, input_btn))
        else:
            input_btn = QPushButton('已导入')
            input_btn.clicked.connect(lambda: self.input_file(name, input_btn))
            input_btn.setEnabled(False)
        return input_btn


class WaitWindow(QFrame):  # 注意这里要写QFrame 具体请看QT设计师里的父窗口类名
    def __init__(self):
        super(WaitWindow, self).__init__()
        self.ui = ui_wait.Ui_widget()
        self.ui.setupUi(self)


def main():
    app = QApplication([])

    # coder 不怎么机灵
    global window1
    global window2
    global window3
    global window4
    window1 = MainWindow()
    window1.refresh_data()
    window2 = WorkSpaceWindow()
    window3 = InputDataWindow()
    window4 = WaitWindow()
    window1.show()
    # window4.show()

    app.exec()
    # sys.exit(app.exec())


if __name__ == '__main__':
    main()
