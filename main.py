import sys

from PySide6 import QtMultimedia
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, QUrl, Qt, QTimer)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon,
                           QPixmap)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QSizePolicy, QWidget)
import res_rc


class UpButton(QPushButton):
    def __init__(self, parent=None):
        super(UpButton, self).__init__(parent)
        self.setIcon(QIcon("Qt_project_res/UpButton.png"))

    def mousePressEvent(self, event):
        super(UpButton, self).mousePressEvent(event)
        self.setIcon(QIcon("Qt_project_res/UpButtonPress.png"))

    def mouseReleaseEvent(self, event):
        super(UpButton, self).mouseReleaseEvent(event)
        self.setIcon(QIcon("Qt_project_res/UpButtonPress.png" if self.isChecked() else "Qt_project_res/UpButton.png"))


class DownButton(QPushButton):
    def __init__(self, parent=None):
        super(DownButton, self).__init__(parent)
        self.setIcon(QIcon("Qt_project_res/DownButton.png"))

    def mousePressEvent(self, event):
        super(DownButton, self).mousePressEvent(event)
        self.setIcon(QIcon("Qt_project_res/DownButtonPress.png"))

    def mouseReleaseEvent(self, event):
        super(DownButton, self).mouseReleaseEvent(event)
        self.setIcon(
            QIcon("Qt_project_res/DownButtonPress.png" if self.isChecked() else "Qt_project_res/DownButton.png"))


class StartTimerButton(QPushButton):
    def __init__(self, parent=None):
        super(StartTimerButton, self).__init__(parent)
        self.setIcon(QIcon("Qt_project_res/StartTimerButton.png"))

    def mousePressEvent(self, event):
        super(StartTimerButton, self).mousePressEvent(event)
        self.setIcon(QIcon("Qt_project_res/StartTimerButtonPress.png"))

    def mouseReleaseEvent(self, event):
        super(StartTimerButton, self).mouseReleaseEvent(event)
        self.setIcon(
            QIcon("Qt_project_res/StartTimerPress.png" if self.isChecked() else "Qt_project_res/StartTimerButton.png"))


class StopTimerButton(QPushButton):
    def __init__(self, parent=None):
        super(StopTimerButton, self).__init__(parent)
        self.setIcon(QIcon("Qt_project_res/StopTimerButton.png"))

    def mousePressEvent(self, event):
        super(StopTimerButton, self).mousePressEvent(event)
        self.setIcon(QIcon("Qt_project_res/StopTimerButtonPress.png"))

    def mouseReleaseEvent(self, event):
        super(StopTimerButton, self).mouseReleaseEvent(event)
        self.setIcon(
            QIcon("Qt_project_res/StopTimerPress.png" if self.isChecked() else "Qt_project_res/StopTimerButton.png"))


class ResetTimerButton(QPushButton):
    def __init__(self, parent=None):
        super(ResetTimerButton, self).__init__(parent)
        self.setIcon(QIcon("Qt_project_res/ResetTimerButton.png"))

    def mousePressEvent(self, event):
        super(ResetTimerButton, self).mousePressEvent(event)
        self.setIcon(QIcon("Qt_project_res/ResetTimerButtonPress.png"))

    def mouseReleaseEvent(self, event):
        super(ResetTimerButton, self).mouseReleaseEvent(event)
        self.setIcon(
            QIcon("Qt_project_res/ResetTimerPress.png" if self.isChecked() else "Qt_project_res/ResetTimerButton.png"))


class LineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(LineEdit, self).__init__(parent)

    def keyPressEvent(self, e):
        k = e.key()
        if Qt.Key_0 <= k <= Qt.Key_9 or k == Qt.Key_Left or k == Qt.Key_Right or k == Qt.Key_Backspace:
            super().keyPressEvent(e)


