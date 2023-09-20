from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time
import unittest
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class FuncionesGlobales():

    def __init__(self,driver):
        self.driver = driver

    #Funcion para pasar el tiempo
    def Tiempo(self,segundos):
       time.sleep(segundos)

    #Funcion para pasar la url y el tiempo se obtiene de la funcion anterior
    def Navegar(self,url,Tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Pagina abierta " + str (url))
        time.sleep(Tiempo)

    #Funcion para obtener texto utilizando ID

    def Texto(self,ID,texto,Tiempo):
            valor = self.driver.find_element(By.ID, ID)
            valor.send_keys(texto)
            valor.clear()
            valor.send_keys(texto)
            print("escribiendo en campo {} el texto {}".format(ID, texto))
            time.sleep(Tiempo)

    # Funcion para obtener texto utilizando XPATH

    def Texto_xpath(self,xpath,texto,Tiempo):
        try:
            valorxpath = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            valorxpath = self.driver.execute_script("arguments[0].scrollIntoView();", valorxpath)
            valorxpath = self.driver.find_element(By.XPATH, xpath)
            valorxpath.clear()
            valorxpath.send_keys(texto)
            print("escribiendo en campo {} el texto {}".format(xpath,texto))
            time.sleep(Tiempo)
        except TimeoutException as ex:
            print(ex)
            print("No se encontro el elemento" + xpath)

    #HACER CLICK POR XPTAH

    def click_xpath(self,xpath,Tiempo):
        try:
            click_xpath = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            click_xpath = self.driver.execute_script("arguments[0].scrollIntoView();", click_xpath)
            click_xpath = self.driver.find_element(By.XPATH, xpath)
            click_xpath.click()
            print("Click en campo {}".format(xpath))
            time.sleep(Tiempo)
        except TimeoutException as ex:
            print(ex)
            print("No se encontro el elemento" + xpath)

    # HACER CLICK POR ID

    def click_id(self,ID,Tiempo):
        try:
            click_id = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
            click_id = self.driver.execute_script("arguments[0].scrollIntoView();", click_id)
            click_id = self.driver.find_element(By.ID, ID)
            click_id.click()
            print("Click en campo {}".format(ID))
            time.sleep(Tiempo)
        except TimeoutException as ex:
            print(ex)
            print("No se encontro el elemento" + ID )

    def Salida(self):
        print("se termina la prueba")


    def Select_xpath_text(self,xpath,text,Tiempo):
        try:
            select_xpath = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            select_xpath = self.driver.execute_script("arguments[0].scrollIntoView();", select_xpath)
            select_xpath = self.driver.find_element(By.XPATH, xpath)
            select_xpath = Select(select_xpath)
            select_xpath.select_by_visible_text(text)
            print("el campo seleccionado es {}".format(text))
            time.sleep(Tiempo)
        except TimeoutException as ex:
            print(ex)
            print("No se encontro el elemento" + xpath)



#PARA TRABAJAR CON SELECT HAY 3 MANERAS, POR ESO DE DESCRIBEN LAS TRES POSIBLES
    def Select_xpath_tipo(self,xpath,tipo, dato,Tiempo):
        try:
            select_xpath = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            select_xpath = self.driver.execute_script("arguments[0].scrollIntoView();", select_xpath)
            select_xpath = self.driver.find_element(By.XPATH, xpath)
            select_xpath = Select(select_xpath)
            if (tipo == "text"):
                select_xpath.select_by_visible_text(dato)
            elif (tipo == "index"):
                select_xpath.select_by_index(dato)
            elif (tipo == "value"):
                select_xpath.select_by_value(dato)
            print("el campo seleccionado es {}".format(dato))
            time.sleep(Tiempo)
        except TimeoutException as ex:
            print(ex)
            print("No se encontro el elemento" + xpath)