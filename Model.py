class Model:
#Método construtor
    def __init__(self):
        self.vetor = []
        self.vetor2 = []

#Métodos de acesso

#Exercicio 1:
    def preencherVetor(self, num):
        self.vetor.append(num)

    def mediaTurma(self):
        soma = 0
        media = 0
        acima = 0
        for i in range(len(self.vetor)):
            soma = soma + self.vetor[i]
            i= i+1
        media = soma / len(self.vetor)

        for i in range(len(self.vetor)):
            if self.vetor[i] > media:
                acima = acima + 1
                i = i+1

        print("A media da turma ficou: {}\n{} Alunos tiveram notas acima da média".format(media, acima))

#Exercicio 3:
    def vetorQ(self):
        q = self.vetor[0]
        posicao = -1
        for i in range(len(self.vetor)):
            if q > self.vetor[i]:
                q = self.vetor[i]
                posicao = i
            i = i + 1
        print("O menor elemento digitado foi: {}\nO mesmo está na posição {} do vetor".format(q, posicao))

#Exercicio 5:
    def visualizarVetor(self):
        for i in range(len(self.vetor)):
            print("{}º número: {}\n".format(i+1,self.vetor[i]))

    def inverso(self):
        self.vetor.reverse()
        self.visualizarVetor()

#Exercicio 7:
    def mediaTemp(self):
        soma = 0
        media = 0
        abaixo = 0
        menorTemp = self.vetor[0]
        maiorTemp = self.vetor[0]

        for i in range(len(self.vetor)):
            soma = soma + self.vetor[i]
            i = i + 1
        media = soma / len(self.vetor)

        for i in range(len(self.vetor)):
            if self.vetor[i] < media:
                abaixo = abaixo + 1
            i = i + 1

        for i in range(len(self.vetor)):
            if menorTemp > self.vetor[i]:
                menorTemp = self.vetor[i]
                i = i + 1

        for i in range(len(self.vetor)):
            if maiorTemp < self.vetor[i]:
                maiorTemp = self.vetor[i]
                i = i + 1

        print("A menor temperatura registrada foi de {}°\n"
              "A maior temperatura registrada foi de {}°\n"
              "A temperatura média ficou {}°\n"
              "A quantidade de dias que a temperatura foi menor que a média foi de {} dias".format(menorTemp, maiorTemp, media, abaixo))

#Exercicio 9:
    def sortVetor(self):
        self.vetor.sort()
        self.visualizarVetor()
        self.inserirVetor()

    def inserirVetor(self):
        print("Digite um novo valor:")
        self.vetor.append(int(input()))
        self.vetor.sort()
        self.visualizarVetor()

#Exercicio 11:
    def preencherVetor2(self, num2):
        self.vetor2.append(num2)

    def compareVetor(self):
        quantidade = 0
        for i in range(len(self.vetor)):
            if self.vetor[i] == self.vetor2[i]:
                quantidade = quantidade + 1
                i = i + 1
        print("A quantidade de vezes que tivemos numeros iguais na mesma posição foi de {}".format(quantidade))

#Exercicio 13:
    def verificarVetor(self):
        posicao = 0
        posicao2 = 0
        num = 0
        for i in range(len(self.vetor)):
            for n in range(len(self.vetor)-1):
                if i == n:
                    n = n + 1
                if self.vetor[i] == self.vetor[n]:
                    num = self.vetor[i]
                    posicao = i
                    posicao2 = n
                n = n + 1
            print("o numero {} repetiu nas posições {} e {}".format(num, posicao, posicao2))
            i = i + 1