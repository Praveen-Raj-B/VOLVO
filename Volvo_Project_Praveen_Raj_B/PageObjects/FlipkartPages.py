import pytest
from selenium.webdriver.common.by import By

class Common :

    def __init__(self, driver):
        self.driver = driver
    
    def Switch_To_New_Window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

class HomePage:
    
    def __init__(self, driver):
        self.driver = driver
    
    product_search_box = (By.XPATH,"//input[@placeholder='Search for Products, Brands and More']")
    fashion_dropdown = (By.XPATH,"//span[contains(text(),'Fashion')]")
    top_offers = (By.XPATH,"//span[contains(text(),'Top Offers')]")
    all_mens_topwear = (By.XPATH,"//a[normalize-space()='All']")
    

    def Product_Search_Box (self):
        return self.driver.find_element(*HomePage.product_search_box)
    
    def Fashion_Dropdown (self):
        return self.driver.find_element(*HomePage.fashion_dropdown)
    
    def All_Mens_Topwear (self):
        return self.driver.find_element(*HomePage.all_mens_topwear)

    def Top_Offers (self):
        return self.driver.find_element(*HomePage.top_offers)
    

class DisplaySearchPage:

    def __init__(self, driver):
        self.driver = driver
    
    select_product_v = "//div[normalize-space()='{}']".format(pytest.mobileModel)
    select_product = (By.XPATH,select_product_v)
    # select_product = (By.XPATH,"//div[normalize-space()='Apple iPhone 16 (White, 128 GB)']")
    high_customer_rating = (By.XPATH,"//div[@title='4★ & above']//div[@class='XqNaEv']")
    select_casual_shirt = (By.XPATH,"(//a[contains(text(),'Men Slim')])[1]")
    product_search_box = (By.XPATH,"//input[@placeholder='Search for products, brands and more']")
    add_to_compare = (By.XPATH,"(//span[contains(text(),'Add to Compare')])[1]")
    compare_button = (By.XPATH,"//span[contains(text(),'COMPARE')]")
    men_dropdown = (By.XPATH,"//span[normalize-space()='Men']")
    casual_shirts = (By.XPATH,"//a[normalize-space()='Casual Shirts']")
    ratings_review = (By.XPATH,"//span[normalize-space()='Ratings & Reviews']")
    
    
    def Select_Product (self):
        return self.driver.find_element(*DisplaySearchPage.select_product)
    
    def High_Customer_Rating (self):
        return self.driver.find_element(*DisplaySearchPage.high_customer_rating)
    
    def Select_Casual_Shirt (self):
        return self.driver.find_element(*DisplaySearchPage.select_casual_shirt)
    
    def Product_Search_Box (self):
        return self.driver.find_element(*DisplaySearchPage.product_search_box)

    def Add_To_Compare (self):
        return self.driver.find_element(*DisplaySearchPage.add_to_compare)
    
    def Compare_Button (self):
        return self.driver.find_element(*DisplaySearchPage.compare_button)
    
    def Men_Dropdown (self):
        return self.driver.find_element(*DisplaySearchPage.men_dropdown)
    
    def Casual_Shirts (self):
        return self.driver.find_element(*DisplaySearchPage.casual_shirts)

    def Ratings_Reviews (self):
        return self.driver.find_element(*DisplaySearchPage.ratings_review)


class AddToCartPage:
    
    def __init__(self, driver):
        self.driver = driver
    
    add_to_cart = (By.XPATH,"//button[normalize-space()='Add to cart']")
    
    def Add_To_Cart (self):
        return self.driver.find_element(*AddToCartPage.add_to_cart)

class PlaceOrderPage:
    
    def __init__(self, driver):
        self.driver = driver
    
    place_order = (By.XPATH,"//span[normalize-space()='Place Order']")
    
    def Place_Order (self):
        return self.driver.find_element(*PlaceOrderPage.place_order)


