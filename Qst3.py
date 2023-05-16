class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def is_empty(self):
        return self.tamanho == 0

    def inserir(self, valor):
        no = No(valor)
        no.proximo = self.topo
        self.topo = no
        self.tamanho += 1

    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self.topo.valor
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return valor

    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self.topo.valor


def infixaParaPosfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'

    for caracter in expressao:
        if caracter in numeros:
            posfixa.append(caracter)
        elif caracter == '(':
            operadores.inserir(caracter)
        elif caracter == ')':
            while operadores.topo() != '(':
                posfixa.append(operadores.remover())
            operadores.remover()
        elif caracter in precedencia:
            while not operadores.is_empty() and operadores.topo() != '(' and precedencia[caracter] <= precedencia[operadores.topo()]:
                posfixa.append(operadores.remover())
            operadores.inserir(caracter)

    while not operadores.is_empty():
        posfixa.append(operadores.remover())

    return ''.join(posfixa)


def calcular_posfixa(posfixa):
    pilha = Pilha()

    for elemento in posfixa:
        if elemento.isnumeric():
            pilha.inserir(int(elemento))
        elif elemento in ('+', '-', '*', '/'):
            if len(pilha) < 2:
                raise ValueError("Expressão inválida")

            b = pilha.remover()
            a = pilha.remover()

            if elemento == '+':
                resultado = a + b
            elif elemento == '-':
                resultado = a - b
            elif elemento == '*':
                resultado = a * b
            elif elemento == '/':
                resultado = a / b

            pilha.inserir(resultado)
        else:
            raise ValueError("Expressão inválida")

    if len(pilha) != 1:
        raise ValueError("Expressão inválida")

    return pilha.topo()


expressao = input("Digite a expressão matemática: ")
posfixa = infixaParaPosfixa(expressao)
resultado = calcularPosfixa(posfixa)

print("Expressão posfixa:", posfixa)
print("Resultado:", resultado)
