from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from FUNCIONES.Funciones import FuncionesGlobales

# SE GENERA CLASE, PARA GENERAR FUNCIONES QUE ÚNICAMENTE SE UTILIZAN EN EL LOGIN

class Pagina_Login():

    def __init__(self, driver):
        self.driver = driver


# DENTRO DE LA FUNCION SE PIDEN DETERMINADOS DATOS QUE LUEGO SON INGRESADOS EN EL MISMO TEST CUANDO SE LLAMA LA FUNCION
    def Login_1(self, url, name, password, t):
        driver = self.driver
        f = FuncionesGlobales(driver)
        f.Navegar(url, t)
        f.Texto_xpath("//*[@id='user-name']", name, t)
        f.Texto_xpath("//*[@id='password']", password, t)
        f.click_xpath("//*[@id='login-button']", t)
        f.Salida()