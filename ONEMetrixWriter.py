from selenium import webdriver


"""
writer for one pos metrix site. 

"""


class ONEMetrixWriter:
    def __init__(self, inventory:{}):
        self.inventory = inventory
        self.destination = ''

    def write(self):
        # open chrome and enter the adress
        driver = webdriver.Chrome()
        driver.get(self.destination)

        # sign in
        self.sign_in(driver)

    def sign_in(self, driver):
        # find every element that needs information to sign in
        id_num_box = driver.find_element_by_class_name('z-intbox')
        username_box = driver.find_element_by_id('u4DPyd')
        password_box = driver.find_element_by_id('u4DP_e')
        click_me = driver.find_element_by_id('u4DP1e')

        # enter the information
        id_num_box.send_keys('11666')
        username_box.send_keys('Jack Frate')
        password_box.send_keys('pubfrato2018')

        # click login
        click_me.click()
