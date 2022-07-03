import os


import streamlit as st
import pandas as pd

from funcs import read_params_csv, calcula_valor_final



def main():
    

    st.set_page_config(page_title='Aluguel', page_icon="✔")

    menu = ['Página Inicial']

    tab = st.sidebar.selectbox('Menu', menu)

    if tab == 'Página Inicial':
        st.title('Calculadora do Aluguel:')


        valor_boleto = st.text_input('Digite o valor total do boleto:')

        if len(valor_boleto) > 0:
            # limpando o valor digitado
            valor_boleto = float(valor_boleto.replace(",", '.'))

            valor_luz = st.text_input('Digite o valor da luz:')
            if len(valor_luz) > 0:
                valor_luz = float(valor_luz.replace(",", '.'))
                valor_boleto = valor_boleto + valor_luz

            troca_params = st.checkbox('Trocar o arquivo de parâmetros?')
            
            if troca_params:
                st.error('NAO FUNCIONA AINDA')
                parms_dict = {}

            else:
                parms_dict = read_params_csv("params.csv")


            st.header('Despesas encontradas:')
            for item, val in parms_dict.items():
                #for val
                #val = float(val.replace(",", '.'))
                st.write(f"{item} -> R$ {val}")

            
            valor_total = valor_boleto - parms_dict['ALUGUEL'] 

            valor_aluguel = parms_dict['ALUGUEL']

            del parms_dict['ALUGUEL']

            st.subheader(f'Valor Total (- Aluguel)')
            st.write(round(valor_total,2))
            for item, val in parms_dict.items():
                valor_total = valor_total + val

            st.subheader('Valor Total (- Alguel + Despesas):')
            st.write(round(valor_total,2))



            st.success('Calculando Valor Final...')

            dict_com_vals = calcula_valor_final(valor_aluguel, valor_total)



            st.header('Resultado Final:')

            soma_total = 0
            for nome, vf in dict_com_vals.items():
                soma_total = soma_total + vf
                st.subheader(f"{nome} R$ {vf}")

            st.warning(f"Soma Total = R$ {round(soma_total,2)}")
            st.write(dict_com_vals)

    return




if __name__ == '__main__':
    main()