import pyttsx3

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def calcular(operador, num1, num2):
    resultado = 0
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    return resultado

falar("Olá! Sou uma calculadora virtual. Como posso ajudar?")

while True:
    entrada = input("Digite a operação matemática (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        falar("Até logo!")
        break
    
    partes = entrada.split()
    if len(partes) != 3:
        falar("Entrada inválida. Por favor, tente novamente.")
        continue
    
    operador, num1, num2 = partes
    num1 = float(num1)
    num2 = float(num2)