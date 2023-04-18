# Autor: Gerson Pereira
# Vamos criar um exemplo de classe Carro
class Carro:
    carros_instanciados = 0


    def __init__(self, marca, modelo, ano, cor, preco, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.preco = preco
        self.velocidade = 0
        self.placa = placa          
        self.combustivel = 0        

        Carro.carros_instanciados += 1


    @classmethod
    def total_instacias(cls):
        return cls.carros_instanciados


    def ligar(self):
        print("O carro está ligado!")


    def abastecer(self, valor):
        if self.combustivel < 100:
            abastecido = self.combustivel + valor

            if abastecido <= 100:
                self.combustivel += valor
                print(f"Foi abastecido {valor}L, agora o carro possui {self.combustivel}L de combustivel!")

            else:
                print(f"O carro não comporta essa quantidade de combustivel. Espaço disponivél: {100 - self.combustivel}L")

        else:
            print("O reservatório está cheio!")


    def consumir_combustivel(self, consumo):
        if self.combustivel > 0:
            self.combustivel -= consumo

        else:
            print(f"O carro possui pouco combustivél {self.combustivel}L, favor abastecer!")


    def acelerar(self, valor):
        self.velocidade += valor


    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
            print("O carro parou!")


    def mostrar_velocidade(self):
        print(f"A velocidade atual é de {self.velocidade} km/h.")


    @staticmethod
    def calcular_media(carros):
        if not carros:
            return 0

        total = sum(carro.preco for carro in carros)
        return total / len(carros)



class Moto:
    def __init__(self, marca, modelo, ano, cor, preco, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.preco = preco
        self.velocidade = 0
        self.placa = placa 
        self.combustivel = 0


    def ligar(self):
        print("A moto está ligado!")


    def abastecer(self, valor):
        if self.combustivel < 100:
            abastecido = self.combustivel + valor


            if abastecido <= 100:
                self.combustivel += valor
                print(f"Foi abastecido {valor}L, agora a moto possui {self.combustivel}L de combustivel!")


            else:
                print(f"A moto não comporta essa quantidade de combustivel. Espaço disponivél: {100 - self.combustivel}L")


        else:
            print("O reservatório está cheio!")


    def consumir_combustivel(self, consumo):
        if self.combustivel > 0:
            self.combustivel -= consumo


        else:
            print(f"A moto possui pouco combustivél {self.combustivel}L, favor abastecer!")


    def acelerar(self, valor):
        self.velocidade += valor


    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
            print("a moto parou!")


    def empinar(self):
        print("A moto está empinando!")


    def mostrar_velocidade(self):
        print(f"A velocidade atual é de {self.velocidade} km/h.")




carro1 = Carro("Chevrolet", "Camaro", 2021, "Amarelo", 280000, "ABC-1234")
carro2 = Carro("Chevrolet", "Camaro", 1968, "Amarelo", 510000, "ABE-1234")


carros = [Carro("Chevrolet", "Camaro", 2021, "Amarelo", 280000, "ABC-1234"),
          Carro("Chevrolet", "Camaro", 2021, "Amarelo", 230000, "ABD-1234"),
          Carro("Chevrolet", "Camaro", 1968, "Amarelo", 510000, "ABE-1234"),
          Carro("Chevrolet", "Camaro", 2021, "Amarelo", 320650, "ABF-1234"),
          Carro("Chevrolet", "Camaro", 2018, "Amarelo", 196054, "ABG-1234")]


print("Carro 1:")
print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"Ano: {carro1.ano}")
print(f"Cor: {carro1.cor}")
print(f"Preço: R$ {carro1.preco:,.2f}")
print(f"Placa: {carro1.placa}")


carro1.ligar()
carro1.abastecer(90)
carro1.acelerar(80)
carro1.consumir_combustivel(80)
carro1.frear(100)
carro1.mostrar_velocidade()


media = Carro.calcular_media(carros)
print(f"A media de preco da lista de carros R$ {media:,.2f}")


print(f"Total de instancias criando à partir do objeto Carro {Carro.total_instacias()}")


moto1 = Moto("Honda", "PCX", 2021, "Cinza", 280000, "DEF-5678")


print("Moto 1:")
print(f"Marca: {moto1.marca}")
print(f"Modelo: {moto1.modelo}")
print(f"Ano: {moto1.ano}")
print(f"Cor: {moto1.cor}")
print(f"Preço: R$ {moto1.preco:,.2f}")
print(f"Placa: {moto1.placa}")


moto1.ligar()
moto1.abastecer(90)
moto1.acelerar(80)
moto1.empinar()
moto1.consumir_combustivel(80)
moto1.frear(100)
moto1.mostrar_velocidade()
