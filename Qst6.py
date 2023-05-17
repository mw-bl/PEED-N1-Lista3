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


def verificarBalanceamento(string):
    pilha = Pilha()
    caracteresAbertura = "([{"
    caracteresFechamento = ")]}"

    for caractere in string:
        if caractere in caracteresAbertura:
            pilha.push(caractere)
        elif caractere in caracteresFechamento:
            if pilha.is_empty():
                return False
            topo = pilha.pop()
            if (caractere == ")" and topo != "(") or (caractere == "}" and topo != "{") or (caractere == "]" and topo != "["):
                return False

    return pilha.is_empty()


string = input("Digite uma string contendo caracteres de abertura e fechamento: ")
if verificarBalanceamento(string):
    print("Os caracteres estão balanceados")
else:
    print("Os caracteres não estão balanceados")
