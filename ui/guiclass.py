import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFrame

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

    def to_outputfile(self):
        print("前往导出数据集窗口")

    def to_workspace(self):
        print("前往数据标注窗口")


class InputDataWindow(QMainWindow):
    def __init__(self):
        super(InputDataWindow, self).__init__()
        self.ui = ui_inputdata.Ui_MainWindow()
        self.ui.setupUi(self)

    def double_clicked_file(self, a, b):
        print(f"导入文件 {a} {b}")

    def back_to_main(self):
        print(f"返回首页")


if __name__ == '__main__':
    app = QApplication([])
    window1 = MainWindow()
    window2 = WorkSpaceWindow()
    window3 = InputDataWindow()
    window1.show()
    window2.show()
    window3.show()

    sys.exit(app.exec())
