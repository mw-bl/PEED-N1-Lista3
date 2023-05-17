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


def verificaExpressao(expressao):
    pilha = Pilha()
    operadores = "+-*/"
    abertura = "([{"
    fechamento = ")]}"

    for caractere in expressao:
        if caractere in abertura:
            pilha.push(caractere)
        elif caractere in fechamento:
            if pilha.is_empty():
                return False
            topo = pilha.pop()
            if (caractere == ")" and topo != "(") or (caractere == "}" and topo != "{") or (caractere == "]" and topo != "["):
                return False
        elif caractere in operadores:
            if pilha.is_empty() or pilha.topo in abertura:
                return False

    return pilha.is_empty()


expressao = input("Digite uma expressão aritmética: ")
if verificaExpressao(expressao):
    print("A expressão é válida")
else:
    print("A expressão não é válida")
