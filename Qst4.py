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


def decimalParaBinario(decimal):
    pilha = Pilha()

    while decimal > 0:
        resto = decimal % 2
        pilha.push(resto)
        decimal = decimal // 2

    if pilha.is_empty():
        pilha.push(0)

    binario = ""
    while not pilha.is_empty():
        binario += str(pilha.pop())

    return binario


numeroDecimal = int(input("Digite um número decimal: "))
numeroBinario = decimalParaBinario(numeroDecimal)
print("Número binário correspondente:", numeroBinario)
