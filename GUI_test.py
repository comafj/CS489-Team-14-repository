import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QLabel, QTextEdit, QHBoxLayout,\
    QVBoxLayout, QSlider, QRadioButton, QTextBrowser
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, Qt
import main as ma


class Result_window(QWidget):
    def __init__(self, title, body, comments):
        super().__init__()
        self.initUI(title, body, comments)

    def initUI(self, title, body, comments):
        self.setWindowTitle('RESULT')
        self.setWindowIcon(QIcon('web.png'))
        self.resize(1200, 675)

        myFont = QFont()
        myFont.setBold(True)

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont('Arial', 20))
        self.textname = QLabel('News text')
        self.textname.setFont(myFont)
        self.text = QTextBrowser(self)
        self.text.append(body)

        self.commentname = QLabel('Top 3 Comments')
        self.commentname.setFont(myFont)
        self.comment1 = QTextBrowser(self)
        self.comment1.append(comments[0][0])
        self.comment1.setFixedWidth(800)
        self.comment1.setFixedHeight(80)
        self.like1 = QLabel(str(comments[0][1]))
        self.like1.setAlignment(Qt.AlignCenter)
        self.disl1 = QLabel(str(comments[0][2]))
        self.disl1.setAlignment(Qt.AlignCenter)
        self.repl1 = QLabel(str(comments[0][3]))
        self.repl1.setAlignment(Qt.AlignCenter)
        comment1_info = QHBoxLayout()
        comment1_info.addWidget(self.comment1)
        comment1_info.addWidget(self.like1)
        comment1_info.addWidget(self.disl1)
        comment1_info.addWidget(self.repl1)

        self.comment2 = QTextBrowser(self)
        self.comment2.append(comments[1][0])
        self.comment2.setFixedWidth(800)
        self.comment2.setFixedHeight(80)
        self.like2 = QLabel(str(comments[1][1]))
        self.like2.setAlignment(Qt.AlignCenter)
        self.disl2 = QLabel(str(comments[1][2]))
        self.disl2.setAlignment(Qt.AlignCenter)
        self.repl2 = QLabel(str(comments[1][3]))
        self.repl2.setAlignment(Qt.AlignCenter)
        comment2_info = QHBoxLayout()
        comment2_info.addWidget(self.comment2)
        comment2_info.addWidget(self.like2)
        comment2_info.addWidget(self.disl2)
        comment2_info.addWidget(self.repl2)

        self.comment3 = QTextBrowser(self)
        self.comment3.append(comments[2][0])
        self.comment3.setFixedWidth(800)
        self.comment3.setFixedHeight(80)
        self.like3 = QLabel(str(comments[2][1]))
        self.like3.setAlignment(Qt.AlignCenter)
        self.disl3 = QLabel(str(comments[2][2]))
        self.disl3.setAlignment(Qt.AlignCenter)
        self.repl3 = QLabel(str(comments[2][3]))
        self.repl3.setAlignment(Qt.AlignCenter)
        comment3_info = QHBoxLayout()
        comment3_info.addWidget(self.comment3)
        comment3_info.addWidget(self.like3)
        comment3_info.addWidget(self.disl3)
        comment3_info.addWidget(self.repl3)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title)
        vbox.addWidget(self.textname)
        vbox.addWidget(self.text)
        vbox.addWidget(self.commentname)
        vbox.addLayout(comment1_info)
        vbox.addLayout(comment2_info)
        vbox.addLayout(comment3_info)
        self.setLayout(vbox)


