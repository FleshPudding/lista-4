class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = (str (marca))
        self.modelo = (str(modelo))
        self.ano = (int(ano))
    def acelerar():
        print('Acelerando o veículo!')
    def frear():
        print('Freando o veículo!')

class carro(veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__(marca, modelo, ano)
        self.cor = (str(cor))
    def ligar_radio():
        print('Ligando o rádio do carro!')
    def abrir_porta():
        print('Abrindo a porta do carro!')

class moto(veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = (str(cilindrada))
    def empinar():
        print('Empinando a moto!')
    def buzinar():
        print('Buzinando a moto!')

class caminhao(veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima):
        super().__init__(marca, modelo, ano)
        self.carga_maxima = (str(carga_maxima))
    def carregar():
        print('Carregando o caminhão!')
    def descarregar():
        print('Descarregando o caminhão!')