class Tablo(object):
    def __init__(self):
        self.MainWindow = QMainWindow()
        self.startTimer = False
        self.stopTimer = False
        self.minutes = 0
        self.seconds = 0
        self.min_go = 0
        self.sec_go = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.TimeOut_func)
        self.player = QtMultimedia.QMediaPlayer()

    def setupUi(self):
        self.MainWindow.setEnabled(True)
        self.MainWindow.resize(800, 360)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWindow.sizePolicy().hasHeightForWidth())
        self.MainWindow.setSizePolicy(sizePolicy)
        self.MainWindow.setMinimumSize(QSize(800, 360))
        self.MainWindow.setMaximumSize(QSize(800, 360))
        self.MainWindow.setSizeIncrement(QSize(800, 360))
        self.MainWindow.setBaseSize(QSize(800, 360))
        font = QFont()
        font.setItalic(False)
        self.MainWindow.setFont(font)
        self.MainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u":/icons/Qt_project_res/football.png", QSize(), QIcon.Normal, QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.MainWidget = QWidget(self.MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setMinimumSize(QSize(800, 360))
        self.MainWidget.setMaximumSize(QSize(800, 360))
        self.MainWidget.setSizeIncrement(QSize(800, 360))
        self.MainWidget.setBaseSize(QSize(800, 359))
        self.MainWidget.setFocusPolicy(Qt.NoFocus)
        self.MainWidget.setStyleSheet(u"QWidget{\n"
                                      "	background-color: rgb(255, 255, 255);\n"
                                      "}")
        self.UpButtonPeriod = UpButton(self.MainWidget)
        self.UpButtonPeriod.setObjectName(u"UpButtonPeriod")
        self.UpButtonPeriod.setGeometry(QRect(434, 42, 50, 50))
        self.UpButtonPeriod.setCursor(QCursor(Qt.PointingHandCursor))
        self.UpButtonPeriod.setStyleSheet(u"QPushButton{\n"
                                          "    	border-radius: 10px;\n"
                                          "}")
        self.UpButtonPeriod.setIconSize(QSize(50, 50))
        self.UpButtonPeriod.setFlat(True)
        self.DownButtonPeriod = DownButton(self.MainWidget)
        self.DownButtonPeriod.setObjectName(u"DownButtonPeriod")
        self.DownButtonPeriod.setGeometry(QRect(434, 104, 50, 50))
        self.DownButtonPeriod.setCursor(QCursor(Qt.PointingHandCursor))
        self.DownButtonPeriod.setStyleSheet(u"QPushButton{\n"
                                            "    	border-radius: 10px;\n"
                                            "}")

        self.DownButtonPeriod.setIconSize(QSize(50, 50))
        self.DownButtonPeriod.setFlat(True)
        self.UpButtonGg = UpButton(self.MainWidget)
        self.UpButtonGg.setObjectName(u"UpButtonGg")
        self.UpButtonGg.setGeometry(QRect(734, 42, 50, 50))
        self.UpButtonGg.setCursor(QCursor(Qt.PointingHandCursor))
        self.UpButtonGg.setStyleSheet(u"QPushButton{\n"
                                      "    	border-radius: 10px;\n"
                                      "}")
        self.UpButtonGg.setIconSize(QSize(50, 50))
        self.UpButtonGg.setFlat(True)
        self.DownButtonGg = DownButton(self.MainWidget)
        self.DownButtonGg.setObjectName(u"DownButtonGg")
        self.DownButtonGg.setGeometry(QRect(734, 104, 50, 50))
        self.DownButtonGg.setCursor(QCursor(Qt.PointingHandCursor))
        self.DownButtonGg.setStyleSheet(u"QPushButton{\n"
                                        "    	border-radius: 10px;\n"
                                        "}")
        self.DownButtonGg.setIconSize(QSize(50, 50))
        self.DownButtonGg.setFlat(True)
        self.UpButtonFg = UpButton(self.MainWidget)
        self.UpButtonFg.setObjectName(u"UpButtonFg")
        self.UpButtonFg.setGeometry(QRect(734, 206, 50, 50))
        self.UpButtonFg.setCursor(QCursor(Qt.PointingHandCursor))
        self.UpButtonFg.setStyleSheet(u"QPushButton{\n"
                                      "    	border-radius: 10px;\n"
                                      "}")
        self.UpButtonFg.setIconSize(QSize(50, 50))
        self.UpButtonFg.setFlat(True)
        self.DownButtonFg = DownButton(self.MainWidget)
        self.DownButtonFg.setObjectName(u"DownButtonFg")
        self.DownButtonFg.setGeometry(QRect(734, 268, 50, 50))
        self.DownButtonFg.setCursor(QCursor(Qt.PointingHandCursor))
        self.DownButtonFg.setStyleSheet(u"QPushButton{\n"
                                        "    	border-radius: 10px;\n"
                                        "}")
        self.DownButtonFg.setIconSize(QSize(50, 50))
        self.DownButtonFg.setCheckable(False)
        self.DownButtonFg.setChecked(False)
        self.DownButtonFg.setAutoRepeat(False)
        self.DownButtonFg.setAutoExclusive(False)
        self.DownButtonFg.setFlat(True)
        self.StartTimerButton = StartTimerButton(self.MainWidget)
        self.StartTimerButton.setObjectName(u"StartTimerButton")
        self.StartTimerButton.setGeometry(QRect(277, 258, 80, 30))
        self.StartTimerButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.StartTimerButton.setAutoFillBackground(False)
        self.StartTimerButton.setStyleSheet(u"QPushButton{\n"
                                            "    	border-radius: 10px;\n"
                                            "}")
        self.StartTimerButton.setIconSize(QSize(80, 30))
        self.StartTimerButton.setFlat(True)
        self.StopTimerButton = StopTimerButton(self.MainWidget)
        self.StopTimerButton.setObjectName(u"StopTimerButton")
        self.StopTimerButton.setGeometry(QRect(362, 258, 80, 30))
        self.StopTimerButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.StopTimerButton.setStyleSheet(u"QPushButton{\n"
                                           "    	border-radius: 10px;\n"
                                           "}")
        self.StopTimerButton.setIconSize(QSize(80, 30))
        self.StopTimerButton.setFlat(True)
        self.ResetTimerButton = ResetTimerButton(self.MainWidget)
        self.ResetTimerButton.setObjectName(u"ResetTimerButton")
        self.ResetTimerButton.setGeometry(QRect(447, 258, 80, 30))
        self.ResetTimerButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ResetTimerButton.setStyleSheet(u"QPushButton{\n"
                                            "    	border-radius: 10px;\n"
                                            "}")
        self.ResetTimerButton.setIconSize(QSize(80, 30))
        self.ResetTimerButton.setFlat(True)
        self.UpButtonFh = UpButton(self.MainWidget)
        self.UpButtonFh.setObjectName(u"UpButtonFh")
        self.UpButtonFh.setGeometry(QRect(134, 206, 50, 50))
        self.UpButtonFh.setCursor(QCursor(Qt.PointingHandCursor))
        self.UpButtonFh.setStyleSheet(u"QPushButton{\n"
                                      "    	border-radius: 10px;\n"
                                      "}")
        self.UpButtonFh.setIconSize(QSize(50, 50))
        self.UpButtonFh.setFlat(True)
        self.DownButtonFh = DownButton(self.MainWidget)
        self.DownButtonFh.setObjectName(u"DownButtonFh")
        self.DownButtonFh.setGeometry(QRect(134, 268, 50, 50))
        self.DownButtonFh.setCursor(QCursor(Qt.PointingHandCursor))
        self.DownButtonFh.setStyleSheet(u"QPushButton{\n"
                                        "    	border-radius: 10px;\n"
                                        "}")
        self.DownButtonFh.setIconSize(QSize(50, 50))
        self.DownButtonFh.setAutoDefault(False)
        self.DownButtonFh.setFlat(True)
        self.HostsScoreText = QLabel(self.MainWidget)
        self.HostsScoreText.setObjectName(u"HostsScoreText")
        self.HostsScoreText.setGeometry(QRect(24, 32, 90, 22))
        self.HostsScoreText.setLayoutDirection(Qt.LeftToRight)
        self.HostsScoreText.setStyleSheet(u"QLabel{\n"
                                          "    font-family: Roboto;\n"
                                          "    font-size: 24px;\n"
                                          "    font-weight: 500;\n"
                                          "}")
        self.HostsScoreText.setLineWidth(1)
        self.HostsScoreText.setTextFormat(Qt.AutoText)
        self.HostsScoreText.setScaledContents(False)
        self.HostsScoreText.setAlignment(Qt.AlignCenter)
        self.HostsScoreText.setWordWrap(False)
        self.HostsScoreText.setIndent(-1)
        self.HostsScoreText.setOpenExternalLinks(False)
        self.HostsScoreText.setTextInteractionFlags(Qt.NoTextInteraction)
        self.Timer_Rectangle = QLabel(self.MainWidget)
        self.Timer_Rectangle.setObjectName(u"Timer_Rectangle")
        self.Timer_Rectangle.setGeometry(QRect(277, 218, 250, 30))
        self.Timer_Rectangle.setPixmap(QPixmap(u":/forms/Qt_project_res/RectangleTimer.png"))
        self.UpButtonGh = UpButton(self.MainWidget)
        self.UpButtonGh.setObjectName(u"UpButtonGh")
        self.UpButtonGh.setGeometry(QRect(134, 42, 50, 50))
        self.UpButtonGh.setCursor(QCursor(Qt.PointingHandCursor))
        self.UpButtonGh.setStyleSheet(u"QPushButton{\n"
                                      "    	border-radius: 10px;\n"
                                      "}")
        self.UpButtonGh.setIconSize(QSize(50, 50))
        self.UpButtonGh.setFlat(True)
        self.DownButtonGh = DownButton(self.MainWidget)
        self.DownButtonGh.setObjectName(u"DownButtonGh")
        self.DownButtonGh.setGeometry(QRect(134, 104, 50, 50))
        self.DownButtonGh.setCursor(QCursor(Qt.PointingHandCursor))
        self.DownButtonGh.setAutoFillBackground(False)
        self.DownButtonGh.setStyleSheet(u"QPushButton{\n"
                                        "    	border-radius: 10px;\n"
                                        "}")
        self.DownButtonGh.setIconSize(QSize(50, 50))
        self.DownButtonGh.setFlat(True)
        self.HostsGoalCounter_Rectangle = QLabel(self.MainWidget)
        self.HostsGoalCounter_Rectangle.setObjectName(u"HostsGoalCounter_Rectangle")
        self.HostsGoalCounter_Rectangle.setGeometry(QRect(19, 54, 100, 100))
        self.HostsGoalCounter_Rectangle.setPixmap(QPixmap(u":/forms/Qt_project_res/Rectangle.png"))
        self.HostsGoalCounter_Rectangle.setAlignment(Qt.AlignCenter)
        self.HostsGoalCounter = QLabel(self.MainWidget)
        self.HostsGoalCounter.setObjectName(u"HostsGoalCounter")
        self.HostsGoalCounter.setGeometry(QRect(29, 62, 81, 84))
        self.HostsGoalCounter.setStyleSheet(u"QLabel{\n"
                                            "    font-family: Roboto;\n"
                                            "    font-size: 85px;\n"
                                            "    font-weight: 500;\n"
                                            "}")
        self.HostsGoalCounter.setAlignment(Qt.AlignCenter)
        self.PeriodCounter_Rectangle = QLabel(self.MainWidget)
        self.PeriodCounter_Rectangle.setObjectName(u"PeriodCounter_Rectangle")
        self.PeriodCounter_Rectangle.setGeometry(QRect(319, 54, 100, 100))
        self.PeriodCounter_Rectangle.setPixmap(QPixmap(u":/forms/Qt_project_res/Rectangle.png"))
        self.PeroidText = QLabel(self.MainWidget)
        self.PeroidText.setObjectName(u"PeroidText")
        self.PeroidText.setGeometry(QRect(320, 31, 98, 20))
        self.PeroidText.setStyleSheet(u"QLabel{\n"
                                      "    font-family: Roboto;\n"
                                      "    font-size: 24px;\n"
                                      "    font-weight: 500;\n"
                                      "}")
        self.PeroidText.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.PeriodCounter = QLabel(self.MainWidget)
        self.PeriodCounter.setObjectName(u"PeriodCounter")
        self.PeriodCounter.setGeometry(QRect(329, 62, 81, 84))
        self.PeriodCounter.setStyleSheet(u"QLabel{\n"
                                         "    font-family: Roboto;\n"
                                         "    font-size: 85px;\n"
                                         "    font-weight: 500;\n"
                                         "}")
        self.PeriodCounter.setAlignment(Qt.AlignCenter)
        self.GuestsGoalCounter_Rectangle = QLabel(self.MainWidget)
        self.GuestsGoalCounter_Rectangle.setObjectName(u"GuestsGoalCounter_Rectangle")
        self.GuestsGoalCounter_Rectangle.setGeometry(QRect(619, 54, 100, 100))
        self.GuestsGoalCounter_Rectangle.setPixmap(QPixmap(u":/forms/Qt_project_res/Rectangle.png"))
        self.GuestsGoalCounter_Rectangle.setAlignment(Qt.AlignCenter)
        self.GuestsGoalCounter = QLabel(self.MainWidget)
        self.GuestsGoalCounter.setObjectName(u"GuestsGoalCounter")
        self.GuestsGoalCounter.setGeometry(QRect(629, 62, 81, 84))
        self.GuestsGoalCounter.setStyleSheet(u"QLabel{\n"
                                             "    font-family: Roboto;\n"
                                             "    font-size: 85px;\n"
                                             "    font-weight: 500;\n"
                                             "}")
        self.GuestsGoalCounter.setAlignment(Qt.AlignCenter)
        self.GuestScoreText = QLabel(self.MainWidget)
        self.GuestScoreText.setObjectName(u"GuestScoreText")
        self.GuestScoreText.setGeometry(QRect(624, 32, 90, 22))
        self.GuestScoreText.setStyleSheet(u"QLabel{\n"
                                          "    font-family: Roboto;\n"
                                          "    font-size: 24px;\n"
                                          "    font-weight: 500;\n"
                                          "}")
        self.GuestScoreText.setAlignment(Qt.AlignCenter)
        self.HostsFoulCounter_Rectangle = QLabel(self.MainWidget)
        self.HostsFoulCounter_Rectangle.setObjectName(u"HostsFoulCounter_Rectangle")
        self.HostsFoulCounter_Rectangle.setGeometry(QRect(19, 218, 100, 100))
        self.HostsFoulCounter_Rectangle.setPixmap(QPixmap(u":/forms/Qt_project_res/Rectangle.png"))
        self.HostsFoulCounter_Rectangle.setAlignment(Qt.AlignCenter)
        self.FoulsHostsText = QLabel(self.MainWidget)
        self.FoulsHostsText.setObjectName(u"FoulsHostsText")
        self.FoulsHostsText.setGeometry(QRect(32, 188, 75, 29))
        self.FoulsHostsText.setStyleSheet(u"QLabel{\n"
                                          "    font-family: Roboto;\n"
                                          "    font-size: 24px;\n"
                                          "    font-weight: 500;\n"
                                          "}")
        self.FoulsHostsText.setAlignment(Qt.AlignCenter)
        self.HostsFoulCounter = QLabel(self.MainWidget)
        self.HostsFoulCounter.setObjectName(u"HostsFoulCounter")
        self.HostsFoulCounter.setGeometry(QRect(29, 226, 81, 84))
        self.HostsFoulCounter.setStyleSheet(u"QLabel{\n"
                                            "    font-family: Roboto;\n"
                                            "    font-size: 85px;\n"
                                            "    font-weight: 500;\n"
                                            "}")
        self.HostsFoulCounter.setAlignment(Qt.AlignCenter)
        self.GuestsFoulCounter_Rectangle = QLabel(self.MainWidget)
        self.GuestsFoulCounter_Rectangle.setObjectName(u"GuestsFoulCounter_Rectangle")
        self.GuestsFoulCounter_Rectangle.setGeometry(QRect(619, 218, 100, 100))
        self.GuestsFoulCounter_Rectangle.setPixmap(QPixmap(u":/forms/Qt_project_res/Rectangle.png"))
        self.GuestsFoulCounter_Rectangle.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.GuestFoulsText = QLabel(self.MainWidget)
        self.GuestFoulsText.setObjectName(u"GuestFoulsText")
        self.GuestFoulsText.setGeometry(QRect(632, 188, 75, 29))
        self.GuestFoulsText.setStyleSheet(u"QLabel{\n"
                                          "    font-family: Roboto;\n"
                                          "    font-size: 24px;\n"
                                          "    font-weight: 500;\n"
                                          "}")
        self.GuestFoulsText.setAlignment(Qt.AlignCenter)
        self.Separator = QLabel(self.MainWidget)
        self.Separator.setObjectName(u"Separator")
        self.Separator.setGeometry(QRect(392, 223, 10, 19))
        self.Separator.setStyleSheet(u"QLabel{\n"
                                     "    font-family: Roboto;\n"
                                     "    font-size: 24px;\n"
                                     "    font-weight: 500;\n"
                                     "}")
        self.Separator.setScaledContents(False)
        self.Separator.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.Separator.setWordWrap(False)
        self.Separator.setMargin(-2)
        self.TimeText = QLabel(self.MainWidget)
        self.TimeText.setObjectName(u"TimeText")
        self.TimeText.setGeometry(QRect(350, 188, 100, 30))
        self.TimeText.setStyleSheet(u"QLabel{\n"
                                    "    font-family: Roboto;\n"
                                    "    font-size: 24px;\n"
                                    "    font-weight: 500;\n"
                                    "}")
        self.TimeText.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.GuestsFoulCounter = QLabel(self.MainWidget)
        self.GuestsFoulCounter.setObjectName(u"GuestsFoulCounter")
        self.GuestsFoulCounter.setGeometry(QRect(629, 226, 81, 84))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setBold(True)
        self.GuestsFoulCounter.setFont(font1)
        self.GuestsFoulCounter.setStyleSheet(u"QLabel{\n"
                                             "    font-family: Roboto;\n"
                                             "    font-size: 85px;\n"
                                             "    font-weight: 500;\n"
                                             "}")
        self.GuestsFoulCounter.setAlignment(Qt.AlignCenter)
        self.Minutes = LineEdit(self.MainWidget)
        self.Minutes.setObjectName(u"Minutes")
        self.Minutes.setGeometry(QRect(316, 224, 48, 18))
        self.Minutes.setStyleSheet(u"QLineEdit{\n"
                                   "    font-family: Roboto;\n"
                                   "    font-size: 18px;\n"
                                   "    font-weight: 500;\n"
                                   "    background-color: white;\n"
                                   "}")
        self.Minutes.setMaxLength(2)
        self.Minutes.setFrame(False)
        self.Minutes.setAlignment(Qt.AlignCenter)
        self.Seconds = LineEdit(self.MainWidget)
        self.Seconds.setObjectName(u"Seconds")
        self.Seconds.setGeometry(QRect(430, 224, 48, 18))
        self.Seconds.setStyleSheet(u"QLineEdit{\n"
                                   "    font-family: Roboto;\n"
                                   "    font-size: 18px;\n"
                                   "    font-weight: 500;\n"
                                   "    background-color: white;\n"
                                   "}")
        self.Seconds.setMaxLength(2)
        self.Seconds.setFrame(False)
        self.Seconds.setEchoMode(QLineEdit.Normal)
        self.Seconds.setAlignment(Qt.AlignCenter)
        self.MainWindow.setCentralWidget(self.MainWidget)
        self.UpButtonPeriod.raise_()
        self.DownButtonPeriod.raise_()
        self.UpButtonGg.raise_()
        self.DownButtonGg.raise_()
        self.UpButtonFg.raise_()
        self.DownButtonFg.raise_()
        self.StartTimerButton.raise_()
        self.StopTimerButton.raise_()
        self.ResetTimerButton.raise_()
        self.UpButtonFh.raise_()
        self.DownButtonFh.raise_()
        self.HostsScoreText.raise_()
        self.Timer_Rectangle.raise_()
        self.UpButtonGh.raise_()
        self.DownButtonGh.raise_()
        self.HostsGoalCounter_Rectangle.raise_()
        self.PeriodCounter_Rectangle.raise_()
        self.PeroidText.raise_()
        self.PeriodCounter.raise_()
        self.GuestsGoalCounter_Rectangle.raise_()
        self.GuestsGoalCounter.raise_()
        self.GuestScoreText.raise_()
        self.HostsFoulCounter_Rectangle.raise_()
        self.FoulsHostsText.raise_()
        self.HostsFoulCounter.raise_()
        self.GuestsFoulCounter_Rectangle.raise_()
        self.GuestFoulsText.raise_()
        self.Separator.raise_()
        self.TimeText.raise_()
        self.GuestsFoulCounter.raise_()
        self.Minutes.raise_()
        self.Seconds.raise_()
        self.HostsGoalCounter.raise_()

        self.retranslateUi(self.MainWindow)

        self.DownButtonFh.setDefault(False)
        self.UpButtonGh.setDefault(False)

        QMetaObject.connectSlotsByName(self.MainWindow)

        self.UpButtonGh.clicked.connect(self.UpButtonGh_func)
        self.DownButtonGh.clicked.connect(self.DownButtonGh_func)
        self.UpButtonFh.clicked.connect(self.UpButtonFh_func)
        self.DownButtonFh.clicked.connect(self.DownButtonFh_func)
        self.UpButtonGg.clicked.connect(self.UpButtonGg_func)
        self.DownButtonGg.clicked.connect(self.DownButtonGg_func)
        self.UpButtonFg.clicked.connect(self.UpButtonFg_func)
        self.DownButtonFg.clicked.connect(self.DownButtonFg_func)
        self.UpButtonPeriod.clicked.connect(self.UpButtonPeriod_func)
        self.DownButtonPeriod.clicked.connect(self.DownButtonPeriod_func)
        self.StartTimerButton.clicked.connect(self.StartTimerButton_func)
        self.StopTimerButton.clicked.connect(self.StopTimerButton_func)
        self.ResetTimerButton.clicked.connect(self.ResetTimerButton_func)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Table", None))
        self.UpButtonPeriod.setText("")
        self.DownButtonPeriod.setText("")
        self.UpButtonGg.setText("")
        self.DownButtonGg.setText("")
        self.UpButtonFg.setText("")
        self.DownButtonFg.setText("")
        self.StartTimerButton.setText("")
        self.StopTimerButton.setText("")
        self.StopTimerButton.setShortcut("")
        self.ResetTimerButton.setText("")
        self.UpButtonFh.setText("")
        self.DownButtonFh.setText("")
        self.HostsScoreText.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0447\u0451\u0442", None))
        self.Timer_Rectangle.setText("")
        self.UpButtonGh.setText("")
        self.DownButtonGh.setText("")
        self.HostsGoalCounter_Rectangle.setText("")
        self.HostsGoalCounter.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.PeriodCounter_Rectangle.setText("")
        self.PeroidText.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.PeriodCounter.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.GuestsGoalCounter_Rectangle.setText("")
        self.GuestsGoalCounter.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.GuestScoreText.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0447\u0451\u0442", None))
        self.HostsFoulCounter_Rectangle.setText("")
        self.FoulsHostsText.setText(QCoreApplication.translate("MainWindow", u"\u0444\u043e\u043b\u044b", None))
        self.HostsFoulCounter.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.GuestsFoulCounter_Rectangle.setText("")
        self.GuestFoulsText.setText(QCoreApplication.translate("MainWindow", u"\u0444\u043e\u043b\u044b", None))
        self.Separator.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.TimeText.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0440\u0435\u043c\u044f", None))
        self.GuestsFoulCounter.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Minutes.setInputMask("")
        self.Minutes.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.Seconds.setText(QCoreApplication.translate("MainWindow", u"00", None))

    def UpButtonGh_func(self):
        n = int(self.HostsGoalCounter.text())
        if n != 9:
            self.HostsGoalCounter.setText(str(n + 1))

    def DownButtonGh_func(self):
        n = int(self.HostsGoalCounter.text())
        if n != 0:
            self.HostsGoalCounter.setText(str(n - 1))

    def UpButtonFh_func(self):
        n = int(self.HostsFoulCounter.text())
        if n != 9:
            self.HostsFoulCounter.setText(str(n + 1))

    def DownButtonFh_func(self):
        n = int(self.HostsFoulCounter.text())
        if n != 0:
            self.HostsFoulCounter.setText(str(n - 1))

    def UpButtonGg_func(self):
        n = int(self.GuestsGoalCounter.text())
        if n != 9:
            self.GuestsGoalCounter.setText(str(n + 1))

    def DownButtonGg_func(self):
        n = int(self.GuestsGoalCounter.text())
        if n != 0:
            self.GuestsGoalCounter.setText(str(n - 1))

    def UpButtonFg_func(self):
        n = int(self.GuestsFoulCounter.text())
        if n != 9:
            self.GuestsFoulCounter.setText(str(n + 1))

    def DownButtonFg_func(self):
        n = int(self.GuestsFoulCounter.text())
        if n != 0:
            self.GuestsFoulCounter.setText(str(n - 1))

    def UpButtonPeriod_func(self):
        n = int(self.PeriodCounter.text())
        if n != 9:
            self.PeriodCounter.setText(str(n + 1))

    def DownButtonPeriod_func(self):
        n = int(self.PeriodCounter.text())
        if n != 0:
            self.PeriodCounter.setText(str(n - 1))

    def StartTimerButton_func(self):
        if self.stopTimer:
            self.stopTimer = False
            self.startTimer = True
            self.timer.start()
            pass
        elif not self.startTimer:
            self.startTimer = True
            self.Seconds.setReadOnly(True)
            self.Minutes.setReadOnly(True)
            self.minutes = int(self.Minutes.text())
            self.seconds = int(self.Seconds.text())
            self.Seconds.setText("00")
            self.Minutes.setText("00")
            self.timer.start(1000)

    def StopTimerButton_func(self):
        if self.startTimer:
            self.startTimer = False
            self.stopTimer = True
            self.timer.stop()

    def ResetTimerButton_func(self):
        self.stopTimer = False
        self.startTimer = False
        self.Minutes.setText("00")
        self.Seconds.setText("00")
        self.Minutes.setReadOnly(False)
        self.Seconds.setReadOnly(False)
        self.timer.stop()
        self.min_go = 0
        self.sec_go = 0
        self.seconds = 0
        self.minutes = 0

    def TimeOut_func(self):
        if self.startTimer:
            self.sec_go += 1
            if self.sec_go == 60:
                self.sec_go = 0
                self.min_go += 1
            if self.sec_go >= self.seconds and self.min_go >= self.minutes:
                self.timer.stop()
                pass
            self.Seconds.setText(f'{self.sec_go // 10}{self.sec_go % 10}')
            self.Minutes.setText(f'{self.min_go // 10}{self.min_go % 10}')

    def load_mp3(self, filename):
        media = QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player.setMedia(content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tablo = Tablo()
    tablo.setupUi()
    tablo.MainWindow.show()
    sys.exit(app.exec())
