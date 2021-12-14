from selenium import webdriver
import time
import pytest


@pytest.mark.repeat(8)
def test_one():
    driver = webdriver.Edge()
    driver.get('https://q.yiban.cn/app/index/appid/707223#block2')
    time.sleep(10800)
    driver.find_element('id', 'account-txt').send_keys('18824048787')
    driver.find_element('id', 'password-txt').send_keys('liyuqing597')
    driver.find_element('id', 'login-btn').click()
    driver.implicitly_wait(5)

    driver.find_element('class name', 'morelink-img').click()
    driver.implicitly_wait(5)

    handle = driver.window_handles
    driver.switch_to.window(handle[1])
    driver.find_element('id', 'rk').click()
    driver.implicitly_wait(5)

    driver.find_element('id', 'an').click()
    localtime = time.asctime(time.localtime(time.time()))
    print('时间：', localtime)

    time.sleep(50)
    driver.quit()


if __name__ == '__main__':
    pytest.main(["-s", "test_flag.py"])
