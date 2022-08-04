# comandos a serem executados no pronpt de camonado para instalação de bibliotecas necessarias para
# execussao do script

# pip install --upgrade pip
# pip install selenium
# pip install pyautogui
# pip install pywinautogui

from ast import Try
from ssl import Options
from selenium import webdriver
from PIL import ImageGrab,Image
from pywinauto import keyboard,clipboard
import time
import os
import base64
import json
import pyautogui

class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        # self.mensagem = "TESTE DE ENVIO 1"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome( executable_path=r'C:\\Users\\cco.camboriu\\Documents\\WinPython\\tools\\chromedriver.exe', chrome_options=options)
        self.driver.get('https://web.whatsapp.com')
        
        self.listabomb = (['BOMB_1.png','BOMB_2.png','BOMB_3.png','BOMB_4.png']) # lista de endereços bombinhas
        self.listasfs = (['SFS_1.png','SFS_2.png']) # lista de endereços são francisco do sul
        self.listpenha = (['PENH_1.png', 'PENH_2.png', 'PENH_3.png', 'PENH_4.png']) # lista de endereços penha
        self.listcamboriu = (['CAMB_1.png', 'CAMB_2.png', 'CAMB_3.png']) # lista de endereços camboriú

    def EnviarMensagens(self):
        time.sleep(30)
        self.driver.maximize_window()
        # envio penha
        campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='CCO Penha']")
        campo_grupo.click()
        time.sleep(5)
        botao_add = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')
        botao_add.click()
        time.sleep(2)
        botao_img = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span')
        pyautogui.hotkey('alt', 'e')
        print('C:\\Users\\cco.camboriu\\Downloads')
        pyautogui.press('enter')
        pyautogui.hotkey('alt','n')
        for listp in self.listpenha:
            pyautogui.press('"')
            print(self.listpenha)
            pyautogui.press('"')
        pyautogui.press('enter')
        time.sleep(15)
        pyautogui.press('enter')

        # envio bombinhas

        campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='CCO Águas de Bombinhas']")
        campo_grupo.click()
        time.sleep(5)
        botao_add = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')
        botao_add.click()
        time.sleep(2)
        botao_img = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span')
        pyautogui.hotkey('alt', 'e')
        print('C:\\Users\\cco.camboriu\\Downloads')
        pyautogui.press('enter')
        pyautogui.hotkey('alt','n')
        for listp in self.listabomb:
            pyautogui.press('"')
            print(self.listabomb)
            pyautogui.press('"')
        pyautogui.press('enter')
        time.sleep(15)
        pyautogui.press('enter')  

        #envio camboriu

        campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='CCO Camboriú']")
        campo_grupo.click()
        time.sleep(5)
        botao_add = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')
        botao_add.click()
        time.sleep(2)
        botao_img = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span')
        pyautogui.hotkey('alt', 'e')
        print('C:\\Users\\cco.camboriu\\Downloads')
        pyautogui.press('enter')
        pyautogui.hotkey('alt','n')
        for listp in self.listcamboriu:
            pyautogui.press('"')
            print(self.listcamboriu)
            pyautogui.press('"')
        pyautogui.press('enter')
        time.sleep(15)
        pyautogui.press('enter')

        # envio sao francisco do sul

        campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='CCO SFS']")
        campo_grupo.click()
        time.sleep(5)
        botao_add = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')
        botao_add.click()
        time.sleep(2)
        botao_img = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span')
        pyautogui.hotkey('alt', 'e')
        print('C:\\Users\\cco.camboriu\\Downloads')
        pyautogui.press('enter')
        pyautogui.hotkey('alt','n')
        for listp in self.listasfs:
            pyautogui.press('"')
            print(self.listasfs)
            pyautogui.press('"')
        pyautogui.press('enter')
        time.sleep(15)
        pyautogui.press('enter')
        self.driver.minimize_window()

bot = WhatsappBot()
cont = 0
while cont < 24:
    bot.EnviarMensagens()
    time.sleep(3500)
    