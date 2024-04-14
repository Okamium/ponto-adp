from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Chrome()

navegador.get("https://expert.brasil.adp.com/")

time.sleep(2)

usuario = navegador.find_element(By.XPATH, '//*[@id="login"]')
senha = navegador.find_element(By.XPATH, '//*[@id="login-pw"]')
botao_login = navegador.find_element(By.XPATH, '/html/body/div/div/section[1]/div/form/div[3]/div/button')

time.sleep(2)

#Seu usuário ADP
usuario.send_keys("")

time.sleep(2)

#Sua senha ADP
senha.send_keys("")

time.sleep(2)

botao_login.click()

botao_ponto = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/section/header[2]/div/div/div[2]/div[2]/div/div[2]/button')

time.sleep(2)

botao_ponto.click()

time.sleep(8)
