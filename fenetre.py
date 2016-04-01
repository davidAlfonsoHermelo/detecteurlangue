# -*- coding: utf-8 -*-

"""
Module implementing LangueDetect.
"""

from PyQt4  import Qt, QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4  import Qt, QtGui
import detecteurLangue
import os
import sys
import codecs
from urllib2 import urlopen

from Ui_fenetre import Ui_MainWindow

class LangueDetect(QMainWindow, Ui_MainWindow):
    """
    Detecteur de langue d'un texte.
    """
    
    def __init__(self, parent = None):
        """
        Constructeur
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        source = None
    
    @pyqtSignature("")
    def on_pushButtonParcourir_clicked(self):
        """
        Retourne le texte contenu dans un document de texte brut.
        """
        chemin = unicode(self.lineEdit.text())
        if len(chemin) > 0 :
            if chemin.startswith("http"):
                self.on_pushButtonURL_clicked()
            else:
                cheminFichier = self.lineEdit.text()
                fichier = codecs.open(cheminFichier,  "r",  "utf8").read()
                self.textEditPrTexte.setText(fichier)
    
    @pyqtSignature("")
    def on_pushButtonURL_clicked(self):
        """
        Retourne le texte aspiré de l'url.
        """
        if len(self.lineEdit.text()) > 0 : 
            url = unicode(self.lineEdit.text())
            if url.startswith("./"):
                self.on_pushButtonParcourir_clicked()
            elif url.startswith("/"):
                self.on_pushButtonParcourir_clicked()
            elif not url.startswith("https://"):
                if not url.startswith("http://"): 
                    url="http://"+url
            html = detecteurLangue.deURLATexte(url)
            self.textEditPrTexte.setText(html)
    
    @pyqtSignature("")
    def on_buttonBoxLancerDetecteur_accepted(self):
        """
        Détecteur de langue. Retourne la langue du texte aparaissant dans la case.
        """
        texte = unicode(self.textEditPrTexte.toPlainText())
        if len(texte) > 0:
            langue = detecteurLangue.langue(texte)
        self.labelReponse.setText("Le texte est probablement en "+langue)
        print langue
    
    @pyqtSignature("")
    def on_buttonBoxLancerDetecteur_rejected(self):
        """
        Ferme la fenêtre.
        """
        sys.exit(0) 

if __name__=="__main__": 
    import sys 
    app = QtGui.QApplication(sys.argv) 
    wnd = LangueDetect() 
    wnd.show() 
    sys.exit(app.exec_())
