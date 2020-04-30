class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.posicao = 0

    def tamanho_vetor(self):
        return len(self.__elementos)

    def __str__(self):
        return ' '.join([ str(i) for i in self.__elementos])

    def contem(self, elemento):
        for i in range(self.__tamanho_vetor()):
            elem = self.listar_elemento(i)
            if elem == elemento:
                return True
        return False

    def indice(self, elemento):
        for i in range(self.tamanho_vetor()):
            elem = self.listar_elemento(i)
            if elem == elemento:
                return i
        return - 1

    def inserir_elemento_posicao(self, elemento, posicao):
        #com base no vetor: [3,4,5], inserir o valor 6
        vetor_inicio = self.__elementos[:posicao] + [None] # 3, 4, [None]
        vetor_final = self.__elementos[posicao:] # 5
        vetor_inicio[len(vetor_inicio) - 1] = elemento # 3, 4, 6, 5
        self.__elementos = vetor_inicio + vetor_final # 3, 4, 6, 5
        self.__posicao += 1


    def inserir_elemento_final(self, elemento):
        if self.__posicao >= len(self.__elementos):
            self.__elementos = self.__elementos + [None]
        self.__elementos[self.posicao] = elemento
        self.posicao += 1


    def remover_elemento_indice(self, posicao):
        #com base no vetor: [3, 4, 5], remover o valor 4
        vetor_inicio = self.__elementos[:posicao] #  3
        vetor_final = self.__elementos[posicao + 1: ] #  5
        self.__elementos = vetor_inicio + vetor_final # 3, 5
        self.__elementos -= 1

    def remover_elemento(self, elemento):
        posicao = self.indice(elemento)
        self.remover_elemento_indice(posicao)

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]
