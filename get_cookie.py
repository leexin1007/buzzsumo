from selenium import webdriver
import time
'''
用账号登录平台，获取cookie
后续可以建立cookies池
'''


def demo():
    path = r'D:\chromedriver\chromedriver.exe'
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    # option.headless = True

    driver = webdriver.Chrome(path, options=option)
    driver.maximize_window()
    url = 'https://buzzsumo.com/'
    driver.get(url)
    time.sleep(1)

    # 因为请求页面之后，会出现一个确定接受cookie的页面显示在页面最下方，所以需要切换到最后一个页面（意思就是：切换到页面最上面的一个）
    driver.switch_to.window(driver.window_handles[-1])
    # html = driver.page_source

    driver.find_element_by_xpath('//button[@class="css-1pup4p5"]').click()  # 确认接受cookie
    time.sleep(1)
    driver.find_element_by_xpath('//a[@id="c-nav__login-btn"]/div/span').click()    # 进入登录账户页面
    time.sleep(1)
    driver.find_element_by_xpath('//input[@name="email"]').send_keys('readonme3@gmail.com')
    driver.find_element_by_xpath('//input[@name="password"]').send_keys('Buzzsumo@1234')
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="ax-progress-button"]/div').click()

    cookies = driver.get_cookies()
    # 获取cookie信息
    cookie_str = ''  # cookies信息
    nd_cookie = ''   # 所需的cookie值
    for i in cookies:
        item_str = i['name'] + '=' + i['value'] + ';'
        cookie_str += item_str
        if i['name'] == 'session_buzzsumo':
            # 获取字典中name为session_buzzsumo的 value值
            nd_cookie = i['value']
        else:
            pass

    return nd_cookie