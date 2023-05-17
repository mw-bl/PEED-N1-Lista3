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


def ordenarLista(lista):
    pilha = Pilha()
    for elemento in lista:
        while not pilha.is_empty() and pilha.topo > elemento:
            lista.append(pilha.pop())
        pilha.push(elemento)
    while not pilha.is_empty():
        lista.append(pilha.pop())
    return lista


numeros = input("Digite uma lista de números separados por espaço: ")
numeros = list(map(int, numeros.split()))

numerosOrdenados = ordenarLista(numeros)
print("Números ordenados:", numerosOrdenados)
