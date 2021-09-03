
class Atleta:
    def __init__(self):
        self.__altura = float(input("Insira sua altura: "))
        self.__peso = int(input("Insira seu peso: "))
        self.__idade = int(input("Insira sua idade: "))
        self.__imc = self.calcular_imc()
        print(self.__imc)
        if(self.verificar_imc() == 1):
            self.perguntas()
    
    def calcular_imc(self):
        imc = self.__peso / self.__altura**2
        if(imc <= 18.5):
            return 'Baixo peso.'
        elif(imc > 18.5 and imc <= 24.9):
            return 'Peso ideal.'
        elif(imc > 25 and imc <= 29.9):
            return 'Sobrepeso.'
        elif(imc > 30 and imc <= 34.9):
            return '!° Obesidade.'
        elif(imc > 35 and imc <= 40):
            return '2° Obesidade.'
        elif(imc > 40):
            return 'Obesidade Grave.'

    def verificar_imc(self):
        if(self.__imc == 'Baixo peso.'):
            return 1
        if(self.__imc == 'Peso ideal.'):
            return 1
        else:
            print("Normalize sua forma física.")

    def perguntas(self):
        self.__vezes_treino = int(input("Quantas vezes você treina por semana? "))
        self.__minutos = int(input("Quantos minutos tem seus treinos? "))
        if self.__vezes_treino * self.__minutos >= 300:
            print("Parabéns, você passou em todos os nossos testes, agora você fará um teste pessoal em nossa sede, favor comparecer ao endereço: Rua dos Atletas, 43, Bairro do Futebol. Nos vemos lá!")
        else:
            print("Muito obrigado, agradecemos a sua participação!")

atleta = Atleta()