class MyApp(QWidget):
    def analysis(self):
        self.URL = self.te.toPlainText()
        self.st1 = self.slider1.value()
        self.st2 = self.slider2.value()
        self.st3 = self.slider3.value()
        self.st4 = self.slider4.value()
        self.k = 1
        if self.rbtn2.isChecked():
            self.k = 0
        elif self.rbtn3.isChecked():
            self.k = -1

        title, article, result = ma.main(self.URL, self.st1, self.st2, self.st3, self.st4, self.k)
        self.second = Result_window(title, article, result)
        self.second.show()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.lbl1 = QLabel('Enter Naver News Link')
        self.lbl1.setFont(QFont('Arial', 15))
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.te.setFixedHeight(100)
        self.start = QPushButton('Start', self)
        self.start.clicked.connect(self.analysis)
        self.exit = QPushButton('Exit', self)
        self.exit.setToolTip('This is a Exit button, please click this if you want to close')
        self.exit.clicked.connect(QCoreApplication.instance().quit)
        self.lbl2 = QLabel('Set your standards')
        self.lbl2.setFont(QFont('Arial', 15))

        self.lbl3 = QLabel('Reply')
        self.lbl3.setMargin(20)
        self.lbl3.setFixedWidth(150)
        self.slider1 = QSlider(Qt.Horizontal, self)
        self.slider1.setMaximum(10)
        self.slider1.setMinimum(1)
        self.slider1.setSingleStep(1)
        self.slider1.setValue(1)
        self.replyval = QLabel()
        self.replyval.setMargin(20)
        self.slider1.valueChanged.connect(self.replyval.setNum)

        self.lbl4 = QLabel('Like / Dislike')
        self.lbl4.setMargin(20)
        self.lbl4.setFixedWidth(150)
        self.slider2 = QSlider(Qt.Horizontal, self)
        self.slider2.setMaximum(10)
        self.slider2.setMinimum(1)
        self.slider2.setSingleStep(1)
        self.slider2.setValue(1)
        self.likeval = QLabel()
        self.likeval.setMargin(20)
        self.slider2.valueChanged.connect(self.likeval.setNum)

        self.rbtn1 = QRadioButton('LIKE + DISLIKE', self)
        self.rbtn1.setChecked(True)
        self.rbtn2 = QRadioButton('ONLY LIKE', self)
        self.rbtn3 = QRadioButton('LIKE - DISLIKE')

        self.lbl5 = QLabel('Keyword')
        self.lbl5.setMargin(20)
        self.lbl5.setFixedWidth(150)
        self.slider3 = QSlider(Qt.Horizontal, self)
        self.slider3.setMaximum(10)
        self.slider3.setMinimum(1)
        self.slider3.setSingleStep(1)
        self.slider3.setValue(1)
        self.keyval = QLabel()
        self.keyval.setMargin(20)
        self.slider3.valueChanged.connect(self.keyval.setNum)

        self.lbl6 = QLabel('Similarity')
        self.lbl6.setMargin(20)
        self.lbl6.setFixedWidth(150)
        self.slider4 = QSlider(Qt.Horizontal, self)
        self.slider4.setMaximum(10)
        self.slider4.setMinimum(1)
        self.slider4.setSingleStep(1)
        self.slider4.setValue(1)
        self.simval = QLabel()
        self.simval.setMargin(20)
        self.slider4.valueChanged.connect(self.simval.setNum)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.start)
        hbox.addWidget(self.exit)
        hbox.addStretch(1)

        labelbox1 = QHBoxLayout()
        labelbox1.addWidget(self.lbl3)
        labelbox1.addWidget(self.slider1)
        labelbox1.addWidget(self.replyval)
        labelbox2 = QHBoxLayout()
        labelbox2.addWidget(self.lbl4)
        labelbox2.addWidget(self.slider2)
        labelbox2.addWidget(self.likeval)
        labelbox3 = QHBoxLayout()
        labelbox3.addWidget(self.lbl5)
        labelbox3.addWidget(self.slider3)
        labelbox3.addWidget(self.keyval)
        labelbox4 = QHBoxLayout()
        labelbox4.addWidget(self.lbl6)
        labelbox4.addWidget(self.slider4)
        labelbox4.addWidget(self.simval)

        radiobox = QHBoxLayout()
        radiobox.addStretch(1)
        radiobox.addWidget(self.rbtn1)
        radiobox.addWidget(self.rbtn2)
        radiobox.addWidget(self.rbtn3)
        radiobox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addLayout(labelbox1)
        vbox.addLayout(labelbox2)
        vbox.addLayout(radiobox)
        vbox.addLayout(labelbox3)
        vbox.addLayout(labelbox4)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setWindowTitle('NCA - News Comment Analyzer')
        self.setWindowIcon(QIcon('web.png'))
        self.resize(1200, 675)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())