from PyQt5 import QtCore, QtGui, QtWidgets

def time_calc(minute, i):
    if i == 0: return '0:00'
    else:
        mi = minute * i
        return f'{round(mi // 60)}:{round(mi % 60):0>2}'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(231, 211)
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\언어\\pythun\\동영상 시간 분할기\\split-video-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_video_time = QtWidgets.QLineEdit(self.centralwidget)
        self.input_video_time.setGeometry(QtCore.QRect(110, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.input_video_time.setFont(font)
        self.input_video_time.setText("")
        self.input_video_time.setAlignment(QtCore.Qt.AlignCenter)
        self.input_video_time.setObjectName("input_video_time")
        self.input_split_num = QtWidgets.QLineEdit(self.centralwidget)
        self.input_split_num.setGeometry(QtCore.QRect(110, 50, 111, 31))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.input_split_num.setFont(font)
        self.input_split_num.setMouseTracking(True)
        self.input_split_num.setText("")
        self.input_split_num.setAlignment(QtCore.Qt.AlignCenter)
        self.input_split_num.setObjectName("input_split_num")
        self.video_full_time_text = QtWidgets.QLabel(self.centralwidget)
        self.video_full_time_text.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.video_full_time_text.setFont(font)
        self.video_full_time_text.setAlignment(QtCore.Qt.AlignCenter)
        self.video_full_time_text.setObjectName("video_full_time_text")
        self.split_count_text = QtWidgets.QLabel(self.centralwidget)
        self.split_count_text.setGeometry(QtCore.QRect(10, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.split_count_text.setFont(font)
        self.split_count_text.setAlignment(QtCore.Qt.AlignCenter)
        self.split_count_text.setObjectName("split_count_text")
        self.results = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.results.setGeometry(QtCore.QRect(10, 90, 211, 111))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.results.setFont(font)
        self.results.setReadOnly(True)
        self.results.setObjectName("ex)\nh:mm\nn\nresults")
        self.colons1 = QtWidgets.QLabel(self.centralwidget)
        self.colons1.setGeometry(QtCore.QRect(90, 50, 10, 31))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.colons1.setFont(font)
        self.colons1.setAlignment(QtCore.Qt.AlignCenter)
        self.colons1.setObjectName("colons1")
        self.colons2 = QtWidgets.QLabel(self.centralwidget)
        self.colons2.setGeometry(QtCore.QRect(90, 10, 10, 31))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.colons2.setFont(font)
        self.colons2.setAlignment(QtCore.Qt.AlignCenter)
        self.colons2.setObjectName("colons2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.input_split_num.returnPressed.connect(self.run)
        self.input_video_time.returnPressed.connect(self.run)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Time Divider"))
        self.video_full_time_text.setText(_translate("MainWindow", "총 영상 길이"))
        self.split_count_text.setText(_translate("MainWindow", "나눌 개수"))
        self.results.setPlainText(_translate("MainWindow", "readme - manual\n"
"h:mm\n"
"n\n"
"\n"
"Results"))
        self.colons1.setText(_translate("MainWindow", ":"))
        self.colons2.setText(_translate("MainWindow", ":"))

    def run(self):
            self.results.clear()
            try:
                counter = int(self.input_split_num.text())
                time = self.input_video_time.text()
                hour, minute = map(int, time.split(':'))
                minute = hour * 60 + minute
                temp = minute / counter
                
                for i in range(counter):
                    self.results.appendPlainText(f'{time_calc(temp, i)} ~ {time_calc(temp, i + 1)}')
                return
            except ValueError:
                return self.results.appendPlainText('잘못된 값이 있습니다.')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())