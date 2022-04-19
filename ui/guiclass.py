import sys

import pysrt
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

import global_obj

import utils

from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QTableWidgetItem, QWidget, QMessageBox

from ui import ui_main, ui_gui, ui_inputdata


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

    def click_refreshBTN(self):
        print("刷新表格")

    def click_play_soundBTN(self):
        print("播放声音")

    def click_backBTN(self):
        print("返回上一个声音")

    def click_nextBTN(self):
        print("继续下一个声音")

    def click_checkBTN(self):
        print("确定本条声音")

    def click_table(self, a):
        print(f"表格单元格被双击 {a.text()}")

    def refresh_data(self, name):
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

    def sound_obj_to_row(self, sound_obj, sound_id):
        # sound_obj = utils.MySound()
        row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_count)
        item1 = QTableWidgetItem()
        item1.setText(sound_obj.text)
        item1.setFlags(Qt.ItemIsEnabled)  # 禁止编辑

        item2 = QTableWidgetItem()
        item_text1 = "已标注"
        print(type(sound_obj.checked))
        if sound_obj.checked == "0":
            btn_text1 = "未标注"
        item2.setText(item_text1)
        item2.setFlags(Qt.ItemIsEnabled)

        item3 = QTableWidgetItem()
        item_text2 = "可用"
        if sound_obj.checked == "0":
            item_text2 = "不可用"
        item3.setText(item_text2)
        item3.setFlags(Qt.ItemIsEnabled)

        self.ui.tableWidget.setItem(row_count, 0, item1)
        self.ui.tableWidget.setItem(row_count, 1, item2)
        self.ui.tableWidget.setItem(row_count, 2, item3)
        self.ui.tableWidget.setCellWidget(row_count, 3, self.button_goto_for_row(sound_id))

        self.ui.tableWidget.resizeColumnsToContents()  # 表格列宽自动调整

    def button_goto_for_row(self, sound_id):
        input_btn = QPushButton('跳转')
        input_btn.clicked.connect(lambda: self.goto_sound(sound_id, input_btn))  # 复杂的参数传递
        if self.work_space_data.now_sound_index == sound_id:
            input_btn.setEnabled(False)
        return input_btn

    def goto_sound(self, sound_id, input_btn):
        # print(self.ui.tableWidget.cellWidget(sound_id, 3).text())
        # self.ui.tableWidget.cellWidget(sound_id, 3).setEnabled(True)  # 写代码写出了幻觉
        self.ui.tableWidget.cellWidget(self.work_space_data.now_sound_index, 3).setEnabled(True)
        self.work_space_data.now_sound_index = sound_id
        self.refresh_now_sound()
        # print("解锁按钮")
        input_btn.setEnabled(False)
        self.ui.tableWidget.selectRow(sound_id)  # 如果不加这个会导致点击按钮后选中按钮下一行的第一个单元格，猜测原因是本应选中按钮，但是按钮被置灰光标自动后移

    def refresh_now_sound(self):
        index = self.work_space_data.now_sound_index
        now_sound_info = self.work_space_data.sound_list[index]
        print(f"现在的音频信息为：{now_sound_info.text}")

        pass


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
        print(f"导出数据集{name}")

    def to_workspace(self, name):
        print(f"前往数据标注窗口 {name}")
        window1.close()
        window2.refresh_data(name)
        window2.show()

    def refresh_data(self):
        self.table_refresh()
        pass

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
            window1.ui.tableWidget.setCellWidget(row_count, 3, self.button_output_for_row(str(row[0])))
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

    def button_output_for_row(self, name):
        input_btn = QPushButton('导出数据集')
        input_btn.clicked.connect(lambda: self.to_outputfile(name))
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


def main():
    app = QApplication([])

    # coder 不怎么机灵
    global window1
    global window2
    global window3
    window1 = MainWindow()
    window1.refresh_data()
    window2 = WorkSpaceWindow()
    window3 = InputDataWindow()
    window1.show()

    app.exec()
    # sys.exit(app.exec())


if __name__ == '__main__':
    main()
