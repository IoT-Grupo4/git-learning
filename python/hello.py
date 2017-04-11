import json
from math import sin, cos, pi
# importa todos os pacotes do módulo.
# https://docs.python.org/3/library/os.html
from sys import platform

print('hello world in python using {}!'.format(platform))


def factorial(n):
    """Retorna o fatorial de N"""
    if n==1:
        return n
    else:
        return n*factorial(n-1 )

def fibonacci(n):
    """Retorna uma lista com os N primeiros números da
    sequencia de Fibonacci"""
    fibonacci_list = [0,1] # uma lista
    for i in range(2,n):
        fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i-2] )

    return fibonacci_list

class Poligono(object):
    """Poligono de n lados"""
    def __init__(self, n, tamanho):
        super(Poligono, self).__init__()
        self.n = n
        self.tamanho = tamanho

    def raio(self):
        # self.tamanho/ (2*sin(180/self.n))
        return self.tamanho/ (2*sin(pi/self.n))

    def apótema(self):
        return self.raio()*cos(pi/self.n)

    def semiperímetro(self):
        return self.n*self.tamanho/2.0
        
    def área(self):
        return self.semiperímetro()*self.apótema()

    def __str__(self):
        dados = {}  # um dicionário
        dados['área'] = self.área()
        dados['semiperímetro'] = self.semiperímetro()
        dados['apótema'] = self.apótema()

        return '{}'.format(dados)

    def __add__(self, other):
        return self.área() + other.área()


    def __lt__(self, other):
        # <
        pass
    def __le__(self, other):
        # <=
        pass
    def __eq__(self, other):
        # ==
        pass
    def __ne__(self, other):
        # !=
        pass
    def __gt__(self, other):
        # >
        pass
    def __ge__(self, other):
        # >=
        pass


class Quadrado(Poligono):
    """Poligono de 4 lados"""
    def __init__(self, tamanho):
        super(Quadrado, self).__init__(n=4,tamanho=tamanho)
        self.tamanho = tamanho
        

n = int(input('Entre um número: '))
print ("fatorial de {} = {}".format( n, factorial(n)))
print('Fibonacci de {} = {}'.format(n, fibonacci(n)))

poli = Poligono(n,2)

# imprimindo dado formatado
print('A área do poligono de {} lados de tamanho 2 é: {:.2f}'.format(n,poli.área()))

# imprimindo saída padrão do objeto
print(poli)

# quadrado de lado n
quadrado = Quadrado(n)

print(quadrado)
print("A soma das áreas é:", quadrado + poli)

# imprimindo atributos do objeto como um JSON
print(json.dumps(poli.__dict__))
print(json.dumps(quadrado.__dict__))