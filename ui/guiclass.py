import sys

import pysrt
from PySide6.QtCore import Qt

import global_obj

import utils

from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QTableWidgetItem, QWidget, QMessageBox

from ui import ui_main, ui_gui, ui_inputdata


class WorkSpaceWindow(QFrame):
    def __init__(self):
        super(WorkSpaceWindow, self).__init__()
        self.ui = ui_gui.Ui_Mainwindow()
        self.ui.setupUi(self)

    def click_refreshBTN(self):
        print("刷新声音")

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
            window1.ui.tableWidget.setCellWidget(row_count, 2, self.button_workspace_for_row(str(row[0])))
            window1.ui.tableWidget.setCellWidget(row_count, 3, self.button_output_for_row(str(row[0])))
            window1.ui.tableWidget.setCellWidget(row_count, 4, self.button_delete_for_row(str(row[0])))

            window1.ui.tableWidget.resizeColumnsToContents()

    def button_workspace_for_row(self, name):
        input_btn = QPushButton('进入')
        input_btn.clicked.connect(lambda: self.to_workspace(name))
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
        is_delete = QMessageBox.question(self, "删除数据集", f"确定删除数据集 {name} ？\n删除后你可以在数据库中手动将其找回", QMessageBox.Yes | QMessageBox.No,
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
