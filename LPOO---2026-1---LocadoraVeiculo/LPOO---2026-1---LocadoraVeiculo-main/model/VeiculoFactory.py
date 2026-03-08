from veiculo import Veiculo, Carro, Motorhome

class VeiculoFactory:
    
    @staticmethod
    def criar_veiculo(self, tipo: str, placa: str, categoria):

        if tipo == "carro":
            return Carro(
                placa=placa,
                categoria=categoria
            )
        elif tipo == "motorhome":
            return Motorhome(
                placa=placa,
                categoria=categoria
            )
        else:
            raise ValueError("Tipo de veículo inválido")