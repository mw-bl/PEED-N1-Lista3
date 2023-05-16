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

    def inserir(self, valor):
        no = No(valor)
        no.proximo = self._topo
        self._topo = no
        self.tamanho += 1

    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor

    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._topo.valor

def verifParenteses(expressao):
    pilha = Pilha()

    for char in expressao:
        if char == '(':
            pilha.inserir(char)
        elif char == ')':
            if pilha.is_empty():
                return False 
            pilha.remover()

    return pilha.is_empty()

expressao = input("Digite uma expressão matemática: ")
if verifParenteses(expressao):
    print("Os parênteses estão balanceados.")
else:
    print("Os parênteses estão desbalanceados.")
