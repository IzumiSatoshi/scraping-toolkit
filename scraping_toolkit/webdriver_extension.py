import time
from selenium import webdriver
import selenium
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions


class WebdriverExtension():
    def __init__(self, headless_mode=False):
        options = Options()
        if headless_mode:
            options.add_argument('--headless')
        self._driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)

    def get(self, url):
        self._driver.get(url)

    def keyword_search(self, keyword, input_el_xpath, submit_btn_xpath):
        """
        keywordを入力し、検索ボタンを押すところまでやります
        timeoutは各処理事？
        """

        # キーワード入力
        input_el = self.find_element(input_el_xpath)
        input_el.clear()
        input_el.send_keys(keyword)

        # 検索
        self.find_element(submit_btn_xpath).click()

    def find_text(self, xpath):
        """
        xpathはtextを囲んでいる要素を指す
        見つからなかったらNoneを返す
        """
        texts = self.find_texts(xpath)

        if texts is None:
            return None

        text = texts[0]
        return text

    def find_texts(self, xpath):
        """
        xpathはtextを囲んでいる要素を指す
        find_elementsを実行して、長さが0ならNoneを返す
        """
        els = self.find_elements(xpath)
        if els is None:
            return None
        texts = [el.text for el in els]
        return texts

    def find_href(self, xpath):
        """
        find_hrefsを実行して、最初の要素を返す
        """
        hrefs = self.find_hrefs(xpath)

        if hrefs is None:
            return None

        return hrefs[0]

    def find_hrefs(self, xpath):
        """
        href属性を見つける
        なければNone
        """
        els = self.find_elements(xpath)

        if els is None:
            return None

        hrefs = [el.get_attribute('href') for el in els]
        return hrefs

    def find_element(self, xpath):
        """
        最初に見つかった要素を返す
        """
        elements = self.find_elements(xpath)

        if elements is None:
            return None

        return elements[0]

    def find_elements(self, xpath):
        """
        見つからなかったらNoneを返す
        """
        elements = self._driver.find_elements_by_xpath(xpath)

        if len(elements) == 0:
            return None

        return elements

    def execute_script(self, script, *args):
        self._driver.execute_script(script, *args)

    def quit(self):
        self._driver.quit()
