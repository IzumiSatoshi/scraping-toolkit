from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebdriverExtensions(webdriver.Chrome):
    """
    Chrome以外には対応していない
    find系メソッドは共通化したほうが良い？
    特に記述がない場合は、xpathで指定
    xpathに絞ってるのに、find_elements_by_xpathをしなきゃいけないのがもやもやする
    """

    def __init__(self, headless_mode=False):
        options = Options()
        if headless_mode:
            options.add_argument('--headless')
        super().__init__(ChromeDriverManager().install(), options=options)

    def keyword_search(self, keyword, input_el_xpath, submit_btn_xpath):
        """
        keywordを入力し、検索ボタンを押すところまでやります
        """

        # キーワード入力
        input_el = self.find_element_by_xpath(input_el_xpath)
        input_el.clear()
        input_el.send_keys(keyword)

        # 検索
        self.find_element_by_xpath(submit_btn_xpath).click()

    def find_text(self, xpath):
        """
        xpathはtextを囲んでいる要素を指す
        find_elementsを実行して、長さが0ならNoneを返す
        None出ないなら、最初の要素を返す
        """
        els = self.find_elements_by_xpath(xpath)
        if len(els) == 0:
            return None

        text = els[0].text
        return text

    def find_href(self, xpath):
        """
        xpathはtextを囲んでいる要素を指す
        find_elementsを実行して、長さが0ならNoneを返す
        None出ないなら、最初の要素を返す
        """
        els = self.find_elements_by_xpath(xpath)
        if len(els) == 0:
            return None

        href = els[0].get_attribute('href')
        return href

    def wait_until_all_elements_located(self, timeout=30):
        WebDriverWait(driver=self, timeout=timeout).until(
            EC.presence_of_all_elements_located)
