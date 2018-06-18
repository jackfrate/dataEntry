from selenium import webdriver


"""
class that takes in a dictionary of item objects and will put them into forms 
https://www.hongkiat.com/blog/automate-create-login-bot-python-selenium/
"""


class WebWriterTest:
    def __init__(self, inventory: {}):
        self.inventory = inventory
        self.destination = 'file:///C:/Users/Jack/Desktop/webtest/page.html'

    def write(self):
        # opens chrome and goes to the adress
        browser = webdriver.Chrome()
        browser.get(self.destination)

        # go to each box and type the code in
        ct = 0
        for key, value in self.inventory.items():
            for i in range(0, 4):

                item_id = 'type' + str(ct)

                fill_this_box = browser.find_element_by_id(item_id)

                if i == 0:
                    fill_this_box.send_keys(value.name)
                elif i == 1:
                    fill_this_box.send_keys(value.category)
                elif i == 2:
                    fill_this_box.send_keys(value.price)
                elif i == 3:
                    fill_this_box.send_keys(value.uom)
                    # notify that it has been entered
                    print(key, ' has been entered!')

                ct += 1
