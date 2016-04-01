# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/dah/ROTTENWORK/MASTER_TAL/Cours_docs_coursS2/PA2_Programmation_et_algorithmie_2/034interfaceGraphique/projetEric4/fenetre.ui'
#
# Created: Fri Apr  1 18:31:27 2016
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.resize(574, 362)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.labelbienvenue = QtGui.QLabel(self.centralWidget)
        self.labelbienvenue.setGeometry(QtCore.QRect(9, 67, 717, 17))
        self.labelbienvenue.setScaledContents(True)
        self.labelbienvenue.setObjectName(_fromUtf8("labelbienvenue"))
        self.labelUrlOuCheminFichier = QtGui.QLabel(self.centralWidget)
        self.labelUrlOuCheminFichier.setGeometry(QtCore.QRect(10, 10, 551, 17))
        self.labelUrlOuCheminFichier.setObjectName(_fromUtf8("labelUrlOuCheminFichier"))
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 351, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButtonParcourir = QtGui.QPushButton(self.centralWidget)
        self.pushButtonParcourir.setGeometry(QtCore.QRect(369, 30, 85, 27))
        self.pushButtonParcourir.setObjectName(_fromUtf8("pushButtonParcourir"))
        self.pushButtonURL = QtGui.QPushButton(self.centralWidget)
        self.pushButtonURL.setGeometry(QtCore.QRect(460, 30, 85, 27))
        self.pushButtonURL.setObjectName(_fromUtf8("pushButtonURL"))
        self.buttonBoxLancerDetecteur = QtGui.QDialogButtonBox(self.centralWidget)
        self.buttonBoxLancerDetecteur.setGeometry(QtCore.QRect(370, 290, 176, 27))
        self.buttonBoxLancerDetecteur.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBoxLancerDetecteur.setObjectName(_fromUtf8("buttonBoxLancerDetecteur"))
        self.labelReponse = QtGui.QLabel(self.centralWidget)
        self.labelReponse.setGeometry(QtCore.QRect(10, 320, 501, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Sans [unknown]"))
        font.setPointSize(11)
        self.labelReponse.setFont(font)
        self.labelReponse.setScaledContents(False)
        self.labelReponse.setObjectName(_fromUtf8("labelReponse"))
        self.textEditPrTexte = QtGui.QTextEdit(self.centralWidget)
        self.textEditPrTexte.setGeometry(QtCore.QRect(10, 90, 531, 181))
        self.textEditPrTexte.setObjectName(_fromUtf8("textEditPrTexte"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.labelbienvenue.setText(_translate("MainWindow", "Vous pouvez écrire ou coller un texte.", None))
        self.labelUrlOuCheminFichier.setText(_translate("MainWindow", "Bienvenue au détecteur de langues. Collez un chemin de fichier ou un lien vers une page web.", None))
        self.lineEdit.setText(_translate("MainWindow", "http://www.legorafi.fr/", None))
        self.pushButtonParcourir.setText(_translate("MainWindow", "Parcourir", None))
        self.pushButtonURL.setText(_translate("MainWindow", "Page Web", None))
        self.labelReponse.setText(_translate("MainWindow", ".", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

