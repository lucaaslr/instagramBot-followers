from secrets import pw
from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username

        self.driver.get("https://instagram.com")
        sleep(2)

        #Log In with instagram account
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        sleep(4)
        self.driver.find_element_by_xpath("//button[@type='submit']")\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(4)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]"\
            .format(self.username)).click()
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]")\
            .click()

bot = InstaBot('testingllr', pw)
#bot.get_unfollowers()