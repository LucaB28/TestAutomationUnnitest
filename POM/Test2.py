from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import unittest
from FUNCIONES.Funciones import FuncionesGlobales
from FUNCIONES.Page_Login import Pagina_Login
from selenium.webdriver.support.ui import Select

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

# SE LLAMA AL DRIVER, LUEGO FUNCIONES GLOBALES, SE LLAMA FUNCION NAVEGAR PARA INTRODUCIR URL
# Y LUEGO A LA OTRA FUNCION PARA ELEGIR LA OPCION MEDIENTE SE QUIERE TRABAJAR EL SELECT CAMBIANDO EL TIPO Y EL DATO (*select no se trabaja con div)
#LA FUNCION QUE ESTA COMENTADA ES UN EJEMPLO PARA UTILIZAR CUANDO SOLO SE QUIERE TRABAJAR CON UN TIPO DE SELECT
    def testSelector(self):
        driver = self.driver
        f = FuncionesGlobales(driver)
        f.Navegar("https://demoqa.com/select-menu", tg)
       # f.Select_xpath_text("//*[@id='oldSelectMenu']","Black" , tg)
        f.Select_xpath_tipo("//*[@id='oldSelectMenu']", "text" , "Black" , tg)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()