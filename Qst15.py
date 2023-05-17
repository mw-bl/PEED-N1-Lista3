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


def decimalParaBinario(decimal):
    pilha = Pilha()

    while decimal > 0:
        pilha.push(decimal % 2)
        decimal //= 2

    binario = ""
    while not pilha.is_empty():
        binario += str(pilha.pop())

    return binario


numero = input("Digite um número decimal: ")

if numero.isdigit():
    decimal = int(numero)
    binario = decimalParaBinario(decimal)
    print("Número binário:", binario)
else:
    print("Entrada inválida. Digite um número decimal válido.")
