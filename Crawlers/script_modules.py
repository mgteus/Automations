import os
import pandas as pd
import csv


def read_params(tags: list=[], df: bool=True) -> dict or pd.DataFrame:
    """
    Função que lê o arquivo de parametros do projeto "Params.csv" e devolve:
    df = True -> pd.DataFrame
    df = False -> dict

    Pode devolver apenas tags específicas caso len(tags)!=0
    """

    path_csv = r"params.csv"

    dict_params = {}
    with open(path_csv, 'r', encoding='UTF-8') as csv_parms:
        csv_text = csv.reader(csv_parms, delimiter=',')

        for row in csv_text:      
            if len(row) > 0:
                dict_params[row[0]] = row[1]
                

    if len(tags) == 0:
        if df:
            return pd.DataFrame(dict_params.values(), index=dict_params.keys())
        else:
            return dict_params
    
    return [dict_params[item] for item in tags]
