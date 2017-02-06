# -*- coding: utf-8 -*-

#
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProjectDialog(object):
    def setupUi(self, ProjectDialog):
        ProjectDialog.setObjectName("ProjectDialog")
        ProjectDialog.resize(774, 734)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProjectDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lNewProject = QtWidgets.QLabel(ProjectDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lNewProject.setFont(font)
        self.lNewProject.setObjectName("lNewProject")
        self.verticalLayout.addWidget(self.lNewProject)
        self.lblName = QtWidgets.QLabel(ProjectDialog)
        self.lblName.setObjectName("lblName")
        self.verticalLayout.addWidget(self.lblName)
        spacerItem = QtWidgets.QSpacerItem(17, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditBroadcastAddress = QtWidgets.QLineEdit(ProjectDialog)
        self.lineEditBroadcastAddress.setInputMask("")
        self.lineEditBroadcastAddress.setObjectName("lineEditBroadcastAddress")
        self.gridLayout.addWidget(self.lineEditBroadcastAddress, 14, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(ProjectDialog)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(ProjectDialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 6)
        self.label_7 = QtWidgets.QLabel(ProjectDialog)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 2)
        self.lblNewPath = QtWidgets.QLabel(ProjectDialog)
        self.lblNewPath.setObjectName("lblNewPath")
        self.gridLayout.addWidget(self.lblNewPath, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(ProjectDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 4, 1, 2)
        self.label = QtWidgets.QLabel(ProjectDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.lineEdit_Path = QtWidgets.QLineEdit(ProjectDialog)
        self.lineEdit_Path.setStatusTip("")
        self.lineEdit_Path.setObjectName("lineEdit_Path")
        self.gridLayout.addWidget(self.lineEdit_Path, 0, 3, 1, 1)
        self.btnSelectPath = QtWidgets.QToolButton(ProjectDialog)
        self.btnSelectPath.setObjectName("btnSelectPath")
        self.gridLayout.addWidget(self.btnSelectPath, 0, 4, 1, 2)
        self.label_5 = QtWidgets.QLabel(ProjectDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 4, 1, 2)
        self.label_2 = QtWidgets.QLabel(ProjectDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 57, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 13, 4, 1, 2)
        self.spinBoxSampleRate = KillerDoubleSpinBox(ProjectDialog)
        self.spinBoxSampleRate.setDecimals(3)
        self.spinBoxSampleRate.setMinimum(0.01)
        self.spinBoxSampleRate.setMaximum(1000000000000.0)
        self.spinBoxSampleRate.setSingleStep(0.001)
        self.spinBoxSampleRate.setProperty("value", 1000000.0)
        self.spinBoxSampleRate.setObjectName("spinBoxSampleRate")
        self.gridLayout.addWidget(self.spinBoxSampleRate, 3, 3, 1, 1)
        self.line = QtWidgets.QFrame(ProjectDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 9, 0, 1, 6)
        self.spinBoxFreq = KillerDoubleSpinBox(ProjectDialog)
        self.spinBoxFreq.setDecimals(3)
        self.spinBoxFreq.setMinimum(0.01)
        self.spinBoxFreq.setMaximum(1000000000000.0)
        self.spinBoxFreq.setSingleStep(0.001)
        self.spinBoxFreq.setProperty("value", 433920000.0)
        self.spinBoxFreq.setObjectName("spinBoxFreq")
        self.gridLayout.addWidget(self.spinBoxFreq, 4, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(ProjectDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 2)
        self.btnAddParticipant = QtWidgets.QToolButton(ProjectDialog)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.btnAddParticipant.setIcon(icon)
        self.btnAddParticipant.setObjectName("btnAddParticipant")
        self.gridLayout.addWidget(self.btnAddParticipant, 11, 4, 1, 2)
        self.lOpenSpectrumAnalyzer = QtWidgets.QLabel(ProjectDialog)
        self.lOpenSpectrumAnalyzer.setTextFormat(QtCore.Qt.AutoText)
        self.lOpenSpectrumAnalyzer.setOpenExternalLinks(False)
        self.lOpenSpectrumAnalyzer.setObjectName("lOpenSpectrumAnalyzer")
        self.gridLayout.addWidget(self.lOpenSpectrumAnalyzer, 8, 0, 1, 4)
        self.label_9 = QtWidgets.QLabel(ProjectDialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 11, 0, 3, 2)
        self.btnRemoveParticipant = QtWidgets.QToolButton(ProjectDialog)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.btnRemoveParticipant.setIcon(icon)
        self.btnRemoveParticipant.setObjectName("btnRemoveParticipant")
        self.gridLayout.addWidget(self.btnRemoveParticipant, 12, 4, 1, 2)
        self.txtEdDescription = QtWidgets.QPlainTextEdit(ProjectDialog)
        self.txtEdDescription.setObjectName("txtEdDescription")
        self.gridLayout.addWidget(self.txtEdDescription, 10, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(ProjectDialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 2)
        self.spinBoxBandwidth = KillerDoubleSpinBox(ProjectDialog)
        self.spinBoxBandwidth.setDecimals(3)
        self.spinBoxBandwidth.setMinimum(1.0)
        self.spinBoxBandwidth.setMaximum(999999999999.0)
        self.spinBoxBandwidth.setSingleStep(0.001)
        self.spinBoxBandwidth.setProperty("value", 1000000.0)
        self.spinBoxBandwidth.setObjectName("spinBoxBandwidth")
        self.gridLayout.addWidget(self.spinBoxBandwidth, 5, 3, 1, 1)
        self.spinBoxGain = QtWidgets.QSpinBox(ProjectDialog)
        self.spinBoxGain.setMinimum(1)
        self.spinBoxGain.setProperty("value", 20)
        self.spinBoxGain.setObjectName("spinBoxGain")
        self.gridLayout.addWidget(self.spinBoxGain, 6, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(ProjectDialog)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 4, 1, 2)
        self.label_11 = QtWidgets.QLabel(ProjectDialog)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 2)
        self.tblParticipants = QtWidgets.QTableView(ProjectDialog)
        self.tblParticipants.setAlternatingRowColors(True)
        self.tblParticipants.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tblParticipants.setObjectName("tblParticipants")
        self.tblParticipants.horizontalHeader().setCascadingSectionResizes(False)
        self.tblParticipants.horizontalHeader().setDefaultSectionSize(100)
        self.tblParticipants.horizontalHeader().setStretchLastSection(True)
        self.tblParticipants.verticalHeader().setCascadingSectionResizes(True)
        self.tblParticipants.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tblParticipants, 11, 3, 3, 1)
        self.label_4 = QtWidgets.QLabel(ProjectDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 14, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOK = QtWidgets.QPushButton(ProjectDialog)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout.addWidget(self.btnOK)
        self.btnCancel = QtWidgets.QPushButton(ProjectDialog)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(ProjectDialog)
        self.btnCancel.clicked.connect(ProjectDialog.close)
        QtCore.QMetaObject.connectSlotsByName(ProjectDialog)

    def retranslateUi(self, ProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        ProjectDialog.setWindowTitle(_translate("ProjectDialog", "Create a new project"))
        self.lNewProject.setText(_translate("ProjectDialog", "New Project"))
        self.lblName.setText(_translate("ProjectDialog", "<Name>"))
        self.lineEditBroadcastAddress.setToolTip(_translate("ProjectDialog", "<html><head/><body><p>Enter the broadcast address of your protocol in <span style=\" font-weight:600;\">hex</span>. If you do not know what to enter here, just leave the default.</p></body></html>"))
        self.lineEditBroadcastAddress.setText(_translate("ProjectDialog", "ffff"))
        self.label_8.setText(_translate("ProjectDialog", "Description:"))
        self.lblNewPath.setText(_translate("ProjectDialog", "<html><head/><body><p><span style=\" font-style:italic;\">Note: A new directory will be created.</span></p></body></html>"))
        self.label_6.setText(_translate("ProjectDialog", "Hz"))
        self.label.setText(_translate("ProjectDialog", "Choose a path:"))
        self.btnSelectPath.setText(_translate("ProjectDialog", "..."))
        self.label_5.setText(_translate("ProjectDialog", "Sps"))
        self.label_2.setText(_translate("ProjectDialog", "Default sample rate:"))
        self.label_3.setText(_translate("ProjectDialog", "Default frequency:"))
        self.btnAddParticipant.setText(_translate("ProjectDialog", "..."))
        self.lOpenSpectrumAnalyzer.setText(_translate("ProjectDialog", "<html><head/><body><p>Tip: Open <a href=\"open_spectrum_analyzer\">spectrum analyzer</a> to find these values.</p></body></html>"))
        self.label_9.setText(_translate("ProjectDialog", "Participants:"))
        self.btnRemoveParticipant.setText(_translate("ProjectDialog", "..."))
        self.label_10.setText(_translate("ProjectDialog", "Default bandwidth:"))
        self.label_12.setText(_translate("ProjectDialog", "Hz"))
        self.label_11.setText(_translate("ProjectDialog", "Default gain:"))
        self.label_4.setText(_translate("ProjectDialog", "Broadcast address (hex):"))
        self.btnOK.setText(_translate("ProjectDialog", "Create new project"))
        self.btnCancel.setText(_translate("ProjectDialog", "Cancel"))

from urh.ui.KillerDoubleSpinBox import KillerDoubleSpinBox
