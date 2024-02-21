# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Copyright (c) 2024 沉默の金
import json
import os
import random
import resource.resource_rc as rc
import sys
import time

import requests
from PySide6.QtCore import (
    QDate,
    QDateTime,
    QObject,
    QSharedMemory,
    Qt,
    QThread,
    QTime,
    QUrl,
    Signal,
    Slot,
)
from PySide6.QtGui import (
    QAction,
    QColor,
    QDesktopServices,
    QFont,
    QGuiApplication,
    QIcon,
    QPainter,
    QTextCursor,
)
from PySide6.QtNetwork import QLocalServer, QLocalSocket
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QSystemTrayIcon,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from data import Data
from icon import Icon
from qfluentwidgets import (
    FluentIcon,
    InfoBar,
    InfoBarIcon,
    InfoBarPosition,
    MSFluentWindow,
    NavigationItemPosition,
    PushButton,
    RoundMenu,
    SplashScreen,
)
from ui.Interface import about, chouqian1, chouqian2, settings, statistics

__version__ = "v2.2"


class MainWindow(MSFluentWindow):

    def __init__(self):
        super().__init__()
        self.resize(700, 560)
        self.setMinimumWidth(540)
        self.setWindowTitle('抽签')
        self.setWindowIcon(QIcon(':/chouqian/icon/logo.png'))

        self.splashScreen = SplashScreen(self.windowIcon(), self)

        self.chouqian1_in_progress = False
        self.chouqian2_in_progress = False
        self.checkupdate_in_progress = False

    def closeEvent(self, event):
        # 隐藏窗口而不是关闭,使其最小化到托盘
        self.hide()
        event.ignore()

    @Slot()
    def show_window(self) -> None:
        # 显示窗口
        self.show()
        if self.isMinimized():
            self.showNormal()
        self.raise_()
        self.activateWindow

    def AddSubInterface(self):
        self.chouqian1 = chouqian1(self)
        self.chouqian2 = chouqian2(self)
        self.statistics = statistics(self)
        self.settings = settings(self)
        self.about = about(self)

        self.addSubInterface(self.chouqian1, Icon.PERSON, '随机姓名', position=NavigationItemPosition.TOP)
        self.addSubInterface(self.chouqian2, FluentIcon.PEOPLE, '随机小组', position=NavigationItemPosition.TOP)
        self.addSubInterface(self.statistics, FluentIcon.PIE_SINGLE, '统计', position=NavigationItemPosition.TOP)
        self.addSubInterface(self.settings, FluentIcon.SETTING, '设置', position=NavigationItemPosition.BOTTOM)
        self.addSubInterface(self.about, FluentIcon.INFO, '关于', position=NavigationItemPosition.BOTTOM)

    def init_input(self):
        self.settings.SwitchButton.setChecked(data.cfg["draw_animation"])  # 抽签动画
        self.settings.SwitchButton_2.setChecked(data.cfg["reduce_duplication"])  # 减少重复
        self.settings.SpinBox.setValue(data.cfg["groups_count"])  # 组的数量
        self.settings.SpinBox.setMinimum(1)

        self.settings.ComboBox.clear()
        self.settings.ComboBox.addItems(data.list_names)
        if data.cfg["default_list"]:
            self.settings.ComboBox.setCurrentIndex(data.list_names.index(data.cfg["default_list"]))

        self.chouqian1.ComboBox.clear()
        self.chouqian1.ComboBox.addItems(data.list_names)
        if data.cfg["default_list"]:
            self.chouqian1.ComboBox.setCurrentIndex(data.list_names.index(data.cfg["default_list"]))

        self.statistics.ComboBox.clear()
        self.statistics.ComboBox.addItems(data.list_names)
        self.statistics.ComboBox.addItem("小组抽签")
        if data.cfg["default_list"]:
            self.statistics.ComboBox.setCurrentIndex(data.list_names.index(data.cfg["default_list"]))

    def Connect_signals_and_slot_functions(self):
        self.stackedWidget.currentChanged.connect(self.change_sub_interface)  # 检查界面切换
        self.settings.PushButton.clicked.connect(load_config)
        self.settings.SwitchButton.checkedChanged.connect(lambda: data.write_settings("draw_animation", self.settings.SwitchButton.indicator.isChecked()))  # 抽签动画
        self.settings.SwitchButton_2.checkedChanged.connect(lambda: data.write_settings("reduce_duplication", self.settings.SwitchButton_2.indicator.isChecked()))  # 减少重复
        self.settings.SpinBox.valueChanged.connect(self.change_groups_count)  # 组的数量
        self.settings.ComboBox.currentIndexChanged.connect(lambda: data.write_settings("default_list", self.settings.ComboBox.currentText()))  # 默认列表

        self.chouqian1.Slider.valueChanged.connect(lambda: self.change_chouqian_count("Slider", self.chouqian1))
        self.chouqian1.PillPushButton.clicked.connect(lambda: self.change_chouqian_count("-", self.chouqian1))
        self.chouqian1.PillPushButton_2.clicked.connect(lambda: self.change_chouqian_count("+", self.chouqian1))
        self.chouqian1.ComboBox.currentIndexChanged.connect(self.init_chouqian)
        self.chouqian1.PushButton.clicked.connect(lambda: self.chouqian_start(1))

        self.chouqian2.Slider.valueChanged.connect(lambda: self.change_chouqian_count("Slider", self.chouqian2))
        self.chouqian2.PillPushButton.clicked.connect(lambda: self.change_chouqian_count("-", self.chouqian2))
        self.chouqian2.PillPushButton_2.clicked.connect(lambda: self.change_chouqian_count("+", self.chouqian2))
        self.chouqian2.PushButton.clicked.connect(lambda: self.chouqian_start(2))

        self.statistics.CalendarPicker.dateChanged.connect(lambda: self.change_date("start_time"))
        self.statistics.CalendarPicker_2.dateChanged.connect(lambda: self.change_date("end_time"))
        self.statistics.ComboBox.currentIndexChanged.connect(self.SetUpStatisticsTable)
        self.statistics.PushButton.clicked.connect(self.resetdate)

        self.about.PrimaryPushButton.clicked.connect(lambda: QDesktopServices.openUrl(QUrl('https://github.com/chenmozhijin/chouqian')))
        self.about.PrimaryPushButton_2.clicked.connect(lambda: self.check_update(False))
        self.about.PrimaryPushButton_3.clicked.connect(lambda: QDesktopServices.openUrl(QUrl('https://github.com/chenmozhijin/chouqian/issues')))

    def init_chouqian(self):
        list_name = self.chouqian1.ComboBox.currentText()
        list_data = data.read_list(list_name)
        list_count = len(list_data)
        self.chouqian1.Slider.setMinimum(1)
        self.chouqian1.Slider.setMaximum(list_count)
        self.chouqian1.Slider.setValue(1)

        self.chouqian2.Slider.setMinimum(1)
        self.chouqian2.Slider.setMaximum(data.cfg["groups_count"])
        self.chouqian2.Slider.setValue(1)

        font = QFont()
        font.setPointSize(30)
        self.chouqian1.chouqian_textEdit.setFont(font)
        self.chouqian2.chouqian_textEdit.setFont(font)

    @Slot()
    def change_groups_count(self):
        data.write_settings("groups_count", int(self.settings.SpinBox.text()))
        data.del_group_record()
        self.chouqian2.Slider.setMaximum(data.cfg["groups_count"])

    @Slot()
    def change_date(self, type_):
        start_time = self.statistics.CalendarPicker.getDate()
        end_time = self.statistics.CalendarPicker_2.getDate()
        start_timestamp = qdate_to_unix_timestamp(start_time)
        end_timestamp = qdate_to_unix_timestamp(end_time)
        if type_ == "start_time" and start_timestamp > end_timestamp:
            self.statistics.CalendarPicker_2.setDate(start_time)
        elif type_ == "end_time" and start_timestamp > end_timestamp:
            self.statistics.CalendarPicker.setDate(end_time)
        self.SetUpStatisticsTable()

    @Slot()
    def resetdate(self):
        date = QDate()
        cp1 = self.statistics.CalendarPicker
        cp2 = self.statistics.CalendarPicker_2
        for cp in [cp1, cp2]:
            cp.setDate(date)
            cp.setText(self.tr('选择一个日期'))
            cp.setProperty('hasDate', False)
            cp.setStyle(QApplication.style())
            cp.update()

    @Slot()
    def chouqian_start(self, type_):
        if type_ == 1:
            if self.chouqian1_in_progress:
                return
            self.chouqian1_in_progress = True
            chouqian_TextEdit = self.chouqian1.chouqian_textEdit
            chouqian_count = self.chouqian1.Slider.value()
            list_name = self.chouqian1.ComboBox.currentText()
            list_data = data.read_list(list_name)
            list_count = len(list_data)
        elif type_ == 2:
            if self.chouqian2_in_progress:
                return
            self.chouqian2_in_progress = True
            chouqian_TextEdit = self.chouqian2.chouqian_textEdit
            chouqian_count = self.chouqian2.Slider.value()
            list_name = "小组抽签"
            list_data = []
            for i in range(1, data.cfg["groups_count"] + 1):
                list_data.append("第" + str(i) + "组")
            list_count = len(list_data)

        chouqian_results = SystemRandom.sample(list_data, chouqian_count)
        if self.settings.SwitchButton_2.indicator.isChecked():
            n = list_count // 2
            if n < chouqian_count:
                n = list_count - chouqian_count
            last_records = data.read_last_records(list_name, n)
            # 替换结果中在last_records的
            for index, item in enumerate(chouqian_results):
                if item in last_records:
                    while True:
                        new_result = random.sample(list_data, 1)[0]
                        if new_result not in last_records and new_result not in chouqian_results[:index] + chouqian_results[index + 1:]:
                            chouqian_results[index] = new_result
                            break
        chouqian_TextEdit.setPlainText("")
        if self.settings.SwitchButton.indicator.isChecked():  # 抽签动画
            if chouqian_count == 1:
                animation_count = 5
                sleeptime = 0.08
            elif chouqian_count < 5:
                animation_count = 5
                sleeptime = 0.06
            elif chouqian_count < 10:
                animation_count = 5
                sleeptime = 0.05
            elif chouqian_count < 25:
                animation_count = 4
                sleeptime = 0.03
            elif chouqian_count < 50:
                animation_count = 3
                sleeptime = 0.02
            elif chouqian_count < 100:
                animation_count = 2
                sleeptime = 0.01
            elif chouqian_count < 300:
                animation_count = 1
                sleeptime = 0.005
            else:
                animation_count = 0
                sleeptime = 0

            if animation_count > list_count:
                animation_count = list_count

            def del_text(n: int) -> None:
                cursor = chouqian_TextEdit.textCursor()
                cursor.movePosition(QTextCursor.End)
                cursor.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor, n)
                cursor.removeSelectedText()
                cursor.movePosition(QTextCursor.End)

            space = ""
            for chouqian_result in chouqian_results:
                for _i in range(animation_count):
                    animation_text = space + random.choice(list_data)  # noqa: S311
                    chouqian_TextEdit.insertPlainText(animation_text)
                    QApplication.processEvents()
                    del_text(len(animation_text))
                chouqian_TextEdit.insertPlainText(space + chouqian_result)
                QApplication.processEvents()
                time.sleep(sleeptime)
                space = " "
        else:
            chouqian_TextEdit.setPlainText(" ".join(chouqian_results))
        for chouqian_result in chouqian_results:
            data.write_record(list_name, chouqian_result, int(time.time()))

        if type_ == 1:
            self.chouqian1_in_progress = False
        elif type_ == 2:
            self.chouqian2_in_progress = False

    def SetUpStatisticsTable(self) -> None:
        local_timezone_offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
        start_time = qdate_to_unix_timestamp(self.statistics.CalendarPicker.getDate())
        end_time = qdate_to_unix_timestamp(self.statistics.CalendarPicker_2.getDate())
        if start_time != 0:
            start_time += local_timezone_offset
        if end_time != 0:
            end_time = end_time + local_timezone_offset + 86400
        statistics_data = data.read_records(self.statistics.ComboBox.currentText(), start_time, end_time)
        statistics_data = sorted(statistics_data.items(), key=lambda x: x[1]['count'], reverse=True)
        table = self.statistics.TableWidget
        table.setRowCount(len(statistics_data))
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(['名称', '次数', '爆率', '上次被抽到的时间'])
        row, total = 0, 0
        total = sum(value[1]['count'] for value in statistics_data)
        for key, value in statistics_data:
            # key 为人名 value["count"] 为次数 value["last_time"]为时间
            if value["last_time"]:
                last_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(value["last_time"] - local_timezone_offset))
            else:
                last_time = "从未被抽中"
            rate = round(value["count"] / total * 100, 3) if total != 0 else 0

            table.setItem(row, 0, QTableWidgetItem(str(key)))
            table.setItem(row, 1, QTableWidgetItem(str(value["count"])))
            table.setItem(row, 2, QTableWidgetItem(str(rate) + "%"))
            table.setItem(row, 3, QTableWidgetItem(last_time))
            row += 1
        table.resizeColumnsToContents()

    @Slot()
    def change_chouqian_count(self, input_, Interface):
        if input_ == "Slider":
            Interface.CaptionLabel.setText(str(Interface.Slider.value()))
        elif input_ == "+":
            Interface.Slider.setValue(Interface.Slider.value() + 1)
            Interface.CaptionLabel.setText(str(Interface.Slider.value()))
        elif input_ == "-":
            Interface.Slider.setValue(Interface.Slider.value() - 1)
            Interface.CaptionLabel.setText(str(Interface.Slider.value()))

    @Slot()
    def change_sub_interface(self):
        interface = self.stackedWidget.currentWidget().objectName()
        if interface == "statistics":
            self.SetUpStatisticsTable()

    def createInfoBar(self, type_, title, content, duration) -> None:
        if type_ == "error":
            infobar = InfoBar.error
        elif type_ == "success":
            infobar = InfoBar.success
        elif type_ == "warning":
            infobar = InfoBar.warning
        elif type_ == "info":
            infobar = InfoBar.info
        infobar(
            title=title,
            content=content,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=duration,
            parent=self
        )

    def check_update(self, IsAuto) -> None:
        if not self.checkupdate_in_progress:
            self.checkupdate_in_progress = True
            # 为更新检查创建一个新的工作实例
            self.update_checker = UpdateChecker(github_repo="chenmozhijin/chouqian", IsAuto=IsAuto)
            self.update_checker_thread = QThread()
            self.update_checker.update_finished.connect(self.handle_check_update_result)
            self.update_checker_thread.started.connect(self.update_checker.run_update)
            self.update_checker.moveToThread(self.update_checker_thread)

            # 启动检查更新线程
            self.update_checker_thread.start()

    def handle_check_update_result(self, success, latest_version, IsAuto) -> None:
        self.update_checker_thread.quit()
        if success:
            if latest_version != __version__:
                infobar = InfoBar(
                    icon=InfoBarIcon.INFORMATION,
                    title='有新版本',
                    content=latest_version,
                    orient=Qt.Horizontal,
                    isClosable=True,
                    position=InfoBarPosition.TOP_RIGHT,
                    duration=5000,
                    parent=self,
                )
                Button = PushButton(MW.tr('前往更新'))
                Button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl(f"https://github.com/{self.update_checker.github_repo}/releases/latest")))
                infobar.addWidget(Button)
                infobar.show()
            elif not IsAuto:
                self.createInfoBar("info", "当前已是最新版本", "", 5000)
        elif not IsAuto:
            self.createInfoBar("error", "检查更新失败", latest_version, 5000)
        self.checkupdate_in_progress = False


