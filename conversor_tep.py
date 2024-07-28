from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel, QLCDNumber, QDoubleSpinBox
import sys
from PySide6.QtCore import Qt

class temperatura(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coversor de Temperatura")
        self.setFixedSize(300, 300)

           
        self.input = QLineEdit(self)
        self.valorTemp = QLabel("Digite o valor de temperatura: ")
        self.resultado = QLabel(" ", self)
        
        self.layout = QVBoxLayout()
        self.button1 = QPushButton("Celsius -> Fahrenheit")
        self.layout = QVBoxLayout()
        self.button2 = QPushButton("Fahrenheit -> Celsius")
        self.layout = QVBoxLayout()
        self.button3 = QPushButton("Celsisu -> Kelvin")
        self.layout = QVBoxLayout()
        self.button4 = QPushButton("Kelvin -> Celsius")
        self.layout = QVBoxLayout()
        self.button5 = QPushButton("Kelvin -> Fahrenheit")
        self.layout = QVBoxLayout()
        self.button6 = QPushButton("Fahrenheit -> Kelvin")

       # self.layout = QVBoxLayout()

        self.layout.addWidget(self.valorTemp)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5)
        self.layout.addWidget(self.button6)

        self.container = QFrame()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        self.button1.clicked.connect(self.celsiusParaFahrenheit)
        self.button2.clicked.connect(self.fahrenheitParaCelsius)
        self.button3.clicked.connect(self.celsiusParaKelvin)
        self.button4.clicked.connect(self.kelvinParaCelsius)
        self.button5.clicked.connect(self.kelvinParaFahrenheit)
        self.button6.clicked.connect(self.fahrenheitParaKelvin)

        self.input.textChanged.connect(self.celsiusParaFahrenheit)
        
        

# Inicio da funções de conversão ##########################

    def celsiusParaFahrenheit(self):
        self.texto = self.input.text()
        temperatura = float(self.texto)
        if self.button1:
            resposta = (temperatura * 1.8) + 32
            self.resultado.setText(f"A temperatura covertida é: {resposta:.1f} graus Fahrenheit!") 
                      

#celsiusParaFahrenheit()

# Função para converter Fahrenheit para Celsius

    def fahrenheitParaCelsius(self):
        self.texto = self.input.text()
        temperatura = float(self.texto) 
        if self.button2:     
            resposta = (temperatura - 32) * (5/9)
            self.resultado.setText(f"A temperatura covertida é: {resposta:.1f} graus Celsius!")

#fahrenheitParaCelsius()

# Função que converte Celsius para Kelvin

    def celsiusParaKelvin(self):
        self.texto = self.input.text()
        temperatura = float(self.texto) 
        if self.button3:
            reposta = temperatura + 273.15
            self.resultado.setText(f"A temperatura covertida é: {reposta:.1f} graus Kelvin!")

# Função que converte Kelvin para Celsius

    def kelvinParaCelsius(self):
        self.texto = self.input.text()
        temperatura = float(self.texto)
        if self.button4:
            resposta = temperatura - 273.15 
            self.resultado.setText(f"A temperatura covertida é: {resposta:.1f} graus Celsius!")

# Função que converte Kelvin para Fahrenheit

    def kelvinParaFahrenheit(self):
        self.texto = self.input.text()
        temperatura = float(self.texto)
        if self.button5:
            resposta = (temperatura - 273.15) * (9/5) + 32
            self.resultado.setText(f"A temperatura covertida é: {resposta:.1f} graus Fahrenheit!")

# Função que converte Fahrenheit para Kelvin

    def fahrenheitParaKelvin(self):
        self.texto = self.input.text()
        temperatura = float(self.texto)
        if self.button6:
            resposta = (temperatura - 32) * (5/9) + 273.15
            self.resultado.setText(f"A temperatura covertida é: {resposta:.1f} graus Kelvin!")



app = QApplication(sys.argv)

objeto = temperatura()
objeto.show()
app.exec()



