# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_run_ui.ui'
#
# Created: Thu Feb  7 20:41:11 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(764, 829)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_5 = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_5.sizePolicy().hasHeightForWidth())
        self.dockWidget_5.setSizePolicy(sizePolicy)
        self.dockWidget_5.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget_5.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_5.setObjectName(_fromUtf8("dockWidget_5"))
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents_5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit = QtGui.QTextEdit(self.dockWidgetContents_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit.setBaseSize(QtCore.QSize(0, 500))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.dockWidget_5.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_5)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_3.sizePolicy().hasHeightForWidth())
        self.dockWidget_3.setSizePolicy(sizePolicy)
        self.dockWidget_3.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget_3.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidget_3.setObjectName(_fromUtf8("dockWidget_3"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.ogl = Show3DWithSlider(self.dockWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ogl.sizePolicy().hasHeightForWidth())
        self.ogl.setSizePolicy(sizePolicy)
        self.ogl.setObjectName(_fromUtf8("ogl"))
        self.horizontalLayout_2.addWidget(self.ogl)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_3)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionEnergy = QtGui.QAction(MainWindow)
        self.actionEnergy.setCheckable(True)
        self.actionEnergy.setChecked(True)
        self.actionEnergy.setObjectName(_fromUtf8("actionEnergy"))
        self.action3D = QtGui.QAction(MainWindow)
        self.action3D.setCheckable(True)
        self.action3D.setObjectName(_fromUtf8("action3D"))
        self.actionGraph = QtGui.QAction(MainWindow)
        self.actionGraph.setCheckable(True)
        self.actionGraph.setObjectName(_fromUtf8("actionGraph"))
        self.toolBar.addAction(self.action3D)
        self.toolBar.addAction(self.actionEnergy)
        self.toolBar.addAction(self.actionGraph)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.dockWidget_5.setWindowTitle(_translate("MainWindow", "Log", None))
        self.dockWidget_3.setWindowTitle(_translate("MainWindow", "3D view", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionEnergy.setText(_translate("MainWindow", "Energy", None))
        self.actionEnergy.setToolTip(_translate("MainWindow", "toggle energy window", None))
        self.action3D.setText(_translate("MainWindow", "3D", None))
        self.action3D.setToolTip(_translate("MainWindow", "toggle 3D viewer", None))
        self.actionGraph.setText(_translate("MainWindow", "Graph", None))
        self.actionGraph.setToolTip(_translate("MainWindow", "toggle graph view", None))

from show3d import Show3DWithSlider
