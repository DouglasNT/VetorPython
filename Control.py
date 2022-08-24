from Model import Model

class Control:
    def __init__(self):
        self.model = Model()
        self.opcao = -1

    def menu(self):
        print("\nEscolha umas das opções abaixo: \n\n"+
              "1. Exercicio 1\n"+
              "2. Exercicio 3\n"+
              "3. Exercicio 5\n"+
              "4. Exercicio 7\n"+
              "5. Exercicio 9\n"+
              "6. Exercicio 11\n"+
              "7. Exercicio 13\n"+
              "0. Sair")

        self.opcao = int(input())

    def operacao(self):
        while(self.opcao != 0):
            self.menu()

            if self.opcao == 0:
                print("Obrigado!!!")

            elif self.opcao == 1:
                i = 0
                for i in range(20):
                    print("Informe a nota do {}º aluno".format(i+1))
                    num = int(input())
                    while (num < 0) or (num > 10):
                        print("Nota inválida!\nFavor digitar novamente: ")
                        num = int(input())
                self.model.mediaTurma()

            elif self.opcao == 2:
                i = 0
                for i in range(20):
                    print("Informe o {}º numero".format(i+1))
                    num = int(input())
                    while num < 0:
                        print("Numero negativo!\nFavor digitar um numero positivo: ")
                        num = int(input())
                    self.model.preencherVetor(num)

                self.model.vetorQ()

            elif self.opcao == 3:
                i = 0
                for i in range(20):
                    print("Digite o {}° numero".format(i+1))
                    self.model.preencherVetor(int(input()))
                print("Os numeros digitados na ordem inversa ficou: ")
                self.model.inverso()

            elif self.opcao == 4:
                i = 0
                for i in range(10):
                    print("Digite a temperatura do {}º dia: ".format(i+1))
                    self.model.preencherVetor(int(input()))
                self.model.mediaTemp()

            elif self.opcao == 5:
                i = 0
                for i in range(10):
                    print("Digite o {}º numero".format(i+1))
                    self.model.preencherVetor(int(input()))
                self.model.sortVetor()

            elif self.opcao == 6:
                i = 0
                for i in range(15):
                    print("Digite o {}º numero".format(i+1))
                    self.model.preencherVetor(int(input()))
                i = 0
                for i in range(15):
                    print("Digite o {}º numero para o segundo Vetor".format(i + 1))
                    self.model.preencherVetor2(int(input()))
                self.model.compareVetor()

            elif self.opcao == 7:
                i = 0
                for i in range(5):
                    print("Digite o {}º numero:".format(i+1))
                    self.model.preencherVetor(int(input()))
                self.model.verificarVetor()