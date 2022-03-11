from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



class Translator:
    def __init__(self):

        self.options = Options()

        self.options.add_argument('headless')
        self.serv = Service("C:\Program Files (x86)\chromedriver.exe")
        self.driver = webdriver.Chrome(options=self.options, service=self.serv)

    def get_translation(self, trans_lang, translated_lang, text_to_translate):
        self.driver.get(f"https://translate.google.ca/?sl={trans_lang}&tl={translated_lang}&text={text_to_translate}&op=translate")
        self.driver.implicitly_wait(0.5)
        data = self.driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]/span/span')

        return data.text

