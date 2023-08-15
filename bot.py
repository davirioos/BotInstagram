from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random

def seguipessoas(login, senha, contaSeguir):
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    sleep(1)

    # Digita Nome de Usuario
    nome_usuario = driver.find_element(By.NAME, "username")
    nome_usuario.send_keys(login)
    print("Encontrei")
    sleep(1)

    # Digita a Senha do Usuario
    senha_usuario = driver.find_element(By.NAME, "password")
    senha_usuario.send_keys(senha)
    print("encontrei")
    sleep(1)

    # Clica no Botão para acessar
    login_box = driver.find_element(By.CLASS_NAME, '_acas')
    login_box.click()
    sleep(10)

    # Clica no Icon Pesquisar
    pesquisar = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a')
    pesquisar.click()
    sleep(10)

    # Clica no Campo de Pesquisar
    pesquisar1 = driver.find_element(By.CLASS_NAME, 'x1lugfcp')
    pesquisar1.click()
    pesquisar1.send_keys(contaSeguir)
    sleep(5)

    #Entra na Conta desejada
    pesquisar2 = driver.find_element(By.CSS_SELECTOR, 'a.x1yutycm')
    pesquisar2.click()
    sleep(5)

    #Clica nos seguidores
    contaSeguidores = driver.find_element(By.CSS_SELECTOR, 'a._alvs')
    contaSeguidores.click()
    sleep(5)

    #Seguindo
    contador = 1
    while contador < 100:

        tempo_de_seguir = random.randrange(256, 353)
        seguindo = driver.find_element(By.CSS_SELECTOR, 'button._acas')
        seguindo.click()
        print(f'Ja Seguir {contador} pessoas ')
        print(f'Só irei seguir a proxima pessoa: {tempo_de_seguir} segundos')
        contador += 1
        sleep(tempo_de_seguir)

def deixaDeSeguir(login, senha):

    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    sleep(1)

    # Digita Nome de Usuario
    nome_usuario = driver.find_element(By.NAME, "username")
    nome_usuario.send_keys(login)
    print("Encontrei")
    sleep(1)

    # Digita a Senha do Usuario
    senha_usuario = driver.find_element(By.NAME, "password")
    senha_usuario.send_keys(senha)
    print("encontrei")
    sleep(1)

    # Clica no Botão para acessar
    login_box = driver.find_element(By.CLASS_NAME, '_acas')
    login_box.click()
    sleep(10)
    #Entrando no meu Perfil
    perfil = driver.find_element(By.CSS_SELECTOR, 'img.xpdipgo')
    perfil.click()
    sleep(7)

    #driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
    seguindo = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
    seguindo.click()
    sleep(7)

    contador = 1
    while contador < 100:

        tempoDeDeixar = random.randrange(180, 239)
        deixando = driver.find_element(By.CSS_SELECTOR, 'button._acat')
        deixando.click()
        sleep(2)
        deixando = driver.find_element(By.CSS_SELECTOR, 'button._a9-_')
        deixando.click()
        print(f'Ja Deixei de Seguir {contador} pessoas ')
        print(f'Só irei Deixar de Seguir a proxima pessoa: {tempoDeDeixar} segundos')
        contador += 1
        sleep(tempoDeDeixar)


escolhaUsuario = input('Escolhar um numero (1) Seguir (2) Deixa de Seguir')

if escolhaUsuario == '1':

    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    contaSeguir = input('Digite a Conta que deseja os seguidores: ')
    print('OBS: você tem que esta seguindo a conta que deseja os seguidores.')
    seguipessoas(login, senha, contaSeguir)

elif escolhaUsuario == '2':
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    deixaDeSeguir(login, senha)

else:
    print('Escolha (1) ou (2)')


