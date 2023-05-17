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


def binarioParaHexadecimal(binario):
    pilha = Pilha()
    hexadecimal = ""

    if not all(digito in '01' for digito in binario):
        return None

    for digito in binario:
        pilha.push(int(digito))

    while len(pilha) % 4 != 0:
        pilha.push(0)

    while not pilha.is_empty():
        valor = 0
        for _ in range(4):
            valor = valor * 2 + pilha.pop()
        if valor < 10:
            hexadecimal = str(valor) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + valor - 10) + hexadecimal

    return hexadecimal


numeroBinario = input("Digite um número binário: ")

numeroHexadecimal = binarioParaHexadecimal(numeroBinario)

if numeroHexadecimal is None:
    print("Entrada inválida. Digite um número binário válido.")
else:
    print("Número hexadecimal:", numeroHexadecimal)
