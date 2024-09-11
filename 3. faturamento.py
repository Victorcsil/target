import json

def faturamento():
    with open('faturamentos.json', 'r') as file:
        data = json.load(file)
    
    faturamentos = [item['faturamento'] for item in data['dias'] if item['faturamento'] != 0]
    
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)

    dias_acima_da_media = sum(1 for f in faturamentos if f > media_faturamento)

    print(f'Menor faturamento: R$ {menor_faturamento:.2f}\n'
          f'Maior faturamento: R$ {maior_faturamento:.2f}\n'
          f'Média faturamento: R$ {media_faturamento:.2f}\n'
          f'Dias acima da média: {dias_acima_da_media}')

faturamento()