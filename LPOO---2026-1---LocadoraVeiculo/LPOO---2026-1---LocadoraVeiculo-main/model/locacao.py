from datetime import date, datetime
from .veiculo import Veiculo


class Locacao:
    def __init__(self, veiculo: Veiculo, data_inicio: date, data_fim: date):
        self.veiculo = veiculo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
    
    
    @property
    def veiculo(self):
        return self.__veiculo
    
    @veiculo.setter
    def veiculo(self, obj):
        if(obj is not None):
            self.__veiculo = obj
        else:
            raise Exception("Objeto Veículo obrigatório!!!")
        
    def calcular_valor_locacao(self) -> float:
        if self.data_inicio is None or self.data_fim is None:
            raise Exception("Data de início e fim da locação são obrigatórias!!!")
        
        dias_locacao = (self.data_fim - self.data_inicio).days

        if dias_locacao == 0:
            dias_locacao = 1

        valor_total = (dias_locacao * self.veiculo.taxa_diaria) + self.veiculo.seguro

        return valor_total
        