class FloatingWindow(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        screen_geometry = QGuiApplication.primaryScreen().availableGeometry()
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口属性为支持半透明背景
        self.setFixedSize(10, 20)  # 设置悬浮窗固定大小
        self.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.move(screen_geometry.right() - self.width() / 2 - 5, screen_geometry.center().y() - self.height() / 2 - 250)  # 将窗口移动到屏幕右边框中部
        self.draggable = False

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # 去除布局的外边距
        self.label = QLabel("抽", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0);")  # 设置标签背景颜色为透明
        layout.addWidget(self.label)
        self.setLayout(layout)

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.LeftButton:
            self.draggable = True
            self.offset = event.position()

            MW.show_window()

    def mouseReleaseEvent(self, event) -> None:
        self.draggable = False

    def mouseMoveEvent(self, event) -> None:
        if self.draggable:
            new_pos = self.mapToParent(event.position() - self.offset).toPoint()
            self.move(new_pos)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(255, 255, 255, 100))


class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.init_ui()

    def init_ui(self) -> None:
        # 创建托盘图标
        tray_icon = QIcon(':/chouqian/icon/logo.png')
        self.setIcon(tray_icon)

        # 创建托盘菜单
        tray_menu = RoundMenu()
        action_show = QAction('显示', self)
        action_exit = QAction('退出', self)

        # 添加菜单项的槽函数
        action_show.triggered.connect(MW.show_window)
        action_exit.triggered.connect(exit_program)

        # 将菜单项添加到托盘菜单
        tray_menu.addAction(action_show)
        tray_menu.addAction(action_exit)

        # 将菜单设置为托盘图标的菜单
        self.setContextMenu(tray_menu)

        # 设置点击托盘图标时显示窗口
        self.activated.connect(MW.show_window)

        # 显示托盘图标
        self.show()


