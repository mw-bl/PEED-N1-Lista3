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


def verificarPalindromo(string):
    pilha = Pilha()
    tamanho = len(string)

    for i in range(tamanho // 2):
        pilha.push(string[i])

    inicio = tamanho // 2 + (tamanho % 2)
    for i in range(inicio, tamanho):
        if pilha.pop() != string[i]:
            return False

    return True


string = input("Digite uma string: ")
if verificarPalindromo(string):
    print("A string é um palíndromo")
else:
    print("A string não é um palíndromo")
