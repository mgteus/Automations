from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

import os
import time


def posta_anuncio(path):



    email = ''
    senha = ''
    path_driver_chrome = r"C:\Program Files (x86)\chromedriver.exe"

    driver = webdriver.Chrome(path_driver_chrome)



    driver.get("https://conta.olx.com.br/acesso?returnToToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJodHRwczovL2NvbnRhLm9seC5jb20uYnIvYW51bmNpb3MiLCJpYXQiOjE2MzM5ODA1NDI4MzF9.VtwDef9Rcl39H_IJrNzALvQIxdlOZVKSwJVLzuWKmYM") 
    time.sleep(3)


    input1 = driver.find_elements(By.TAG_NAME, "input")[0]
    input2 = driver.find_elements(By.TAG_NAME, "input")[1]

    input1.send_keys(email)

    input2.send_keys(senha)

    time.sleep(1)

    driver.find_elements(By.TAG_NAME, "button")[1].click()

    
    


    time.sleep(5)





    return 


if __name__ == '__main__':
    posta_anuncio()
