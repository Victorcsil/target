def calc_percentual(fat_dict):
    total = sum(fat_dict.values())
    for estado in fat_dict:
        print(f'Percentual de representação de: {estado} {fat_dict[estado] / total * 100:.2f}%')


fat_dict = { 'SP': 67836.43, 
            'RJ': 36678.66, 
            'MG': 29229.88, 
            'ES': 27165.48, 
            'Outros': 19849.53
             }

calc_percentual(fat_dict)