def qdate_to_unix_timestamp(qdate):
    qdatetime = QDateTime(qdate, QTime(0, 0), Qt.UTC)
    return qdatetime.toSecsSinceEpoch()


def load_config() -> None:
    config_path, _ = QFileDialog.getOpenFileName(filter="抽签配置文件 (*.cqp)")
    if not config_path:
        return

    with open(config_path, encoding='utf-8') as file:
        try:
            config = json.load(file)
        except json.JSONDecodeError as e:
            MW.createInfoBar("error", "错误", f"配置文件无法解析。错误信息：{e}", -1)
            return

    if not all(key in config for key in ["version", "settings", "lists"]) or not all(key in config["settings"] for key in data.cfg_keys):
        MW.createInfoBar("error", "错误", "不支持的配置文件", -1)
        return

    lists = config["lists"]
    version = config["version"]

    if version > data.db_version:
        MW.createInfoBar("error", "错误", "不支持的配置文件。", -1)
        return

    for key, value in lists.items():
        if not isinstance(key, str) or not isinstance(value, list):
            MW.createInfoBar("error", "错误", "列表格式错误。", -1)
            return
        elif len(value) == 0:
            MW.createInfoBar("error", "错误", "存在空列表", -1)
            return
        elif key == "小组抽签":
            MW.createInfoBar("error", "错误", "列表名不能为小组抽签", -1)
            return
        for item in value:
            if not isinstance(item, str):
                MW.createInfoBar("error", "错误", "列表项格式错误。", -1)
                return

    for key, value in config["settings"].items():
        if key not in data.cfg_keys or (key in data.cfg_boolkeys and not isinstance(value, bool)) or (key in data.cfg_intkeys and not isinstance(value, int)) or (key in data.cfg_strkeys and not isinstance(value, str)):
            MW.createInfoBar("error", "错误", "设置项错误。", -1)
            return

    if config["settings"]["default_list"] not in lists:
        MW.createInfoBar("error", "错误", "默认列表不存在。", -1)
        return

    data.write_lists(lists)
    for key, value in config["settings"].items():
        data.write_settings(key, value)
    data.del_group_record()
    MW.init_input()
    MW.init_chouqian()
    MW.createInfoBar("success", "成功", "配置文件已成功导入。", 5000)


