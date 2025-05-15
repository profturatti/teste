# mathBasic.py

import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def resto(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a % b

def testePar(valor):
    return "Par" if valor % 2 == 0 else "Ímpar"

def raiz(a):
    if a < 0:
        return "Erro: Raiz de número negativo"
    return math.sqrt(a)
