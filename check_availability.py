from selenium import webdriver
import time


def is_available(domain_name):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    url = 'https://godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=' + domain_name + ".com"
    browser.get(url)
    time.sleep(2)
    available = ''
    try:
        available = browser.find_element_by_xpath('/html/body/main/div/div/div/div/div[2]/div['
                                                  '1]/div/div/div/div/div/div[2]/div[1]/div[1]/span').text
    except:
        pass
    return available