class UpdateChecker(QObject):
    update_finished = Signal(bool, str, bool)

    def __init__(self, github_repo, IsAuto) -> None:
        super().__init__()
        self.github_repo = github_repo
        self.IsAuto = IsAuto

    def run_update(self) -> None:
        try:
            latest_release = requests.get(f"https://api.github.com/repos/{self.github_repo}/releases/latest", timeout=5).json()
        except Exception as e:
            self.update_finished.emit(False, str(e), self.IsAuto)
        else:
            if "tag_name" in latest_release:
                latest_version = latest_release["tag_name"]
                self.update_finished.emit(True, latest_version, self.IsAuto)
            else:
                self.update_finished.emit(False, "无法获取最新版本信息。", self.IsAuto)


class HandleInstanceRepeatedRuns(QObject):
    AnotherInstanceStarts = Signal()

    def __init__(self):
        super().__init__()
        self.shared_memory = QSharedMemory(self)
        self.shared_memory.setKey("chenmozhijinChouQianAppKey")

        self.local_server = QLocalServer(self)
        self.local_server.newConnection.connect(self.handleNewConnection)

        if self.isRunning():
            self.sendSignal()
            sys.exit(0)
        else:
            self.startLocalServer()

    def isRunning(self):
        if self.shared_memory.attach():
            return True
        if not self.shared_memory.create(1):
            return True
        return False

    def startLocalServer(self):
        self.local_server.listen("chenmozhijinChouQianAppLocalServer")

    def sendSignal(self):
        socket = QLocalSocket(self)
        socket.connectToServer("chenmozhijinChouQianAppLocalServer")
        if socket.waitForConnected(1000):
            socket.write(b"Activate")
            socket.waitForBytesWritten(1000)
            socket.disconnectFromServer()

    def handleNewConnection(self):
        socket = self.local_server.nextPendingConnection()
        if socket:
            socket.readyRead.connect(self.handleReadyRead)
            socket.disconnected.connect(socket.deleteLater)

    def handleReadyRead(self):
        socket = self.sender()
        if socket.bytesAvailable():
            data = socket.readAll()
            if data == b"Activate":
                self.AnotherInstanceStarts.emit()
                print("Received activation signal.")


