# diferenca_datas.py
from datetime import datetime

def calcular_diferenca(data1, data2, unidade):
    # Converter as datas para objetos datetime
    data1_obj = datetime.strptime(data1, '%Y-%m-%d')
    data2_obj = datetime.strptime(data2, '%Y-%m-%d')

    # Calcular a diferença entre as datas
    diferenca = data2_obj - data1_obj

    # Calcular a diferença na unidade desejada
    if unidade == 'dias':
        return diferenca.days
    elif unidade == 'meses':
        meses = (data2_obj.year - data1_obj.year) * 12 + data2_obj.month - data1_obj.month
        return meses
    elif unidade == 'anos':
        anos = data2_obj.year - data1_obj.year
        return anos
    elif unidade == 'horas':
        return diferenca.days * 24 + diferenca.seconds // 3600
    elif unidade == 'minutos':
        return diferenca.days * 24 * 60 + diferenca.seconds // 60

    return None
