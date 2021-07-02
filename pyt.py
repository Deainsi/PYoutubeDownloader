import urllib

from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube

from ThreadWorker import ThreadWorker


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 50)
        MainWindow.setMinimumSize(QtCore.QSize(540, 71))
        MainWindow.setMaximumSize(QtCore.QSize(1020, 800))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1200, 900))
        self.frame.setMinimumSize(QtCore.QSize(1200, 900))
        self.frame.setMaximumSize(QtCore.QSize(1200, 900))
        self.frame.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 460, 31))
        self.lineEdit.setStyleSheet("border-radius:10px;\n"
                                    "background-color: rgb(90, 90, 90);")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(500, 20, 30, 31))
        self.pushButton.setStyleSheet("QPushButton{background-color: rgb(90,90,90);\n"
                                      "border-radius:15px;\n"
                                      "}\n"
                                      "QPushButton::hover{\n"
                                      "background-color: rgb(70,70,70);\n"
                                      "}\n"
                                      "QPushButton::pressed{\n"
                                      "    background-color: rgb(50, 50, 50);\n"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon("se.png"))
        self.pushButton.clicked.connect(lambda: self.search_url(MainWindow))
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 80, 960, 540))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setVisible(False)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 640, 861, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setVisible(False)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 680, 791, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.setVisible(False)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(910, 640, 80, 31))
        self.comboBox.setStyleSheet("background-color: rgb(60, 60, 60);\n"
                                    "color:rgb(241, 241, 241);\n"
                                    "border-radius:10px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setVisible(False)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 680, 170, 31))
        self.pushButton_2.setStyleSheet("QPushButton{border-radius:10px;\n"
                                        "background-color: rgb(16, 216, 6);\n"
                                        "font: 87 10pt \"Arial\";}\n"
                                        "QPushButton::hover{\n"
                                        "    background-color: rgb(46, 167, 39);\n"
                                        "}\n"
                                        "QPushButton::pressed\n"
                                        "{\n"
                                        "    background-color: rgb(39, 118, 58);\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setVisible(False)
        self.pushButton_2.clicked.connect(self.download)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(30, 720, 960, 31))
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 720, 960, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PytubeDownloader"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Insert video URL"))
        self.pushButton_2.setText(_translate("MainWindow", "Download"))

    def search_url(self, MainWindow):
        url = self.lineEdit.text()
        self.yt = YouTube(url)
        pdata = urllib.request.urlopen(self.yt.thumbnail_url).read()
        qim = QtGui.QImage()
        qim.loadFromData(pdata)
        pixmap = QtGui.QPixmap.fromImage(qim).scaled(960, 540)
        self.label.setPixmap(pixmap)
        self.label_2.setText(self.yt.title)
        self.label_3.setText(self.yt.author)
        self.label_4.setVisible(False)
        yt = self.yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution')
        self.comboBox.clear()
        resoultions = list(set([stream.resolution for stream in yt]))
        resoultions.sort(key=lambda x: int(x[:-1]))
        for resoultion in resoultions:
            self.comboBox.addItem(resoultion)

        if MainWindow.size() == QtCore.QSize(540, 71):
            self.animate(MainWindow)

    def download(self):
        self.progressBar.setValue(0)
        if self.label_4.isVisible():
            self.label_4.setVisible(False)
        self.progressBar.setVisible(True)

        self.thread = ThreadWorker(self.yt, self.comboBox.currentText())
        self.thread.progress.connect(self.downloading)
        self.thread.finished.connect(self.done)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.thread.start()

    def animate(self, MainWindow):
        self.label.setVisible(True)
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.pushButton_2.setVisible(True)
        self.comboBox.setVisible(True)

        self.anim = QtCore.QVariantAnimation()
        self.anim.setStartValue(QtCore.QSize(540, 71))
        self.anim.setEndValue(QtCore.QSize(1020, 800))
        self.anim.setDuration(500)
        self.anim.valueChanged.connect(MainWindow.setMinimumSize)

        self.anim1 = QtCore.QVariantAnimation()
        self.anim1.setStartValue(QtCore.QRect(20, 20, 460, 31))
        self.anim1.setEndValue(QtCore.QRect(265, 20, 460, 31))
        self.anim1.setDuration(500)
        self.anim1.valueChanged.connect(self.lineEdit.setGeometry)

        self.anim2 = QtCore.QVariantAnimation()
        self.anim2.setStartValue(QtCore.QRect(500, 20, 30, 31))
        self.anim2.setEndValue(QtCore.QRect(765, 20, 30, 31))
        self.anim2.setDuration(500)
        self.anim2.valueChanged.connect(self.pushButton.setGeometry)

        self.ag = QtCore.QParallelAnimationGroup()
        self.ag.addAnimation(self.anim)
        self.ag.addAnimation(self.anim1)
        self.ag.addAnimation(self.anim2)
        self.ag.start()

    def downloading(self, stream, chunk, remaining):
        fs = self.yt.streams.filter(file_extension='mp4', progressive=True).get_by_resolution(
            self.comboBox.currentText()).filesize
        self.progressBar.setValue(int((fs - remaining) / fs * 100))

    def done(self, stream, filepath):
        self.progressBar.setVisible(False)
        self.label_4.setVisible(True)
        self.label_4.setText(f"Download complete. Video can be found at {filepath}")
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
