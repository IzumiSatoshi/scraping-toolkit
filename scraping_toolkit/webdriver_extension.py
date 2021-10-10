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

    def keyword_search(self, keyword, input_el_xpath, submit_btn_xpath, timeout=30):
        """
        keywordを入力し、検索ボタンを押すところまでやります
        timeoutは各処理事？
        """

        # キーワード入力
        input_el = self.find_element(input_el_xpath, timeout=timeout)
        input_el.clear()
        input_el.send_keys(keyword)

        # 検索
        self.find_element(submit_btn_xpath, timeout=timeout).click()

    def find_text(self, xpath, timeout=30):
        """
        xpathはtextを囲んでいる要素を指す
        見つからなかったらNoneを返す
        """
        texts = self.find_texts(xpath, timeout=timeout)

        if texts is None:
            return None

        text = texts[0]
        return text

    def find_texts(self, xpath, timeout=30):
        """
        xpathはtextを囲んでいる要素を指す
        find_elementsを実行して、長さが0ならNoneを返す
        """
        els = self.find_elements(xpath, timeout=timeout)
        if els is None:
            return None
        texts = [el.text for el in els]
        return texts

    def find_href(self, xpath, timeout=30):
        """
        find_hrefsを実行して、最初の要素を返す
        """
        hrefs = self.find_hrefs(xpath, timeout=timeout)

        if hrefs is None:
            return None

        return hrefs[0]

    def find_hrefs(self, xpath, timeout=30):
        """
        href属性を見つける
        なければNone
        """
        els = self.find_elements(xpath, timeout=timeout)

        if els is None:
            return None

        hrefs = [el.get_attribute('href') for el in els]
        return hrefs

    def find_element(self, xpath, timeout=30):
        elements = self.find_elements(xpath, timeout=timeout)

        if elements is None:
            return None

        return elements[0]

    def find_elements(self, xpath, timeout=30):
        """
        タイムアウト付きのfind_elements_by_xpath
        見つからなかったらNoneを返す
        """
        elements = None

        # 終了時刻を定義
        end_time = time.time() + timeout
        while True:
            try:
                # エレメントを見つける
                elements = self._driver.find_elements_by_xpath(xpath)
                break
            except exceptions.StaleElementReferenceException:
                # エラーなら少し待つ
                time.sleep(0.5)
                print('err')

            # 終了時刻を過ぎていたら抜ける
            if time.time() > end_time:
                break

        # Noneだとlen()ができないので
        if elements is None:
            return None

        # 見つからなかったらNone
        if len(elements) == 0:
            return None

        return elements

    def execute_script(self, script, *args):
        self._driver.execute_script(script, *args)

    def wait_until_to_be_clickable(self, xpath, timeout=30):

        end_time = time.time() + timeout
        print('end = ', end_time)
        while True:
            try:
                els = self.find_elements(xpath, timeout=timeout)
                for el in els:
                    el.click()
                print('break')
                break
            except exceptions.StaleElementReferenceException:
                print('err')
                time.sleep(0.5)

            if time.time() > end_time:
                break

        print('now = ', time.time())
