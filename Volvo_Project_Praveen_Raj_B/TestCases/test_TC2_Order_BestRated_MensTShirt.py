#Author : Praveen Raj Balasubramanian

from Utilities.BaseClass import BaseClass
from selenium.webdriver.common.keys import Keys
from Utilities.Logger import Logger
from PageObjects.FlipkartPages import Common,HomePage,DisplaySearchPage,AddToCartPage,PlaceOrderPage
import time

class Test_Order_BestRated_MensTShirt(BaseClass):

    logFileName  = 'TC2_Order_BestRated_MensTShirt.log'
    logger = Logger.setupLogger(name=logFileName,
                                filePath=f"TestEvidences/{logFileName}",
                                fileMode="w")
    logger.info('Initializing Logger')
    wait_time = 5

    def test_order_bestrated_menstshirt(self, driver):
        try :
            self.logger.info('TC2 : STRATED : Order Best Rated Mens T-Shirt')
            #Step0 : Get data from Config File
            url = self.configs.get("FLIPKART_URL").data
            self.logger.info("URL : " + url)

            #Step1 : Open Flipkart URL
            driver.get(url)
            currentURL = driver.current_url
            self.logger.info("Current URL is " + currentURL)

            #Step2 : Select Top Offers
            homePage = HomePage (driver)
            self.EW_Visibility_Of_Element(driver, homePage.product_search_box, self.wait_time)
            # homePage.Fashion_Dropdown().click()
            homePage.Top_Offers().click()
            # homePage.All_Mens_Topwear().click()
            self.logger.info("Selected Top Offers")

            #Step3 : Select Casual Shirt
            displaySearchPage = DisplaySearchPage (driver)
            self.EW_Visibility_Of_Element(driver, displaySearchPage.men_dropdown, self.wait_time)
            self.EW_Element_Clickabale(driver, displaySearchPage.men_dropdown, self.wait_time)
            displaySearchPage.Men_Dropdown().click()
            self.EW_Visibility_Of_Element(driver, displaySearchPage.casual_shirts, self.wait_time)
            displaySearchPage.Casual_Shirts().click()
            self.EW_Visibility_Of_Element(driver, displaySearchPage.high_customer_rating, self.wait_time)
            self.EW_Element_Clickabale(driver, displaySearchPage.high_customer_rating, self.wait_time)
            displaySearchPage.High_Customer_Rating().click()
            time.sleep(1)
            self.EW_Visibility_Of_Element(driver, displaySearchPage.select_casual_shirt, self.wait_time)
            self.EW_Element_Clickabale(driver, displaySearchPage.select_casual_shirt, self.wait_time)
            displaySearchPage.Select_Casual_Shirt().click()
            self.logger.info("Selected Casual Shirt")

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

            self.logger.info('TC2 : PASSED : Order Best Rated Mens T-Shirt')
    
        except Exception as e:
            self.logger.error(e)
            self.logger.error('TC2 : FAILED : Order Best Rated Mens T-Shirt')
            raise e


        

        

        