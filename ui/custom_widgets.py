from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor, QTextDocument
from PySide6.QtWidgets import QTextEdit


class TextLineEdit(QTextEdit):
    topMarginCorrection = -4  # not sure why needed
    returnPressed = Signal()

    def __init__(self, parent=None, fontSize: int = 10, verticalMargin=20):
        QTextEdit.__init__(self, parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setLineWrapMode(QTextEdit.NoWrap)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTextColor(QColor(0, 0, 0))
        self.setFontPointSize(fontSize)
        self.setViewportMargins(
            -verticalMargin, self.topMarginCorrection, 0, 0,
        )  # left, top, right, bottom
        # Set up document with appropriate margins and font
        # 设置光标为指针
        

        self.document = QTextDocument()
        current_font = self.currentFont()
        current_font.setPointSize(fontSize)
        self.document.setDefaultFont(current_font)
        self.document.setDocumentMargin(verticalMargin)
        self.setFixedHeight(self.document.size().height())
        self.setDocument(self.document)

        self.setLineWrapMode(QTextEdit.WidgetWidth)

        self.setStyleSheet("""QTextEdit {
                                background-color: transparent;
                                border: none;
                                font-size: 30px;
                                text-align: center;
                                color: black;
                            }""")
        self.setCursor(Qt.ArrowCursor)

    def insertPlainText(self, text: str) -> None:
        super().insertPlainText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedHeight(self.document.size().height())

    def setPlainText(self, text: str) -> None:
        super().setPlainText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedHeight(self.document.size().height())

    def keyPressEvent(self, event) -> None:
        """stops retun from returning newline"""
        if event.key() in (Qt.Key_Enter, Qt.Key_Return):
            self.returnPressed.emit()
            event.accept()
        else:
            QTextEdit.keyPressEvent(self, event)
