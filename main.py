# coding: utf-8

from PyQt5 import QtWidgets, QtCore, QtGui, QtPrintSupport
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QApplication, QPushButton, QBoxLayout, QDoubleSpinBox)


# import MyForm

class Diagnost(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # self.ui = MyForm.Ui_MyForm()
        # self.ui.setupUi(self)
        # self.init_signals()
        self.setupUi(self)

    def setupUi(self, MyForm):
        MyForm.setObjectName("MyForm")
        MyForm.resize(906, 722)
        self.layoutWidget = QtWidgets.QWidget(MyForm)
        self.layoutWidget.setGeometry(QtCore.QRect(512, 11, 390, 701))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Result = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.Result.setObjectName("Result")
        self.verticalLayout.addWidget(self.Result)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ResultButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ResultButton.clicked.connect(self.on_click)
        # self.ResultButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ResultButton.setFont(font)
        self.ResultButton.setObjectName("ResultButton")
        self.horizontalLayout.addWidget(self.ResultButton)
        self.SbrosButton = QtWidgets.QPushButton(self.layoutWidget)
        self.SbrosButton.clicked.connect(self.on_clear)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SbrosButton.setFont(font)
        self.SbrosButton.setObjectName("SbrosButton")
        self.horizontalLayout.addWidget(self.SbrosButton)
        self.SaveButton = QtWidgets.QPushButton(self.layoutWidget)
        self.SaveButton.clicked.connect(self.on_save)
        self.SaveButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SaveButton.setFont(font)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout.addWidget(self.SaveButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(MyForm)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 210, 491, 116))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Antropometric_data = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Antropometric_data.setFont(font)
        self.Antropometric_data.setObjectName("Antropometric_data")
        self.verticalLayout_8.addWidget(self.Antropometric_data)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(14)
        self.formLayout.setObjectName("formLayout")
        self.Weight = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Weight.setFont(font)
        self.Weight.setObjectName("Weight")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Weight)
        self.Weight_line = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Weight_line.setPlaceholderText("Например: 80")
        self.Weight_line.setObjectName("Weight_line")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Weight_line)
        self.Grow = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Grow.setFont(font)
        self.Grow.setObjectName("Grow")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Grow)
        self.Grow_line = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Grow_line.setPlaceholderText("Например: 180")
        self.Grow_line.setObjectName("Grow_line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Grow_line)
        self.IMT = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.IMT.setFont(font)
        self.IMT.setObjectName("IMT")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.IMT)
        self.IMT_Line = QtWidgets.QLineEdit(self.layoutWidget1)
        self.IMT_Line.setPlaceholderText("Результат появится автоматически")
        self.IMT_Line.setObjectName("IMT_Line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.IMT_Line)
        self.verticalLayout_8.addLayout(self.formLayout)
        self.layoutWidget2 = QtWidgets.QWidget(MyForm)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 330, 491, 232))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Problems = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Problems.setFont(font)
        self.Problems.setObjectName("Problems")
        self.verticalLayout_11.addWidget(self.Problems)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Diabet_nefropatia = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Diabet_nefropatia.setFont(font)
        self.Diabet_nefropatia.setObjectName("Diabet_nefropatia")
        self.verticalLayout_10.addWidget(self.Diabet_nefropatia)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setVerticalSpacing(14)
        self.formLayout_3.setObjectName("formLayout_3")
        self.Kreatin = QtWidgets.QLabel(self.layoutWidget2)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.Kreatin.setFont(font)
        self.Kreatin.setObjectName("Kreatin")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Kreatin)
        self.Kreatin_line = QtWidgets.QLineEdit(self.layoutWidget2)
        self.Kreatin_line.setPlaceholderText("Например: 90")
        self.Kreatin_line.setObjectName("Kreatin_line")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Kreatin_line)
        self.SKF = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SKF.setFont(font)
        self.SKF.setObjectName("SKF")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.SKF)
        self.SKF_line = QtWidgets.QLineEdit(self.layoutWidget2)
        self.SKF_line.setPlaceholderText("Результат появится автоматически")
        self.SKF_line.setObjectName("SKF_line")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SKF_line)
        self.MAU = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.MAU.setFont(font)
        self.MAU.setObjectName("MAU")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.MAU)
        self.MAU_Line = QtWidgets.QLineEdit(self.layoutWidget2)
        self.MAU_Line.setPlaceholderText("Например: 30")
        self.MAU_Line.setObjectName("MAU_Line")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.MAU_Line)
        self.verticalLayout_10.addLayout(self.formLayout_3)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.verticalLayout_9.addLayout(self.verticalLayout_11)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Diabet_retinopatia = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Diabet_retinopatia.setFont(font)
        self.Diabet_retinopatia.setObjectName("Diabet_retinopatia")
        self.horizontalLayout_3.addWidget(self.Diabet_retinopatia)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Neproferativnaya_radioButton = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Neproferativnaya_radioButton.setFont(font)
        self.Neproferativnaya_radioButton.setObjectName("Neproferativnaya_radioButton")
        self.verticalLayout_2.addWidget(self.Neproferativnaya_radioButton)
        self.Preproliferativnaya_radioButton = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Preproliferativnaya_radioButton.setFont(font)
        self.Preproliferativnaya_radioButton.setObjectName("Preproliferativnaya_radioButton")
        self.verticalLayout_2.addWidget(self.Preproliferativnaya_radioButton)
        self.Proliferativnaya_radioButton = QtWidgets.QRadioButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Proliferativnaya_radioButton.setFont(font)
        self.Proliferativnaya_radioButton.setObjectName("Proliferativnaya_radioButton")
        self.verticalLayout_2.addWidget(self.Proliferativnaya_radioButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.layoutWidget3 = QtWidgets.QWidget(MyForm)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 569, 496, 54))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Diabet_Polineyroptia = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Diabet_Polineyroptia.setFont(font)
        self.Diabet_Polineyroptia.setObjectName("Diabet_Polineyroptia")
        self.horizontalLayout_2.addWidget(self.Diabet_Polineyroptia)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Nignie_Konechnosti_radioButton = QtWidgets.QRadioButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Nignie_Konechnosti_radioButton.setFont(font)
        self.Nignie_Konechnosti_radioButton.setObjectName("Nignie_Konechnosti_radioButton")
        self.verticalLayout_3.addWidget(self.Nignie_Konechnosti_radioButton)
        self.Nignie_Verhnie_Konechnosti_radioButton = QtWidgets.QRadioButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Nignie_Verhnie_Konechnosti_radioButton.setFont(font)
        self.Nignie_Verhnie_Konechnosti_radioButton.setObjectName("Nignie_Verhnie_Konechnosti_radioButton")
        self.verticalLayout_3.addWidget(self.Nignie_Verhnie_Konechnosti_radioButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.Diagnoz = QtWidgets.QLabel(MyForm)
        self.Diagnoz.setGeometry(QtCore.QRect(13, 120, 86, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Diagnoz.setFont(font)
        self.Diagnoz.setObjectName("Diagnoz")
        self.SDS = QtWidgets.QLabel(MyForm)
        self.SDS.setGeometry(QtCore.QRect(11, 660, 51, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SDS.setFont(font)
        self.SDS.setObjectName("SDS")
        self.layoutWidget4 = QtWidgets.QWidget(MyForm)
        self.layoutWidget4.setGeometry(QtCore.QRect(260, 630, 214, 80))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Ichemia_Form_radioButton = QtWidgets.QRadioButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Ichemia_Form_radioButton.setFont(font)
        self.Ichemia_Form_radioButton.setObjectName("Ichemia_Form_radioButton")
        self.verticalLayout_4.addWidget(self.Ichemia_Form_radioButton)
        self.Nefro_Ichemia_Form_radioButton = QtWidgets.QRadioButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Nefro_Ichemia_Form_radioButton.setFont(font)
        self.Nefro_Ichemia_Form_radioButton.setObjectName("Nefro_Ichemia_Form_radioButton")
        self.verticalLayout_4.addWidget(self.Nefro_Ichemia_Form_radioButton)
        self.Nefropatia_Form_radioButton = QtWidgets.QRadioButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Nefropatia_Form_radioButton.setFont(font)
        self.Nefropatia_Form_radioButton.setObjectName("Nefropatia_Form_radioButton")
        self.verticalLayout_4.addWidget(self.Nefropatia_Form_radioButton)
        self.layoutWidget5 = QtWidgets.QWidget(MyForm)
        self.layoutWidget5.setGeometry(QtCore.QRect(12, 146, 475, 24))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Sugar_Diabet = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Sugar_Diabet.setFont(font)
        self.Sugar_Diabet.setObjectName("Sugar_Diabet")
        self.horizontalLayout_4.addWidget(self.Sugar_Diabet)
        spacerItem = QtWidgets.QSpacerItem(78, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.Sugar_Diabet_First_Type_radioButton = QtWidgets.QRadioButton(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Sugar_Diabet_First_Type_radioButton.setFont(font)
        self.Sugar_Diabet_First_Type_radioButton.setObjectName("Sugar_Diabet_First_Type_radioButton")
        self.horizontalLayout_4.addWidget(self.Sugar_Diabet_First_Type_radioButton)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.Sugar_Diabet_Second_Type_radioButton = QtWidgets.QRadioButton(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Sugar_Diabet_Second_Type_radioButton.setFont(font)
        self.Sugar_Diabet_Second_Type_radioButton.setObjectName("Sugar_Diabet_Second_Type_radioButton")
        self.horizontalLayout_4.addWidget(self.Sugar_Diabet_Second_Type_radioButton)
        self.layoutWidget6 = QtWidgets.QWidget(MyForm)
        self.layoutWidget6.setGeometry(QtCore.QRect(10, 11, 491, 104))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.Pacient = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Pacient.setFont(font)
        self.Pacient.setObjectName("Pacient")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Pacient)
        self.FIO = QtWidgets.QLabel("", self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.FIO.setFont(font)
        self.FIO.setObjectName("FIO")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.FIO)
        self.FIO_line = QtWidgets.QLineEdit(self.layoutWidget6)
        self.FIO_line.setPlaceholderText("Например: Иванов Иван Иванович")
        self.newFIO_line = str(self.FIO_line)
        self.FIO_line.setObjectName("FIO_line")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.FIO_line)
        self.DateBirth = QtWidgets.QLabel("", self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DateBirth.setFont(font)
        self.DateBirth.setObjectName("DateBirth")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.DateBirth)
        self.DateBirth_line = QtWidgets.QLineEdit(self.layoutWidget6)
        self.DateBirth_line.setPlaceholderText("Например: 64")
        self.DateBirth_line.setObjectName("DateBirth_line")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.DateBirth_line)
        self.verticalLayout_12.addLayout(self.formLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Sex = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Sex.setFont(font)
        self.Sex.setObjectName("Sex")
        self.horizontalLayout_7.addWidget(self.Sex)
        spacerItem2 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.Male_radioButton = QtWidgets.QRadioButton(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Male_radioButton.setFont(font)
        self.Male_radioButton.setObjectName("Male_radioButton")
        self.horizontalLayout_7.addWidget(self.Male_radioButton)
        self.Female_radioButton = QtWidgets.QRadioButton(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Female_radioButton.setFont(font)
        self.Female_radioButton.setObjectName("Female_radioButton")
        self.horizontalLayout_7.addWidget(self.Female_radioButton)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.widget = QtWidgets.QWidget(MyForm)
        self.widget.setGeometry(QtCore.QRect(11, 180, 462, 26))
        self.widget.setObjectName("widget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Hard_problems = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Hard_problems.setFont(font)
        self.Hard_problems.setObjectName("Hard_problems")
        self.horizontalLayout_6.addWidget(self.Hard_problems)
        spacerItem3 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.HardProblems_Yes_radioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.HardProblems_Yes_radioButton.setFont(font)
        self.HardProblems_Yes_radioButton.setObjectName("HardProblems_Yes_radioButton")
        self.horizontalLayout_5.addWidget(self.HardProblems_Yes_radioButton)
        spacerItem4 = QtWidgets.QSpacerItem(48, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.HardProblems_No_radioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.HardProblems_No_radioButton.setFont(font)
        self.HardProblems_No_radioButton.setObjectName("HardProblems_No_radioButton")
        self.horizontalLayout_5.addWidget(self.HardProblems_No_radioButton)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.Diagnoz.raise_()
        self.SDS.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.Hard_problems.raise_()

        self.retranslateUi(MyForm)
        QtCore.QMetaObject.connectSlotsByName(MyForm)

    def retranslateUi(self, MyForm):
        _translate = QtCore.QCoreApplication.translate
        MyForm.setWindowTitle(_translate("MyForm", "Form"))
        self.ResultButton.setText(_translate("MyForm", "Получить результат"))
        self.SbrosButton.setText(_translate("MyForm", "Сброс"))
        self.SaveButton.setText(_translate("MyForm", "Сохранить в файл"))
        self.Antropometric_data.setText(_translate("MyForm", "III. Антропометрические данные"))
        self.Weight.setText(_translate("MyForm", "1. Вес (кг):"))
        self.Grow.setText(_translate("MyForm", "2. Рост (cм):"))
        self.IMT.setText(_translate("MyForm", "3. ИМТ:"))
        self.Problems.setText(_translate("MyForm", "IV. Осложнения:"))
        self.Diabet_nefropatia.setText(_translate("MyForm", "1.Диабетическая нефропатия:"))
        self.Kreatin.setText(_translate("MyForm", "а) Креатинин (ммоль/л):"))
        self.SKF.setText(_translate("MyForm", "б) СКФ (мл/мин):"))
        self.MAU.setText(_translate("MyForm", "в) МАУ (мг):"))
        self.Diabet_retinopatia.setText(_translate("MyForm", "2. Диабетическая ретинопатия:"))
        self.Neproferativnaya_radioButton.setText(_translate("MyForm", "Непролиферативная"))
        self.Preproliferativnaya_radioButton.setText(_translate("MyForm", "Препролиферативная"))
        self.Proliferativnaya_radioButton.setText(_translate("MyForm", "Пролиферативная"))
        self.Diabet_Polineyroptia.setText(_translate("MyForm", "3. Диабетическая полинейропатия:"))
        self.Nignie_Konechnosti_radioButton.setText(_translate("MyForm", "Нижних конечностей"))
        self.Nignie_Verhnie_Konechnosti_radioButton.setText(_translate("MyForm", "Нижних и верхних конечностей"))
        self.Diagnoz.setText(_translate("MyForm", "II. Диагноз"))
        self.SDS.setText(_translate("MyForm", "4. СДС:"))
        self.Ichemia_Form_radioButton.setText(_translate("MyForm", "Ишемическая форма"))
        self.Nefro_Ichemia_Form_radioButton.setText(_translate("MyForm", "Нейроишемическая форма"))
        self.Nefropatia_Form_radioButton.setText(_translate("MyForm", "Нейропатическая форма"))
        self.Sugar_Diabet.setText(_translate("MyForm", "1. Основной: сахарный диабет:"))
        self.Sugar_Diabet_First_Type_radioButton.setText(_translate("MyForm", "1 типа"))
        self.Sugar_Diabet_Second_Type_radioButton.setText(_translate("MyForm", "2 типа"))
        self.Pacient.setText(_translate("MyForm", "I. Пациент"))
        self.FIO.setText(_translate("MyForm", "1. ФИО:"))
        self.DateBirth.setText(_translate("MyForm", "2. Полных лет:"))
        self.Sex.setText(_translate("MyForm", "3. Пол:"))
        self.Male_radioButton.setText(_translate("MyForm", "Мужской"))
        self.Female_radioButton.setText(_translate("MyForm", "Женский"))
        self.Hard_problems.setText(_translate("MyForm", "2. Наличие тяжелых осложнений:"))
        self.HardProblems_Yes_radioButton.setText(_translate("MyForm", "Да"))
        self.HardProblems_No_radioButton.setText(_translate("MyForm", "Нет"))

    #
    def init_signals(self):
        self.ResultButton.clicked.connect(self.on_click)
        self.SbrosButton.clicked.connect(self.on_clear)
        #     self.SaveButton.clicked.connect(self.on_clear)
        # self.srcAmount.valueChanged.connect(self.change_value)
        # self.resultAmount.valueChanged.connect(self.change_value)

    def on_click(self):
        name = self.FIO_line.text()
        birthdate = self.DateBirth_line.text()
        grow = self.Grow_line.text()
        weight = self.Weight_line.text()
        imt = round(float(weight) / (float(grow) / 100) ** 2, 1)
        kreatinin = self.Kreatin_line.text()
        mau = self.MAU_Line.text()

        if self.Sugar_Diabet_First_Type_radioButton.isChecked() == True:
            sugar = 'сахарный диабет 1 типа'
        else:
            sugar = 'сахарный диабет 2 типа'

        if self.HardProblems_Yes_radioButton.isChecked() == True:
            problems = True
        else:
            problems = False

        if int(self.DateBirth_line.text()) <= 44 and problems == False:
            HBA1C = 6.5
        elif int(self.DateBirth_line.text()) <= 44 and problems == True:
            HBA1C = 7.0
        elif int(self.DateBirth_line.text()) > 44 and int(self.DateBirth_line.text()) < 60 and problems == False:
            HBA1C = 7.0
        elif int(self.DateBirth_line.text()) > 44 and int(self.DateBirth_line.text()) < 60 and problems == True:
            HBA1C = 7.5
        elif int(self.DateBirth_line.text()) > 60 and problems == False:
            HBA1C = 7.5
        elif int(self.DateBirth_line.text()) > 60 and problems == True:
            HBA1C = 8.0
        else:
            HBA1C = "ОШИБКА"

        if imt < 18:
            imt_text = 'Дефицит массы тела.'
        elif imt >= 18 and imt < 25:
            imt_text = ''
        elif imt >= 25 and imt < 30:
            imt_text = 'Избыточная масса тела.'
        elif imt >= 30 and imt < 35:
            imt_text = "Ожирение I степени."
        elif imt >= 35 and imt < 40:
            imt_text = "Ожирение II степени."
        elif imt >= 40:
            imt_text = "Ожирение III степени (морбидное)."
        else:
            imt_text = 'Ошибка'

        hbpfor = ((140 - int(birthdate)) * float(weight)) / float(kreatinin)

        if self.Male_radioButton.isChecked() == True:
            hbpfor = round(float(hbpfor * 1.23), 2)
        elif self.Male_radioButton.isChecked() == False:
            hbpfor = round(float(hbpfor * 1.05), 2)

        if hbpfor >= 90:
            hbp = "C1"
        elif hbpfor >= 60 and hbpfor < 90:
            hbp = 'C2'
        elif hbpfor >= 45 and hbpfor < 60:
            hbp = "C3a"
        elif hbpfor >= 30 and hbpfor < 45:
            hbp = "C3б"
        elif hbpfor >= 15 and hbpfor < 30:
            hbp = 'C4'
        elif hbpfor < 15:
            hbp = 'C5'
        else:
            hbp = 'ОШИБКА'

        if self.Preproliferativnaya_radioButton.isChecked() == True:
            retinotype = "препролиферативная"
        elif self.Neproferativnaya_radioButton.isChecked() == True:
            retinotype = "непроферативная"
        elif self.Proliferativnaya_radioButton.isChecked() == True:
            retinotype = "пролиферативная"
        else:
            retinotype = ''

        if self.Nignie_Konechnosti_radioButton.isChecked() == True:
            polyneirotype = 'нижних конечностей'
        elif self.Nignie_Verhnie_Konechnosti_radioButton.isChecked() == True:
            polyneirotype = 'нижних и верхних конечностей'
        else:
            polyneirotype = ''

        if self.Nefro_Ichemia_Form_radioButton.isChecked() == True:
            sds = "СДС. Нейроишемическая форма"
        elif self.Ichemia_Form_radioButton.isChecked() == True:
            sds = 'СДС. Ишемическая форма'
        elif self.Nefropatia_Form_radioButton.isChecked() == True:
            sds = 'СДС. Нейропатическая форма'
        else:
            polyneirotype = ''

        if int(mau) < 30:
            mau_text = 'A1'
        elif int(mau) >= 30 and int(mau) < 300:
            mau_text = "А2"
        elif int(mau) >= 300:
            mau_text = "A3"
        else:
            mau_text = "ОШИБКА"

        result = str(
            str(name) + str('\nПолных лет: ') + str(birthdate)
            + ('\nДиагноз')
            + ('\nОсновной: ') + str(sugar)
            + ('\nЦелевой HBA1C до ') + str(HBA1C) + ('%. ') + str(imt_text)
            + ('\nОсложнения:') + ('Диабетическая нефропатия. ХБП: ') + str(hbp) + str(mau_text)
            + ('\nДиабетичекая ') + str(retinotype) + (' ретинопатия:')
            + ('\nДиабетическая полинейропатия ') + '\n' + str(polyneirotype) + ".\n"
            + str(sds))

        self.Result.setPlainText(result)
        self.Result.zoomIn(range=3)

        skf_result = str(hbpfor)
        self.SKF_line.setText(skf_result)
        imt_result = str(imt)
        self.IMT_Line.setText(imt_result)

    def on_clear(self):
        self.Result.clear()
        self.FIO_line.clear()
        self.DateBirth_line.clear()
        self.Grow_line.clear()
        self.Weight_line.clear()
        self.IMT_Line.clear()
        self.Kreatin_line.clear()
        self.SKF_line.clear()
        self.MAU_Line.clear()
        # self.Female_radioButton.setCheckable(False)
        #
        # self.Male_radioButton.setCheckable(False)
        # self.Female_radioButton.setCheckable(True)
        # self.Male_radioButton.setCheckable(True)

    def on_save(self):
        printer = QtPrintSupport.QPrinter()
        printer.setOutputFileName('Диагноз.pdf')
        painter = QtGui.QPainter()
        painter.begin(printer)
        pen = QtGui.QPen(QtGui.QColor(QtCore.Qt.blue), 5, style=QtCore.Qt.DotLine)
        painter.setPen(pen)
        painter.setBrush(QtCore.Qt.NoBrush)
        painter.drawRect(0, 0, printer.width(), printer.height())
        color = QtGui.QColor(QtCore.Qt.black)
        painter.setPen(QtGui.QPen(color))
        painter.setBrush(QtGui.QBrush(color))
        font = QtGui.QFont('Verdana', pointSize=24)
        painter.setFont(font)
        painter.drawText(10, printer.height() // 2 - 100, printer.width() - 20, 50,
                         QtCore.Qt.AlignJustify | QtCore.Qt.TextDontClip, 'Диагноз пациента')
        # printer.setPageOrientation(QtGui.QPageLayout.Landscape)
        # printer.newPage()
        # pixmap = QtGui.QPixmap('img.jpg')
        # pixmap = pixmap.scaled(printer.width(), printer.height(), aspectRatioMode = QtCore.Qt.KeepAspectRatio)
        # painter.drawPixmap(0,0,pixmap)
        painter.end()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Diagnost()
    window.setWindowTitle('Диагност 1.0')
    window.setWindowOpacity(0.95)  # Задали небольшую прозрачность главного экрана
    pal = window.palette()
    pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                 QtGui.QColor("#98FF98"))  # задали background-color (Зеленая мята)
    window.setPalette(pal)
    window.resize(913, 722)
    window.show()
    sys.exit(app.exec_())
