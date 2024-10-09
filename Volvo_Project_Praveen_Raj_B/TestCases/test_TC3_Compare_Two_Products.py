#Author : Praveen Raj Balasubramanian

from Utilities.BaseClass import BaseClass
from selenium.webdriver.common.keys import Keys
from Utilities.Logger import Logger
from PageObjects.FlipkartPages import Common,HomePage,DisplaySearchPage,AddToCartPage,PlaceOrderPage
import time

class Test_Compare_Two_Products(BaseClass):

    logFileName  = 'TC3_Compare_Two_Products.log'
    logger = Logger.setupLogger(name=logFileName,
                                filePath=f"TestEvidences/{logFileName}",
                                fileMode="w")
    logger.info('Initializing Logger')
    wait_time = 5

    def test_compare_two_products(self, driver):
        try :
            self.logger.info('TC3 : STRATED : Compare Two Products')
            #Step0 : Get data from Config File
            url = self.configs.get("FLIPKART_URL").data
            productA = self.configs.get("PRODUCT_1").data
            productB = self.configs.get("PRODUCT_2").data
            self.logger.info("URL : " + url)
            self.logger.info("Product A : " + productA)
            self.logger.info("Product B : " + productB)

            #Step1 : Open Flipkart URL
            driver.get(url)
            currentURL = driver.current_url
            self.logger.info("Current URL is " + currentURL)

            #Step2 : Search and Add to Compare Product A
            homePage = HomePage (driver)
            self.EW_Visibility_Of_Element(driver, homePage.product_search_box, self.wait_time)
            homePage.Product_Search_Box().click()
            homePage.Product_Search_Box().send_keys(productA)
            homePage.Product_Search_Box().send_keys(Keys.ENTER)
            self.logger.info("Searched Product A : " + productA)
            displaySearchPage = DisplaySearchPage (driver)
            displaySearchPage.Add_To_Compare().click()
            self.logger.info("Product A added to compare")

            #Step3 : Search and Add to Compare Product B
            self.EW_Visibility_Of_Element(driver, displaySearchPage.product_search_box, self.wait_time)
            self.EW_Element_Clickabale(driver, displaySearchPage.product_search_box, self.wait_time)
            displaySearchPage.Product_Search_Box().click()
            # displaySearchPage.Product_Search_Box().clear()
            displaySearchPage.Product_Search_Box().send_keys(Keys.CONTROL + "a")
            displaySearchPage.Product_Search_Box().send_keys(Keys.DELETE)
            displaySearchPage.Product_Search_Box().send_keys(productB)
            displaySearchPage.Product_Search_Box().send_keys(Keys.ENTER)
            time.sleep(1)
            displaySearchPage.Add_To_Compare().click()
            self.logger.info("Product B added to compare")

            #Step4 : Click on Compare Button
            displaySearchPage.Compare_Button().click()
            self.logger.info("Clicked on Compare Button")
            self.EW_Visibility_Of_Element(driver, displaySearchPage.ratings_review, self.wait_time)
            displaySearchPage.Ratings_Reviews().click()

            self.logger.info('TC3 : PASSED : Compare Two Products')
    
        except Exception as e:
            self.logger.error(e)
            self.logger.error('TC3 : FAILED : Compare Two Products')
            raise e


        

        

        