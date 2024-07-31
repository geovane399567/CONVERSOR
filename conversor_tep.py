from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel, QLCDNumber, QDoubleSpinBox
import sys

class temperatura(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coversor de Temperatura")
        self.setFixedSize(300, 300)

          
        self.input = QLineEdit(self)
        self.valorTemp = QLabel("Digite o valor de temperatura: ")

                
 
        self.layout = QVBoxLayout()
        self.button1 = QPushButton("Celsius -> Fahrenheit")
        self.button2 = QPushButton("Fahrenheit -> Celsius")
        self.button3 = QPushButton("Celsius -> Kelvin")
        self.button4 = QPushButton("Kelvin -> Celsius")
        self.button5 = QPushButton("Kelvin -> Fahrenheit")
        self.button6 = QPushButton("Fahrenheit -> Kelvin")

        self.resultado = QLabel(" ", self)

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

                 
        

# Inicio da funções de conversão ##########################

    def celsiusParaFahrenheit(self):
            
        if self.button1:    
            temperatura = float(self.input.text())
            resposta = (temperatura * 1.8) + 32
            self.resultado.setText(f"{resposta:.1f} graus \n  Fahrenheit!") 
        else:
            self.resultado.setText("Valor inválido! Digite um número!")             

#celsiusParaFahrenheit()


# Função para converter Fahrenheit para Celsius

    def fahrenheitParaCelsius(self):
        if self.button2:    
            temperatura = float(self.input.text()) 
            resposta = (temperatura - 32) * (5/9)
            self.resultado.setText(f"{resposta:.1f} graus \n Celsius!") 
        else:
            self.resultado.setText("Valor inválido! Digite um número!")
#fahrenheitParaCelsius()

# Função que converte Celsius para Kelvin

    def celsiusParaKelvin(self):
        if self.button3:    
            temperatura = float(self.input.text()) 
            resposta = temperatura + 273.15
            self.resultado.setText(f"{resposta:.1f} graus \n Kelvin!") 
        else:
            self.resultado.setText("Valor inválido! Digite um número!")
    

# Função que converte Kelvin para Celsius

    def kelvinParaCelsius(self):
        if self.button3:    
            temperatura = float(self.input.text()) 
            resposta = temperatura - 273.15 
            self.resultado.setText(f"{resposta:.1f} graus \n Celsius!") 
        else:
            self.resultado.setText("Valor inválido! Digite um número!")

# Função que converte Kelvin para Fahrenheit

    def kelvinParaFahrenheit(self):
        if self.button3:    
            temperatura = float(self.input.text())
            resposta = (temperatura - 273.15) * (9/5) + 32
            self.resultado.setText(f"{resposta:.1f} graus \n Fahrenheit!") 
        else:
            self.resultado.setText("Valor inválido! Digite um número!")

# Função que converte Fahrenheit para Kelvin

    def fahrenheitParaKelvin(self):
        if self.button3:    
            temperatura = float(self.input.text())
            resposta = (temperatura - 32) * (5/9) + 273.15
            self.resultado.setText(f"{resposta:.1f} graus \n Kelvin!") 
        else:
            self.resultado.setText("Valor inválido! Digite um número!")

        

        
        
        


app = QApplication(sys.argv)

objeto = temperatura()
objeto.show()
app.exec()



