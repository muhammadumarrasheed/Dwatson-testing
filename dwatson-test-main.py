from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import Time

class DWatson:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def accessDWatson(self):
        self.driver.get("https://dwatson.pk/")
        print("Successfully accesses the dwatson.pk site")
        print("\t---\nCurrently on https://dwatson.pk/")
        time.sleep(2)

    def searchProduct(self):
        search_input = self.driver.find_element(By.ID, "search")
        search_term = "honey"
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.ENTER)
        print("Successfully searching the item 'honey'")
        print("\t---\nCurrently on https://dwatson.pk/catalogsearch/result/?q=honey")
        time.sleep(3)

    def searchAndSortProduct(self):
        sort_by = Select(self.driver.find_element(By.ID, "sorter"))
        sort_by.select_by_value("price")
        time.sleep(6)
        print("Successfully searching the item 'honey'")
        print("\t---\nCurrently on https://dwatson.pk/catalogsearch/result/index/?q=honey&product_list_order=price\n")

    def relatedSearchTerm(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.search.results")))
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "honey grape tablet"))).click()
        print("Successfully searching the related item 'honey'")
        print("\t---\nCurrently on https://dwatson.pk/catalogsearch/result/?q=honey+grape+tablet\n")

    def didYouMean(self):
        related_search_section = self.driver.find_element(By.CSS_SELECTOR, "dl.block")
        first_related_search_term = related_search_section.find_element(By.TAG_NAME, "a")
        first_related_search_term.click()
        print("Successfully selected the medicine category'")
        print("-----")

    def testCategoryButton(self):
        category_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.filter-options-title")))
        category_button.click()

    def testSelectCategory(self):
        time.sleep(1)
        medicines_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/catalogsearch/result/index/?cat=3&q=vitamin') and .//text()='Medicines']")))
        medicines_link.click()
        print("Medicines category is selected successfully")
        print("-----")

    def viewProductDetailTest(self):
        first_product_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.product.photo.product-item-photo")))
        first_product_link.click()
        print("Successfully displayed the product details")
        print("-----")

    def inputQuantityTest(self):
        quantity_input = self.wait.until(EC.visibility_of_element_located((By.ID, "qty")))
        quantity_input.clear()
        quantity_input.send_keys("3")
        print("Successfully input the item quantity")
        print("-----")

    def addQuantityTest(self):
        add_button = self.wait.until(EC.element_to_be_clickable((By.ID, "addQty")))
        add_button.click()
        print("Plus 1 in the product quantity Successfully")
        print("-----")

    def minusQuantityTest(self):
        minus_button = self.wait.until(EC.element_to_be_clickable((By.ID, "minusQty")))
        minus_button.click()
        print("Minus 1 in the product quantity Successfully")
        print("-----")

    def addToCartButtonTest(self):
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.ID, "product-addtocart-button")))
        add_to_cart_button.click()
        print("Items are added to the cart successfully")
        print("-----")

    def viewCartButtonTest(self):
        cart_icon = self.driver.find_element(By.CSS_SELECTOR, "a.action.showcart")
        cart_icon.click()
        print("Cart icon is clicked and added items are displayed")
        print("-----")

    def proceedToCheckoutButtonTest(self):
        self.driver.execute_script("document.getElementById('top-cart-btn-checkout').click();")
        print("Proceed to checkout button is clicked")
        print("-----\n")

    def fillShippingDetailsTest(self):
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "customer-email")))
        email_input.send_keys("example@example.com")

        first_name_input = self.driver.find_element(By.NAME, "firstname")
        first_name_input.send_keys("John")

        last_name_input = self.driver.find_element(By.NAME, "lastname")
        last_name_input.send_keys("Doe")

        street_input = self.driver.find_element(By.NAME, "street[0]")
        street_input.send_keys("123 Main St")

        street_input2 = self.driver.find_element(By.NAME, "street[1]")
        street_input2.send_keys("123 Main St")

        time.sleep(2)
        dropdown_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, "region_id")))
        dropdown = Select(dropdown_element)
        dropdown.select_by_value("1109")
        time.sleep(1)

        dropdown_element_city = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "")))
        dropdown_city = Select(dropdown_element_city)
        dropdown_city.select_by_visible_text("GWADAR")
        time.sleep(1)

        telephone_input = self.driver.find_element(By.NAME, "telephone")
        telephone_input.send_keys("1234567890")
        print("Inputting all the shipping info")
        print("-----")

    def nextShipButtonTest(self):
        next_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-role='opc-continue']")))
        next_button.click()
        print("Next button is clicked")
        print("-----")
        time.sleep(5)

    def medicinesTagTest(self):
        medicines_link = self.driver.find_element(By.LINK_TEXT, "Medicines")
        medicines_link.click()
        print("Medicines Category is opened")
        print("-----")
        time.sleep(5)

    def deleteProductFromCart(self):
        view_edit_cart = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='View and Edit Cart']")))
        view_edit_cart.click()
        remove_item = self.driver.find_element(By.XPATH, "//span[normalize-space()='Remove item']")
        self.driver.execute_script("arguments[0].click();", remove_item)
        print("Added product from cart are successfully deleted")
        print("-----")
        time.sleep(5)

    def signInTest(self):
        sign_in_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In")))
        sign_in_link.click()
        print("Successfully accesses the login page")
        print("\t---\nCurrently on https://dwatson.pk/customer/account/login/referer/aHR0cHM6Ly9kd2F0c29uLnBrLw%2C%2C/")
        time.sleep(2)

    def fillSignInForm(self):
        email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        email_field.send_keys("hinod65727@nexxterp.com")  # Replace with the actual email address
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "pass")))
        password_field.send_keys("asbE@Z24pAPyycV")  # Replace with the actual password
        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.ID, "send2")))
        time.sleep(10)
        sign_in_button.click()
        print("All fields are filled correctly and SignedIn Successfully")
        print("\t---\nCurrently on https://dwatson.pk/customer/account/login/referer/aHR0cHM6Ly9kd2F0c29uLnBrLw%2C%2C/")
        time.sleep(2)

    def closeCart(self):
        close_button = self.wait.until(EC.element_to_be_clickable((By.ID, "btn-minicart-close")))
        close_button.click()
        print("Cart is successfully closed")

    def element(self):
        items = self.driver.find_elements(By.XPATH, "@href, '/catalogsearch/result/')")
        first_ele = items[0]
        first_ele.click()

# Example usage
dwatson = DWatson()
dwatson.accessDWatson()
dwatson.searchProduct()
dwatson.viewProductDetailTest()
dwatson.inputQuantityTest()
dwatson.addToCartButtonTest()
time.sleep(10)
# ... (call other methods as needed)
