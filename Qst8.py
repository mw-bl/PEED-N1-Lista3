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

    def push(self, valor):
        no = No(valor)
        no.proximo = self.topo
        self.topo = no
        self.tamanho += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self.topo.valor
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return valor


def decimalParaHexadecimal(decimal):
    pilha = Pilha()
    digitosHexa = "0123456789ABCDEF"

    while decimal > 0:
        resto = decimal % 16
        pilha.push(digitosHexa[resto])
        decimal = decimal // 16

    if pilha.is_empty():
        pilha.push('0')

    hexadecimal = ""
    while not pilha.is_empty():
        hexadecimal += pilha.pop()

    return hexadecimal


numeroDecimal = int(input("Digite um número decimal: "))
numeroHexadecimal = decimalParaHexadecimal(numeroDecimal)
print("Número hexadecimal correspondente:", numeroHexadecimal)
