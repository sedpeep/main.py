import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

username = 'wwhupthm'
password = 'da2m6tqxs0fg'
proxy_ip = 'http://2.56.119.93:5074'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--proxy-server=%s' % proxy_ip)

chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://whatismyipaddress.com/")
time.sleep(10)
