# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alex\Desktop\Программирование\Python\Converter\Forms\main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 210)
        MainWindow.setStyleSheet("background-color: rgb(51, 51, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 151, 191))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 131, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ImageConvertRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.ImageConvertRadioButton.setFont(font)
        self.ImageConvertRadioButton.setObjectName("ImageConvertRadioButton")
        self.verticalLayout.addWidget(self.ImageConvertRadioButton)
        self.VideoConvertRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.VideoConvertRadioButton.setFont(font)
        self.VideoConvertRadioButton.setObjectName("VideoConvertRadioButton")
        self.verticalLayout.addWidget(self.VideoConvertRadioButton)
        self.AudioConvertRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.AudioConvertRadioButton.setFont(font)
        self.AudioConvertRadioButton.setObjectName("AudioConvertRadioButton")
        self.verticalLayout.addWidget(self.AudioConvertRadioButton)
        self.VideoToAudioConvertRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.VideoToAudioConvertRadioButton.setFont(font)
        self.VideoToAudioConvertRadioButton.setObjectName("VideoToAudioConvertRadioButton")
        self.verticalLayout.addWidget(self.VideoToAudioConvertRadioButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(170, 10, 521, 191))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_2.setGeometry(QtCore.QRect(90, 58, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 18, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 98, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(90, 98, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(90, 18, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 58, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.ConvertPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.ConvertPushButton.setGeometry(QtCore.QRect(110, 140, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.ConvertPushButton.setFont(font)
        self.ConvertPushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(68, 68, 70);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#989898;\n"
"    color: black;\n"
"}")
        self.ConvertPushButton.setObjectName("ConvertPushButton")
        self.BrowseSourceFilePushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.BrowseSourceFilePushButton.setGeometry(QtCore.QRect(440, 20, 75, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.BrowseSourceFilePushButton.setFont(font)
        self.BrowseSourceFilePushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(68, 68, 70);\n"
"    color: white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#989898;\n"
"    color: black;\n"
"}")
        self.BrowseSourceFilePushButton.setObjectName("BrowseSourceFilePushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Convert"))
        self.ImageConvertRadioButton.setText(_translate("MainWindow", "Image"))
        self.VideoConvertRadioButton.setText(_translate("MainWindow", "Video"))
        self.AudioConvertRadioButton.setText(_translate("MainWindow", "Audio"))
        self.VideoToAudioConvertRadioButton.setText(_translate("MainWindow", "Video to audio"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Convert"))
        self.label.setText(_translate("MainWindow", "Source file"))
        self.label_3.setText(_translate("MainWindow", "Format"))
        self.label_2.setText(_translate("MainWindow", "Output file"))
        self.ConvertPushButton.setText(_translate("MainWindow", "CONVERT"))
        self.BrowseSourceFilePushButton.setText(_translate("MainWindow", "Browse"))

class Converter(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BrowseSourceFilePushButton.clicked.connect(self.openFile)
        self.ConvertPushButton.clicked.connect(self.convertFile)
        self.ImageConvertRadioButton.toggled.connect(lambda: self.btnState(self.ImageConvertRadioButton))
        self.AudioConvertRadioButton.toggled.connect(lambda: self.btnState(self.AudioConvertRadioButton))
        self.VideoConvertRadioButton.toggled.connect(lambda: self.btnState(self.VideoConvertRadioButton))
        self.VideoToAudioConvertRadioButton.toggled.connect(lambda: self.btnState(self.VideoToAudioConvertRadioButton))

    def btnState(self, radioButton):
        self.comboBox.clear()
        if self.ImageConvertRadioButton.isChecked():
            for elem in imageFormats:
                self.comboBox.addItem(elem)
        if self.VideoConvertRadioButton.isChecked():
            for elem in videoFormats:
                self.comboBox.addItem(elem)
        if self.AudioConvertRadioButton.isChecked() or self.VideoToAudioConvertRadioButton.isChecked():
            for elem in audioFormats:
                self.comboBox.addItem(elem)
    
    def openFile(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        sourceFile = ""
        if self.ImageConvertRadioButton.isChecked():
            sourceFile = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "/home", "Images (*.png *.xpm *.jpg *.raw *.cr2 *.nef *.orf *.sr2 *.eps *.gif *.jpg *.jpeg *.bmp *.tif *.tiff)")
        if self.VideoConvertRadioButton.isChecked() or self.VideoToAudioConvertRadioButton.isChecked():
            sourceFile = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "/home", "Videos (*.webm *.mkv *.flv *.flv *.vob *.ogv *.ogg *.drc *.gif *.gifv *.mng *.avi *.MTS *.M2TS *.TS *.mov *.qt *.wmv *.yuv *.rm *.rmvb *.viv *.asf *.amv *.mp4 *.m4p *.m4v *.mpg *.mp2 *.mpeg *.mpe *.mpv *.mpg *.mpeg *.m2v *.m4v *.svi *.3gp *.3g2 *.mxf *.roq *.nsv *.flv *.f4v *.f4p *.f4a *.f4b)")
        if self.AudioConvertRadioButton.isChecked():
            sourceFile = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", "/home", "Audio (*.3gp *.aa *.aac *.aax *.act *.aiff *.alac *.amr *.ape *.au *.awb *.dct *.dss *.dvf *.flac *.gsm *.iklax *.ivs *.m4a *.m4b *.m4p *.mmf *.mp3 *.mpc *.msv *.nmf *.ogg  *.oga  *.mogg *.opus *.ra *.rm *.raw *.rf64 *.sln *.tta *.voc *.vox *.wav *.wma *.wv *.webm *.8svx *.cda)")
        self.textEdit.setText(sourceFile[0])
    
    def convertFile(self):
        file = self.textEdit.toPlainText()
        if self.ImageConvertRadioButton.isChecked():
            from PIL import Image
            img = Image.open(file)

            for elem in imageFormats:
                index = file.find(elem)
                if index != -1:
                    file = file.replace(elem, str(self.comboBox.currentText()))
                    break
            
            img.save(file)
        if self.VideoConvertRadioButton.isChecked():
            import moviepy.editor as mp

            for elem in videoFormats:
                index = file.find(elem)
                if index != -1:
                    clip = mp.VideoFileClip(file)
                    file = file.replace(elem, str(self.comboBox.currentText()))
                    clip.write_videofile(file)
                    break
        if self.VideoToAudioConvertRadioButton.isChecked():
            import moviepy.editor as mp

            for elem in videoFormats:
                index = file.find(elem)
                if index != -1:
                    clip = mp.VideoFileClip(file)
                    file = file.replace(elem, str(self.comboBox.currentText()))
                    clip.audio.write_audiofile(file)
                    break
        if self.AudioConvertRadioButton.isChecked() or self.VideoToAudioConvertRadioButton.isChecked():
            from pydub import AudioSegment
            
            for elem in audioFormats:
                index = file.find(elem)
                if index != -1:
                    audio = AudioSegment.from_file(self.textEdit.toPlainText(), format = elem)          
                    file = file.replace(elem, str(self.comboBox.currentText()))
                    audio.export(file, format = str(self.comboBox.currentText()))
                    break        
        self.textEdit_2.setText(file)

imageFormats = [".png", ".xpm", ".jpg", ".raw", ".cr2", ".nef", ".orf", ".sr2", ".eps", ".gif", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"]
audioFormats = [".3gp", ".aa", ".aac", ".aax", ".act", ".aiff", ".alac", ".amr", ".ape", ".au", ".awb", ".dct", ".dss", ".dvf", ".flac", ".gsm", ".iklax", ".ivs", ".m4a", ".m4b", ".m4p", ".mmf", ".mp3", ".mpc", ".msv", ".nmf", ".ogg ", ".oga ", ".mogg", ".opus", ".ra", ".rm", ".raw", ".rf64", ".sln", ".tta", ".voc", ".vox", ".wav", ".wma", ".wv", ".webm", ".8svx", ".cda"]
videoFormats = [".webm", ".mkv", ".flv", ".flv", ".vob", ".ogv", ".ogg", ".drc", ".gif", ".gifv", ".mng", ".avi", ".MTS", ".M2TS", ".TS", ".mov", ".qt", ".wmv", ".yuv", ".rm", ".rmvb", ".viv", ".asf", ".amv", ".mp4", ".m4p", ".m4v", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".mpg", ".mpeg", ".m2v", ".m4v", ".svi", ".3gp", ".3g2", ".mxf", ".roq", ".nsv", ".flv", ".f4v", ".f4p", ".f4a", ".f4b"]

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Converter()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()