#Author : Praveen Raj Balasubramanian

from Utilities.BaseClass import BaseClass
from selenium.webdriver.common.keys import Keys
from Utilities.Logger import Logger
from PageObjects.FlipkartPages import Common,HomePage,DisplaySearchPage,AddToCartPage,PlaceOrderPage

class Test_Search_And_Order_Mobile(BaseClass):

    logFileName  = 'TC1_Search_And_Order_Mobile.log'
    logger = Logger.setupLogger(name=logFileName,
                                filePath=f"TestEvidences/{logFileName}",
                                fileMode="w")
    logger.info('Initializing Logger')
    wait_time = 5

    def test_search_and_order_mobile(self, driver):
        try :
            self.logger.info('TC1 : STRATED : Search And Order Mobile')
            #Step0 : Get data from Config File
            url = self.configs.get("FLIPKART_URL").data
            mobileModel = self.configs.get("MOBILE_MODEL").data
            self.logger.info("URL : " + url)
            self.logger.info("Mobile Model : " + mobileModel)

            #Step1 : Open Flipkart URL
            driver.get(url)
            currentURL = driver.current_url
            self.logger.info("Current URL is " + currentURL)

            #Step2 : Search Mobile
            homePage = HomePage (driver)
            self.EW_Visibility_Of_Element(driver, homePage.product_search_box, self.wait_time)
            homePage.Product_Search_Box().click()
            homePage.Product_Search_Box().send_keys(mobileModel)
            homePage.Product_Search_Box().send_keys(Keys.ENTER)
            self.logger.info("Searched Mobile Model : " + mobileModel)

            #Step3 : Select Mobile
            displaySearchPage = DisplaySearchPage (driver)
            self.EW_Visibility_Of_Element(driver, displaySearchPage.select_product, self.wait_time)
            self.EW_Element_Clickabale(driver, displaySearchPage.select_product, self.wait_time)
            displaySearchPage.Select_Product().click()
            self.logger.info("Selected Mobile Model : " + mobileModel)

            common = Common(driver)
            common.Switch_To_New_Window()

            #Step4 : Add to cart
            addToCartPage = AddToCartPage (driver)
            self.EW_Visibility_Of_Element(driver, addToCartPage.add_to_cart, self.wait_time)
            addToCartPage.Add_To_Cart().click()
            self.logger.info("Added To Cart")

            #Step5 : Place Order
            placeOrderPage = PlaceOrderPage (driver)
            self.EW_Visibility_Of_Element(driver, placeOrderPage.place_order, 5)
            placeOrderPage.Place_Order().click()
            self.logger.info("Placed Order")

            self.logger.info('TC1 : PASSED : Search And Order Mobile')
            driver.quit()
    
        except Exception as e:
            self.logger.error(e)
            self.logger.error('TC1 : FAILED : Search And Order Mobile')
            raise e


        

        

        