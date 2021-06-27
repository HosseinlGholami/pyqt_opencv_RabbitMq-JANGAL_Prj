# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReceiveUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 561)
        MainWindow.setMinimumSize(QtCore.QSize(670, 561))
        MainWindow.setMaximumSize(QtCore.QSize(670, 561))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(670, 520))
        self.centralwidget.setMaximumSize(QtCore.QSize(670, 520))
        self.centralwidget.setObjectName("centralwidget")
        self.textLabel = QtWidgets.QLabel(self.centralwidget)
        self.textLabel.setGeometry(QtCore.QRect(10, 490, 299, 21))
        self.textLabel.setObjectName("textLabel")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(5, 5, 640, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QtCore.QSize(640, 480))
        self.image_label.setMaximumSize(QtCore.QSize(640, 480))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 480, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 21))
        self.menubar.setObjectName("menubar")
        self.menuexit = QtWidgets.QMenu(self.menubar)
        self.menuexit.setObjectName("menuexit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionblur_filter = QtWidgets.QAction(MainWindow)
        self.actionblur_filter.setObjectName("actionblur_filter")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionBlur_Filter = QtWidgets.QAction(MainWindow)
        self.actionBlur_Filter.setObjectName("actionBlur_Filter")
        self.actionRed_Filter = QtWidgets.QAction(MainWindow)
        self.actionRed_Filter.setObjectName("actionRed_Filter")
        self.actionGreen_Filter = QtWidgets.QAction(MainWindow)
        self.actionGreen_Filter.setObjectName("actionGreen_Filter")
        self.actionBlue_Filter = QtWidgets.QAction(MainWindow)
        self.actionBlue_Filter.setObjectName("actionBlue_Filter")
        self.menubar.addAction(self.menuexit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textLabel.setText(_translate("MainWindow", "this application designed by HosseinlGholami-2021"))
        self.menuexit.setTitle(_translate("MainWindow", "File"))
        self.actionblur_filter.setText(_translate("MainWindow", "blur-filter"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionBlur_Filter.setText(_translate("MainWindow", "Blur Filter"))
        self.actionRed_Filter.setText(_translate("MainWindow", "Red Filter"))
        self.actionGreen_Filter.setText(_translate("MainWindow", "Green Filter"))
        self.actionBlue_Filter.setText(_translate("MainWindow", "Blue Filter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
