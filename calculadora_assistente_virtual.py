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