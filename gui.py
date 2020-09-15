import sys
from logic import prepare_browser, get_translate
from PySide2 import QtWidgets

browser = prepare_browser()


class TranslatorGui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.textEditor = QtWidgets.QTextEdit()
        self.translateButton = QtWidgets.QPushButton(">>")
        self.textBrowser = QtWidgets.QTextBrowser()
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.textEditor)
        self.layout.addWidget(self.translateButton)
        self.layout.addWidget(self.textBrowser)
        self.setLayout(self.layout)
        self.translateButton.clicked.connect(self.translate_text)

    def translate_text(self):
        text = self.textEditor.toPlainText()
        if text == '':
            self.textBrowser.setText('')
            return
        translated_text = get_translate(browser, text)
        self.textBrowser.setText(translated_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = TranslatorGui()
    widget.resize(500, 200)
    widget.show()
    if app.exec_() == 0:
        browser.quit()
        sys.exit()
