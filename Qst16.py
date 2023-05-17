class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self._topo = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def is_empty(self):
        return self.tamanho == 0

    def push(self, valor):
        no = No(valor)
        no.proximo = self._topo
        self._topo = no
        self.tamanho += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor

    def peek(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._topo.valor


def hexParaDecimal(hexadecimal):
    pilha = Pilha()
    decimal = 0
    potencia = 0

    for caractere in hexadecimal:
        if caractere.isdigit():
            pilha.push(int(caractere))
        else:
            decimal_digit = ord(caractere.upper()) - ord('A') + 10
            pilha.push(decimal_digit)

    while not pilha.is_empty():
        decimal += pilha.pop() * (16 ** potencia)
        potencia += 1

    return decimal


hexadecimal = input("Digite um número hexadecimal: ")

decimal = hexParaDecimal(hexadecimal)
print("Número decimal:", decimal)
