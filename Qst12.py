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


def converterParaDecimal(string):
    pilha = Pilha()
    for caractere in string:
        if caractere.isdigit():
            pilha.push(int(caractere))
        else:
            return None

    numeroDecimal = 0
    posicao = 0
    while not pilha.is_empty():
        digito = pilha.pop()
        numeroDecimal += digito * (10 ** posicao)
        posicao += 1

    return numeroDecimal


stringNumeros = input("Digite uma string contendo números: ")

numeroDecimal = converterParaDecimal(stringNumeros)

if numeroDecimal is not None:
    print("Número decimal:", numeroDecimal)
else:
    print("Erro: A string contém caracteres inválidos")
