from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import configs

class BaseClass: 

    configs = configs

    def EW_Visibility_Of_Element(self,driver,locator,waitTime):
            WebDriverWait(driver,waitTime).until(EC.visibility_of_element_located(locator))
    
    def EW_InVisibility_Of_Element(self,driver,locator,waitTime):
        WebDriverWait(driver,waitTime).until(EC.invisibility_of_element_located(locator))
    
    def EW_Element_Clickabale(self,driver,locator,waitTime):
        WebDriverWait(driver,waitTime).until(EC.element_to_be_clickable(locator))
    
    def EW_Element_Staleness(self,driver,locator,waitTime,):
        WebDriverWait(driver,waitTime).until(EC.staleness_of(locator))

