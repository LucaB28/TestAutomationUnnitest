import time
import unittest
from FUNCIONES import Funciones_Ex
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import unittest
from FUNCIONES.Funciones import FuncionesGlobales

tg = 4

class base_test(unittest.TestCase):

    def setUp(self):
        chromedriver_path = "C:/Users/Luca/OneDrive/Escritorio/LUCA/chromedriver.exe"
        service = ChromeService(executable_path=chromedriver_path)
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        # self.driver.get("https://www.saucedemo.com/v1/")


    def test1(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        fe= Funciones_Ex(driver)
        f.Navegar("https://demoqa.com/text-box")
        ruta = "C:/Users/Luca/PycharmProjects/pythonProject7/excelparausar/testExcel.xlsx"
        filas = fe.getRowCount(ruta, "Hoja1")

#Inicia en dos por que la columna 1 es el titulo
        for r in range (2,filas+1):
            nombre = fe.readData (ruta, "Hoja1", r, 1)
            apellido = fe.readData (ruta, "Hoja1", r, 2)
            edad = fe.readData(ruta, "Hoja1", r, 3)

        f.Texto("id", "userName", nombre, tg)
        f.Texto("id", "userLastname", apellido, tg)
        f.Texto("id", "YearsOld", edad , tg)


