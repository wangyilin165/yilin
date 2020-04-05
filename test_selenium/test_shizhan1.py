# coding=utf-8
import json
from selenium import webdriver


class TestTest():
    def setup(self):
        # 声明一个变量chrome_opts，ChromeOptions是一个配置 chrome 启动属性的类,通过这个类，我们可以为chrome配置一些参数
        chrome_opts = webdriver.ChromeOptions()
        # 设置调试器地址debugger_address,地址为localhost,并设置端口
        chrome_opts.debugger_address = "127.0.0.1:9222"
        # 在终端敲入: chrome - remote - debugging - port = 9222，开启chrome_debug模式，打开一个用于调试的chrome浏览器
        # 需要和debugger_address的设置的端口号对应
        # 复用刚刚打开的浏览器
        self.driver = webdriver.Chrome(options=chrome_opts)
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(5)

    # def teardown(self):
    #     self.driver.quit()

    def test_test(self):
        # self.driver.find_element_by_css_selector(".index_service_cnt_item_title").click()
        # cookies=self.driver.get_cookies()
        # with open("cookies.txt","w") as f:
        #     json.dump(cookies,f)

        with open("cookies.txt", "r") as f:
            cookies = json.load(f)
            for cookie in cookies:
                if "expiry" in cookie.keys():
                    cookie.pop("expiry")
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        self.driver.find_element_by_css_selector(".index_service_cnt_item_title").click()
        self.driver.find_element_by_id("username").send_keys("hins")
        self.driver.find_element_by_id("memberAdd_english_name").send_keys("hinhin")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("hinhinlovely")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("12345678")
        self.driver.find_element_by_id("memberAdd_mail").send_keys("123456789@qq.com")

        self.driver.find_element_by_css_selector(".qui_btn.ww_btn.ww_btn_Blue.js_btn_continue").click()
