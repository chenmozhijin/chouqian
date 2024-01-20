from PySide6.QtWidgets import QWidget

from ui.about_ui import Ui_about
from ui.chouqian1_ui import Ui_chouqian1
from ui.chouqian2_ui import Ui_chouqian2
from ui.settings_ui import Ui_settings
from ui.statistics_ui import Ui_statistics


class about(QWidget, Ui_about):

    def __init__(self, parent=None):
        super(about, self).__init__(parent)
        self.setupUi(self)


class chouqian1(QWidget, Ui_chouqian1):

    def __init__(self, parent=None):
        super(chouqian1, self).__init__(parent)
        self.setupUi(self)
        # ScrollArea 设置透明背景
        self.ScrollArea.setStyleSheet("background-color: transparent;")


class chouqian2(QWidget, Ui_chouqian2):

    def __init__(self, parent=None):
        super(chouqian2, self).__init__(parent)
        self.setupUi(self)
        # ScrollArea 设置透明背景
        self.ScrollArea.setStyleSheet("background-color: transparent;")


class settings(QWidget, Ui_settings):

    def __init__(self, parent=None):
        super(settings, self).__init__(parent)
        self.setupUi(self)
        # ScrollArea 设置透明背景
        self.ScrollArea.setStyleSheet("background-color: transparent;")


class statistics(QWidget, Ui_statistics):

    def __init__(self, parent=None):
        super(statistics, self).__init__(parent)
        self.setupUi(self)
