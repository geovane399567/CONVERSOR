import textwrap

# Função para converter Celsius para Fahrenheit

def celsiusParaFahrenheit():

    celsius = float(input("Informe a temperatura em Celsius: "))

    fahrenheit = (celsius * 1.8) + 32

    print(f"A temperatura covertida é: {fahrenheit:.1f} graus Fahrenheit!")

#celsiusParaFahrenheit()

# Função para converter Fahrenheit para Celsius

def fahrenheitParaCelsius():

    fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))

    celsius = (fahrenheit - 32) * (5/9) 

    print(f"A temperatura covertida é: {celsius:.1f} graus Celsius!")

#fahrenheitParaCelsius()

# Função que converte Celsius para Kelvin

def celsiusParaKelvin():

    celsius = float(input("Informe a temperatura em Celsius: "))

    kelvin = celsius + 273.15 

    print(f"A temperatura covertida é: {kelvin:.1f} graus Kelvin!")

# Função que converte Kelvin para Celsius

def kelvinParaCelsius():

    kelvin = float(input("Informe a temperatura em Kelvin: "))

    celsius =  kelvin - 273.15 

    print(f"A temperatura covertida é: {celsius:.1f} graus Celsius!")

# Função que converte Kelvin para Fahrenheit

def kelvinParaFahrenheit():

    kelvin = float(input("Informe a temperatura em Kelvin: "))

    fahrenheit = (kelvin - 273.15) * (9/5) + 32

    print(f"A temperatura covertida é: {fahrenheit:.1f} graus Fahrenheit!")

# Função que converte Fahrenheit para Kelvin

def fahrenheitParaKelvin():

    fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))

    kelvin = (fahrenheit - 32) * (5/9) + 273.15

    print(f"A temperatura covertida é: {kelvin:.1f} graus Kelvin!")





# Menu de Entrada
def menuEntrada():
    menuEntrada = """
    \n
       ########## Conversor de temperatura ########
       \n
       #######   Escolha a escala: ######

       [1]\t Celsius para Fahrenheit
       [2]\t Fahrenheit para Celsius
       [3]\t Celsius para Kelvin
       [4]\t Kelvin para Celsius
       [5]\t Kelvin para Fahrenheit
       [6]\t Fahrenheit para Kelvin 
       [7]\t Sair do programa

  """
    return input(textwrap.dedent(menuEntrada))

# Função para validar o menu de entrada

def entrada():
      
      while True:
           opcao = menuEntrada()

           if opcao == "1":
               celsiusParaFahrenheit()
           elif opcao == "2":
               fahrenheitParaCelsius()   
           elif opcao == "3":
               celsiusParaKelvin()
           elif opcao == "4":
               kelvinParaCelsius()
           elif opcao == "5":
               kelvinParaFahrenheit()
           elif opcao == "6":
               fahrenheitParaKelvin()
           elif opcao == "7":
               break
           else:
               print("Opção Inválida!") 


entrada()               
              
#####################################################################################




