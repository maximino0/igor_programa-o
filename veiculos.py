class veiculos:
    def __init__(self,marca,ano,preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco
    def exibir_info(self):
        return f"marca: {self.marca}, Ano: {self.ano}, Preço: {self.preco}R$"
class carro(veiculos):
    def __init__(self,marca,ano,preco,modelo,potencia):
        super().__init__(marca,ano,preco)
        self.modelo = modelo
        self.pot = potencia
    def exibir_info(self):
        return super().exibir_info() + f", Modelo: {self.modelo}, Potencia: {self.pot} cavalos"
class moto(veiculos):
    def __init__(self,marca,ano,preco,cilindrada):
        super().__init__(marca,ano,preco)
        self.cil = cilindrada
    def exibir_info(self):
        return super().exibir_info() + f", Cilindrada: {self.cil} cilindradas"