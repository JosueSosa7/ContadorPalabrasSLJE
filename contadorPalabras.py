import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        # Carga de nuestra vista
        uic.loadUi("contadorPalabras.ui", self)
        self.btnContar.clicked.connect(self.ContarPalabras)
        
    def ContarPalabras(self):
        #Recuperar el texto 
        texto = self.edtCaracteres.text()
        
        # Separar las palabras
        textoSeparado = texto.split()
        print(textoSeparado)
        # Contar las palabras
        cantidadPalabras = len(textoSeparado)
        print("Palabras: ", cantidadPalabras)
        self.tvPalabras.setText(f"Palabras: {cantidadPalabras}")
        # Contar los caracteres
        totalCaracteres = 0
        for palabra in textoSeparado:
            totalCaracteres += len(palabra)
        self.tvCaracteres.setText(f"Caracteres: {totalCaracteres}")
        
        #Cambiar color palabras al superar las 50 palabras o caracteres
        if cantidadPalabras >= 20:
            self.tvPalabras.setStyleSheet("color: #FF0000;")
        else:
            self.tvPalabras.setStyleSheet("color: #000000;")

        if totalCaracteres >= 120:
             self.tvCaracteres.setStyleSheet("color: #FF0000;")
        else:
            self.tvCaracteres.setStyleSheet("color: #000000;")
             
app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec_())