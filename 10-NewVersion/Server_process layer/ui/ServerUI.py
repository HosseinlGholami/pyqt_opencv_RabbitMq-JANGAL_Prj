# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServerUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(448, 485)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(448, 485))
        MainWindow.setMaximumSize(QtCore.QSize(448, 485))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 421, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.acamTab = QtWidgets.QWidget()
        self.acamTab.setAccessibleName("")
        self.acamTab.setAutoFillBackground(False)
        self.acamTab.setObjectName("acamTab")
        self.addc_Button = QtWidgets.QPushButton(self.acamTab)
        self.addc_Button.setGeometry(QtCore.QRect(220, 130, 181, 31))
        self.addc_Button.setObjectName("addc_Button")
        self.label_5 = QtWidgets.QLabel(self.acamTab)
        self.label_5.setGeometry(QtCore.QRect(10, 19, 91, 21))
        self.label_5.setObjectName("label_5")
        self.processor_lyr_lineEdit = QtWidgets.QLineEdit(self.acamTab)
        self.processor_lyr_lineEdit.setGeometry(QtCore.QRect(110, 50, 261, 20))
        self.processor_lyr_lineEdit.setObjectName("processor_lyr_lineEdit")
        self.label_8 = QtWidgets.QLabel(self.acamTab)
        self.label_8.setGeometry(QtCore.QRect(10, 49, 81, 21))
        self.label_8.setObjectName("label_8")
        self.lvl_ComboBox = QtWidgets.QComboBox(self.acamTab)
        self.lvl_ComboBox.setGeometry(QtCore.QRect(110, 80, 261, 21))
        self.lvl_ComboBox.setObjectName("lvl_ComboBox")
        self.lvl_ComboBox.addItem("")
        self.lvl_ComboBox.addItem("")
        self.lvl_ComboBox.addItem("")
        self.lvl_ComboBox.addItem("")
        self.label_17 = QtWidgets.QLabel(self.acamTab)
        self.label_17.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.label_17.setObjectName("label_17")
        self.CamNameComboBox = QtWidgets.QComboBox(self.acamTab)
        self.CamNameComboBox.setGeometry(QtCore.QRect(110, 20, 261, 21))
        self.CamNameComboBox.setObjectName("CamNameComboBox")
        self.Refresh_Button = QtWidgets.QPushButton(self.acamTab)
        self.Refresh_Button.setGeometry(QtCore.QRect(20, 130, 181, 31))
        self.Refresh_Button.setObjectName("Refresh_Button")
        self.tabWidget.addTab(self.acamTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.StrSenButton = QtWidgets.QPushButton(self.tab)
        self.StrSenButton.setGeometry(QtCore.QRect(20, 140, 111, 31))
        self.StrSenButton.setObjectName("StrSenButton")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 91, 21))
        self.label_3.setObjectName("label_3")
        self.AlgComboBox = QtWidgets.QComboBox(self.tab)
        self.AlgComboBox.setGeometry(QtCore.QRect(130, 80, 261, 21))
        self.AlgComboBox.setObjectName("AlgComboBox")
        self.StpSenButton = QtWidgets.QPushButton(self.tab)
        self.StpSenButton.setGeometry(QtCore.QRect(150, 140, 111, 31))
        self.StpSenButton.setObjectName("StpSenButton")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 71, 21))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 81, 21))
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(90, 60, 301, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.process_spinBox = QtWidgets.QSpinBox(self.tab)
        self.process_spinBox.setGeometry(QtCore.QRect(140, 110, 71, 22))
        self.process_spinBox.setMaximum(255)
        self.process_spinBox.setProperty("value", 60)
        self.process_spinBox.setObjectName("process_spinBox")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(30, 110, 91, 21))
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(30, 30, 81, 21))
        self.label_9.setObjectName("label_9")
        self.SelectprocessComboBox = QtWidgets.QComboBox(self.tab)
        self.SelectprocessComboBox.setGeometry(QtCore.QRect(130, 30, 261, 21))
        self.SelectprocessComboBox.setObjectName("SelectprocessComboBox")
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(110, 10, 281, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setEnabled(False)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.label_11.setObjectName("label_11")
        self.delSenButton = QtWidgets.QPushButton(self.tab)
        self.delSenButton.setGeometry(QtCore.QRect(280, 140, 111, 31))
        self.delSenButton.setObjectName("delSenButton")
        self.tabWidget.addTab(self.tab, "")
        self.LogtextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.LogtextBrowser.setGeometry(QtCore.QRect(10, 270, 421, 161))
        self.LogtextBrowser.setObjectName("LogtextBrowser")
        self.logLabel = QtWidgets.QLabel(self.centralwidget)
        self.logLabel.setGeometry(QtCore.QRect(20, 250, 51, 21))
        self.logLabel.setObjectName("logLabel")
        self.LogtextBrowser.raise_()
        self.logLabel.raise_()
        self.tabWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.acamTab.setToolTip(_translate("MainWindow", "<html><head/><body><p>Add Camera</p></body></html>"))
        self.addc_Button.setText(_translate("MainWindow", "Add Process"))
        self.label_5.setText(_translate("MainWindow", "Camera Selection"))
        self.processor_lyr_lineEdit.setText(_translate("MainWindow", "pc1"))
        self.label_8.setText(_translate("MainWindow", "Processor Name"))
        self.lvl_ComboBox.setItemText(0, _translate("MainWindow", "1"))
        self.lvl_ComboBox.setItemText(1, _translate("MainWindow", "2"))
        self.lvl_ComboBox.setItemText(2, _translate("MainWindow", "3"))
        self.lvl_ComboBox.setItemText(3, _translate("MainWindow", "4"))
        self.label_17.setText(_translate("MainWindow", "Level of Access"))
        self.Refresh_Button.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.acamTab), _translate("MainWindow", "Add Processing Layer"))
        self.StrSenButton.setStatusTip(_translate("MainWindow", "it will activate the camera to send data to clients and store it for future access."))
        self.StrSenButton.setText(_translate("MainWindow", "Activate Process"))
        self.label_3.setText(_translate("MainWindow", "Algorithm Selection"))
        self.StpSenButton.setStatusTip(_translate("MainWindow", "it will deactivate the camera but still exist and could be activated again."))
        self.StpSenButton.setText(_translate("MainWindow", "Deactivate Process"))
        self.label_7.setText(_translate("MainWindow", "Process control"))
        self.label_10.setText(_translate("MainWindow", "frame Hop"))
        self.label_9.setText(_translate("MainWindow", "Processor Name"))
        self.label_11.setText(_translate("MainWindow", "Process Selection"))
        self.delSenButton.setStatusTip(_translate("MainWindow", "it will deactivate the camera but still exist and could be activated again."))
        self.delSenButton.setText(_translate("MainWindow", "Delete Process"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Process Controller"))
        self.logLabel.setText(_translate("MainWindow", "Log"))
        self.actionClose.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
