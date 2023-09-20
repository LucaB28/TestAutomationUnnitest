from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import unittest
from FUNCIONES.Funciones import FuncionesGlobales
from FUNCIONES.Page_Login import Pagina_Login

tg = 4
#AL UTILIZAR UNNITEST SIEMPRE SE COMIENZA CON LA CLASE (UNITTEST.TESTCASE)
#LUEGO LA FUNCION SETUP , LUEGO LOS TEST Y LUEGO TEARDOWN Y PARA CERRAR LA CLASE EL MAIN
class BaseTest_Login(unittest.TestCase):

    def setUp(self):
        chromedriver_path = "C:/Users/Luca/OneDrive/Escritorio/LUCA/chromedriver.exe"
        service = ChromeService(executable_path=chromedriver_path)
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        #self.driver.get("https://www.saucedemo.com/v1/")

# SE LLAMA AL DRIVER, LUEGO FUNCIONES GLOBALES QUE CONTIENEN LAS FUNCIONES DEL LOGIN, SE LLAMA A LAS FUNCIONES DEL LOGIN Y LUEGO A LA FUNCION DEL LOGIN QUE CONTIENE EL SCRIPT CON LOS DATOS SOLICITADOS

    def test_login1(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        pg = Pagina_Login(driver)
        pg.Login_1("https://www.saucedemo.com/v1/","Luca", "Luca321" , tg )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
