import pandas as pd
import numpy as np
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options


import time


from script_modules import read_params



def compra_amazon():
    """
    Funcao que ira comprar determinado item na amazon 
    """
    lista_params = ['EMAIL', 'SENHA_AMZ', 'PROD_AMZ', 'PATH_DRIVER', 'CPF']
    email_amz, senha_amz, item_amz, path_chromedriver, cpf = read_params(lista_params)


    # criando o driver
    driver = webdriver.Chrome(path_chromedriver)          

    # entrando no site
    driver.get(item_amz) 


    driver.find_element(By.ID, 'buy-now-button').click()

    time.sleep(1)
    driver.find_element(By.ID, 'ap_email').send_keys(email_amz)
    driver.find_element(By.ID, 'continue').click()

    time.sleep(1)

    driver.find_element(By.ID, 'ap_password').send_keys(senha_amz)
    driver.find_element(By.ID, 'signInSubmit').click()


    time.sleep(30)


    




    # try: 
    #     driver.find_element(By.LINK_TEXT, 'Envie para este endereço').click()
    # except:
    #     driver.find_element(By.LINK_TEXT, 'Utilize este endereço').click()
                        
    # time.sleep(2)



    # driver.find_elements(By.NAME, 'ppw-widgetEvent:SetPaymentPlanSelectContinueEvent')[0].click()


    # time.sleep(3)
    # time.sleep(1)
    # orders = driver.find_elements(By.NAME, 'order0')


    # orders[0].click()
    # time.sleep(6)

    # driver.find_element(By.NAME, 'placeYourOrder1').click()

    # time.sleep(4)



    return


def busca_itens_amazon():

    lista_params = ['EMAIL', 'SENHA_AMZ', 'PROD_AMZ', 'PATH_DRIVER', 'CPF']
    email_amz, senha_amz, item_amz, path_chromedriver, cpf = read_params(lista_params)




    # criando o driver
    driver = webdriver.Chrome(path_chromedriver)          

    # entrando no site
    driver.get('https://www.amazon.com.br/') 

    driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('GTX 1660')
    driver.find_element(By.ID, 'nav-search-submit-button').click()

    driver.find_element(By.LINK_TEXT, 'GPU NV GTX1660 6GB GHOST GDDR5 192BITS NE51660018J9-1161L, GAINWARD / PALIT').click()
    time.sleep(3)


    x = driver.find_elements(By.CLASS_NAME, 'priceblock_ourprice')[-1].click()

    print(x.text.replace('R$', '').replace('.', '').replace(',','.'))


    time.sleep(3)



    return






if __name__ == '__main__':
    busca_itens_amazon()
