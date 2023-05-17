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


def verificaPalindromo(string):
    pilha = Pilha()
    tamanho = len(string)
    meio = tamanho // 2

    for i in range(meio):
        pilha.push(string[i])

    if tamanho % 2 == 1:
        inicio = meio + 1
    else:
        inicio = meio

    for i in range(inicio, tamanho):
        if pilha.is_empty() or string[i] != pilha.pop():
            return False

    return pilha.is_empty()


numero = input("Digite um número: ")
if verificaPalindromo(numero):
    print("A string é um número palíndromo")
else:
    print("A string não é um número palíndromo")
