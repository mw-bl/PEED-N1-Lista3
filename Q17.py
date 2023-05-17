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


def octalParaDecimal(octal):
    pilha = Pilha()
    decimal = 0
    potencia = 0

    for digito in octal:
        pilha.push(int(digito))

    while not pilha.is_empty():
        decimal += pilha.pop() * (8 ** potencia)
        potencia += 1

    return decimal


octal = input("Digite um número octal: ")

decimal = octalParaDecimal(octal)
print("Número decimal:", decimal)
