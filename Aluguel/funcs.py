#! .\venv\scripts\python.exe

import numpy as np
import pandas as pd



def read_params_csv(filepath: str = '') -> dict:
    """
    Funcao simples que le o csv de parametros e devolve um dicionario
    """
    final_dict = {}
    if len(filepath) > 0:
        cols = ['ITEM', 'VALOR']

        df = pd.read_csv(filepath, header=None)
        
        df.columns = cols
        
        #final_dict = {col:[val for val in df[col]] for col in df.columns}
        final_dict  = {df['ITEM'].iloc[i]:df['VALOR'].iloc[i] for i in range(df.shape[0])}
        return final_dict

    else:

        return final_dict

def calcula_valor_final(alguel:float = 0, despesas:float = 0) -> dict:
    """
    Funcao que calcula o valor para cada pessoa (Dreger, Edu e Mateus)
    """

    NOMES = ['DREGER', 'EDU', 'MATEUS']
    VFS = [0, 0, 0] # dreger, edu, mateus
    PORCENTAGENS = [0.3, 0.3, 0.4]  # dreger, edu, mateus

    for porcent, ind in zip(PORCENTAGENS, range(len(VFS))):
        VFS[ind] = alguel*porcent
        VFS[ind] = VFS[ind] + despesas/len(VFS)
 
    final_dict = {name:round(val, 2) for name, val in zip(NOMES, VFS)}
    
    return final_dict

    


if __name__ == '__main__':
    #print(read_params_csv("Aluguel\params.csv"))

    print(calcula_valor_final(1900, 300))