def exit_program():
    if HandleInstanceRepeatedRunsThread.isRunning():
        HandleInstanceRepeatedRunsThread.quit()
    if MW.update_checker_thread.isRunning():
        MW.update_checker_thread.quit()
    HandleInstanceRepeatedRuns.deleteLater()
    sys.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    HandleInstanceRepeatedRuns = HandleInstanceRepeatedRuns()
    HandleInstanceRepeatedRunsThread = QThread()
    HandleInstanceRepeatedRuns.moveToThread(HandleInstanceRepeatedRunsThread)
    HandleInstanceRepeatedRunsThread.start()

    rc.qInitResources()

    MW = MainWindow()
    HandleInstanceRepeatedRuns.AnotherInstanceStarts.connect(MW.show_window)

    MW.show()
    QApplication.processEvents()
    MW.AddSubInterface()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    data = Data(current_directory)
    SystemRandom = random.SystemRandom()
    MW.init_input()
    MW.init_chouqian()
    MW.Connect_signals_and_slot_functions()
    MW.about.BodyLabel_2.setText('版本：' + __version__)
    floating_window = FloatingWindow()
    floating_window.show()
    tray_icon = TrayIcon()
    tray_icon.show()
    QApplication.processEvents()
    MW.splashScreen.finish()
    if not data.list_names:
        MW.createInfoBar("warning", "注意", "没有可用的数据，请前往设置导入", 5000)
    MW.check_update(True)

    sys.exit(app.exec())
