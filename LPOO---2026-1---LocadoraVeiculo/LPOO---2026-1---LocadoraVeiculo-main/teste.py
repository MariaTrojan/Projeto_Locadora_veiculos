from model.locacao import *
from model.veiculo import *
from model.VeiculoFactory import VeiculoFactory

carro = Carro(placa="ABC1#34", taxa_diaria=100)
locacao = Locacao(veiculo = carro, data_fim=None, data_inicio=None)

categoria = "A"

veiculo1 = VeiculoFactory.criar_veiculo("carro", "ABC1234", categoria)
veiculo2 = VeiculoFactory.criar_veiculo("motorhome", "XYZ9999", categoria)

print(veiculo1)
print(veiculo2)